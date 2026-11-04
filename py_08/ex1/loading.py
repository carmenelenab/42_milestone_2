import sys
import importlib.util
from typing import Any

PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready"
}


def check_dependencies() -> tuple[bool, Any, Any, Any]:
    print("Checking dependencies:")

    loaded_mods = {}
    missing_packages = []

    for pkg_name, description in PACKAGES.items():
        if importlib.util.find_spec(pkg_name) is not None:
            if pkg_name == "matplotlib":
                mod = importlib.import_module("matplotlib.pyplot")
                parent_mod = importlib.import_module("matplotlib")
                version = getattr(parent_mod, "__version__", "unknown")
            else:
                mod = importlib.import_module(pkg_name)
                version = getattr(mod, "__version__", "unknown")
            print(f"\033[32;1m[OK] {pkg_name} ({version}) - "
                  f"{description}\033[0m")
            loaded_mods[pkg_name] = mod
        else:
            print(f"\033[31;1m[MISSING] {pkg_name} - Not installed\033[0m")
            missing_packages.append(pkg_name)

    is_available = len(missing_packages) == 0
    return (
        is_available,
        loaded_mods.get("pandas"),
        loaded_mods.get("numpy"),
        loaded_mods.get("matplotlib")
    )


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()

    dependencies_available, pd, np, plt = check_dependencies()

    if not dependencies_available:
        print(
            "\nPlease install dependencies using one of the following methods:"
        )
        print(
            "  \033[33;1;4mpython3 -m pip install -r requirements.txt\033[0m"
        )
        print("  # OR")
        print("  \033[33;1;4mpoetry install\033[0m")
        sys.exit(1)

    print()
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    data = np.random.randn(1000, 2)

    df: Any = pd.DataFrame(data, columns=["Signal_A", "Signal_B"])
    df["Matrix_Anomaly"] = df["Signal_A"] * df["Signal_B"]

    print("Generating visualization...")
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Signal_A"], df["Signal_B"],
                c=df["Matrix_Anomaly"], cmap="coolwarm", alpha=0.7)
    plt.title("Matrix Data Analysis - Zion Network")
    plt.xlabel("Signal A")
    plt.ylabel("Signal B")
    plt.colorbar(label="Anomaly Score")

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()
    print()
    print("Analysis complete!")
    print(f"Results saved to: \033[32m{output_file}\033[0m")

    print("\n-->If you need to uninstall / reset everything first, run:")
    print("\033[33;1mpython3 -m pip uninstall -r requirements.txt -y\033[0m")


if __name__ == "__main__":
    main()
