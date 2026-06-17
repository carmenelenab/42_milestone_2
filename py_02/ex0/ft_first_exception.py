def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    input_data = ["25", "abc"]
    i = 0
    while i < 2:
        print(f"\nInput data is '{input_data[i]}'")
        try:
            data = input_temperature(input_data[i])
            print(f"Temperature is now {data}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        i += 1
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
