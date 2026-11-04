#!/usr/bin/env python3

import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end="")
    try:
        alchemy.create_earth()
    except AttributeError as e:
        print(f"{e.__class__.__name__}: {e}, Did you mean: 'create_air'?")


if __name__ == "__main__":
    main()
