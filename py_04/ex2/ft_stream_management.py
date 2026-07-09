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


def save_data(file_name: str, content: str) -> None:
    new_file = None
    sys.stdout.write(f"Saving data to '{file_name}'\n")
    sys.stdout.flush()
    try:
        new_file = open(file_name, "w")
        new_file.write(content)
        sys.stdout.write(f"Data saved in file '{file_name}'")
    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{file_name}': {e}"
            "\nData not saved!"
        )
    finally:
        if new_file is not None:
            new_file.close()


def header_footer_display(content: str) -> None:
    sys.stdout.write("\n---\n")
    sys.stdout.write(f"\n{content}\n")
    sys.stdout.write("\n---\n")


def main() -> None:
    if len(sys.argv) < 2:
        sys.stdout.write(f"Usage: {sys.argv[0]} <file>")
        return None
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===")
    sys.stdout.write(f"\nAccessing file '{sys.argv[1]}'\n")
    to_open = None
    content = None
    try:
        to_open = open(sys.argv[1])
        content = extract_data(to_open)
        header_footer_display(content)
    except Exception as e:
        sys.stderr.write("[STDERR] Error opening file "
                         f"'{sys.argv[1]}': {e}\n")
        return None
    finally:
        if to_open is not None:
            to_open.close()
            sys.stdout.write(f"\nFile '{sys.argv[1]}' closed.\n")
    sys.stdout.write("\nTransform data:")
    transformed_data = transform_data(content)
    header_footer_display(transformed_data)
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file_name = sys.stdin.readline().strip()
    if not new_file_name:
        sys.stdout.write("Not saving data!")
        return None
    save_data(new_file_name, transformed_data)


if __name__ == "__main__":
    main()
