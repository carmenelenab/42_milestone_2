def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    input_data = ["25", "abc", "100", "-50", "ana", "40", "0", "-100"]
    i = 0
    while i < 8:
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
