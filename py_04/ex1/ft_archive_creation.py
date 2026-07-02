#!/usr/bin/env python3

import sys
import typing


def extract_data(opened_file: typing.IO[str]) -> str:
    return opened_file.read()


def transform_data(content: str) -> str:
    in_lines = content.splitlines()
    in_lines = [line + "#" for line in in_lines]
    content = "\n".join(in_lines)
    return content


def header_footer_print(content: str) -> None:
    print("---\n")
    print(content)
    print("\n---")


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
            header_footer_print(content)
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
            return None
        finally:
            if to_open is not None:
                to_open.close()
                print(f"File '{sys.argv[1]}' closed.")
    print("\nTransform data:")
    transformed_data = transform_data(content)
    header_footer_print(transformed_data)
    new_file_name = input("Enter new file name (or empty): ")
    if not new_file_name:
        print("Not saving data.")
        return None
    new_file = None
    try:
        new_file = open(new_file_name, "w")
        new_file.write(transformed_data)
        print(f"Saving data to '{new_file_name}'")
    finally:
        if new_file is not None:
            new_file.close()
            print(f"Data saved in file '{new_file_name}'")


if __name__ == "__main__":
    main()
