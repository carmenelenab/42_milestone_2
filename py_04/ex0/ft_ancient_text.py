#!/usr/bin/env python3

import sys
import typing


def extract_data(opened_file: typing.IO[str]) -> str:
    content = opened_file.read()
    return (content)
    


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return None
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        to_open = None
        try:
            to_open = open(sys.argv[1])
            content = extract_data(to_open)
            print("---\n")
            print(content)
            print("\n---")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        finally:
            if to_open is not None:
                to_open.close()
                print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
