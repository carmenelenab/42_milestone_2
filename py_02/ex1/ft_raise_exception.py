def input_temperature(temp_str: str) -> int:
    try:
        if int(temp_str) < 0:
            try:
                
    except:
        print()
    return int(temp_str)
    




def test_temperature() -> None:
    print("=== Garden Temperature ===")
    input_data = ["25", "abc", "100", "-50"]
    i = 0
    while i < 2:
        print()
        print(f"Input data is '{input_data[i]}'")
        try:
            data = input_temperature(input_data[i])
            print(f"Temperature is now {data}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        i += 1
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
