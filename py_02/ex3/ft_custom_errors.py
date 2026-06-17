class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def test_custom_error() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError()
    except GardenError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    errors = [PlantError(), WaterError()]
    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_error()
