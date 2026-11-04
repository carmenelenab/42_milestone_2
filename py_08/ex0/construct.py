import sys
import os
import site


def main() -> None:
    is_venv = (sys.prefix != sys.base_prefix) or (
        "VIRTUAL_ENV" in os.environ
    )
    if is_venv:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
        venv_name = os.path.basename(venv_path)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment path: {venv_path}")
        print()
        print("\033[32mSUCCESS\033[0m: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print()
        print("Package installation path:")
        for path in site.getsitepackages():
            print(path)
    else:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("\033[31mWARNING\033[0m: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("  \033[33mpython3 -m venv matrix_env\033[0m")
        print(" \033[33;4msource matrix_env/bin/activate\033[0m # On Unix")
        print(r" matrix_env\Scripts\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
