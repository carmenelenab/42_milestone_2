#!/usr/bin/env python3

def secure_archive(file_name: str, action: str, content: str = ""
                   ) -> tuple[bool, str]:
    try:
        with open(file_name, action) as open_file:
            if action == "r":
                to_read = open_file.read()
                return (True, to_read)
            elif action == "w":
                open_file.write(content)
                return (True, content)
    except Exception as e:
        return (False, f"{e}: {file_name}")
    return (False, "Action denied!")


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "r"))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("ancient_fragment.txt", "w",
                         "Content successfully written to file"))
    # print("\nUsing different action than w & r'secure_archive' to write previous content to a new file:")
    # print(secure_archive("ancient_fragment.txt", "a"))


if __name__ == "__main__":
    main()
