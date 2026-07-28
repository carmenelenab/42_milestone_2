def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 32
    return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    i = 0
    while i < 5:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except Exception as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        i += 1

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
