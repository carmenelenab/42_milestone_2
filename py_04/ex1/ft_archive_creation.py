#!/usr/bin/env python3

import sys

def display_data() -> None:
    

def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        to_read = None
        try:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file '{sys.argv[1]}'")
            to_read = open(sys.argv[1])
            to_create = input("Add the name of the new created file: ").write()
            content = to_read.read()
            print("---\n")
            for elem in content:
                to_create.write(elem)
                if elem in ("\n", "\0"):
                    to_create.write("#")
            print("\n---")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        finally:
            if to_read is not None:
                to_read.close()
                print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
