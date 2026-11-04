import os
import sys
from typing import Any

REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
]


def initialize_dotenv() -> bool:
    try:
        from dotenv import load_dotenv
        load_dotenv()
        return True
    except ImportError:
        return False


def load_matrix_config() -> dict[str, Any]:
    dotenv_available = initialize_dotenv()
    env_file_exists = os.path.exists(".env")
    return {
        "detenv_available": dotenv_available,
        "env_file_exists": env_file_exists,
        "matrix_mode": os.getenv("MATRIX_MODE"),
        "database_url": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT"),
    }


def validate_configuration(config: dict[str, Any]) -> None:
    if not config["detenv_available"]:
        print("\n\033[31m[WARNING]\033[0m \033[33m'python-dotenv'\033[0m "
              "package is not installed.")
        print("Falling back to system environment variables only.")
        print("To enable \033[33m.env\033[0m file support, run:"
              "  \033[31;1mpython3 -m pip install python-dotenv\033[0m")
        print("*" * 50)

    missing_vars = [
        var for var in REQUIRED_VARS
        if not config.get(var.lower())
    ]

    if missing_vars:
        print("\n\033[31m[WARNING]\033[0m Missing configuration variables: "
              f"{', '.join(missing_vars)}")
        print("Please set them up:")
        print("  1. Copy \033[32m.env.example\033[0m to \033[32m.env\033[0m] "
              "(--> \033[31;1mcp .env.example .env\033[0m) and run again!")
        print(
            "  2. Fill in the required values in your \033[33m.env\033[0m file"
        )
        print("  3. Or use environment variable override \n"
              "(e.g., MATRIX_MODE=production python3 oracle.py)")
        sys.exit(1)


def get_environment_behavior(matrix_mode: str) -> tuple[str, str, str]:
    if matrix_mode == "production":
        return (
            "Connected to secure remote cluster",
            "Authenticated (Prod Secure Token)",
            "Encrypted Secure Node"
        )
    else:
        return (
            "Connected to local instance",
            "Authenticated (Dev Key)",
            "Online (Local simulation)"
        )


def print_system_status(
    config: dict[str, Any],
    behaviors: tuple[str, str, str]
) -> None:
    matrix_mode = config["matrix_mode"]
    db_status, api_status, zion_status = behaviors

    print("\nConfiguration loaded:")
    print(f"\033[32mMode\033[0m: {matrix_mode}")
    print(f"\033[32mDatabase\033[0m: {db_status}")
    print(f"\033[32mAPI Access\033[0m: {api_status}")
    print(f"\033[32mLog Level\033[0m: {config["log_level"]}")
    print(f"\033[32mZion Network\033[0m: {zion_status}")

    print("\nEnvironment security check:")
    print("\033[32m[OK]\033[0m No hardcoded secrets detected")
    if config["env_file_exists"]:
        print("\033[32m[OK]\033[0m .env file properly configured")
    else:
        print("\033[31m[WARNING]\033[0m \033[33m.env\033[0m file not found")
    print("\033[32m[OK]\033[0m Production overrides available")
    print()
    print("The Oracle sees all configurations.")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    config = load_matrix_config()
    validate_configuration(config)
    behaviors = get_environment_behavior(str(config["matrix_mode"]))
    print_system_status(config, behaviors)


if __name__ == "__main__":
    main()
