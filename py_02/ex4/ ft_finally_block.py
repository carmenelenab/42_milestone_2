class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = " Invalid plant name to water:") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError()
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants..")
    print("Opening watering system")
    vegetables = ["Tomato", "Lettuce", "Carrots"]
    for veggi in vegetables:
        try:
            water_plant(veggi)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
    print("Closing watering system\n")

    print("Testing invalid plants...")
    vegetables = ["Tomato", "lettuce", "carrots"]
    for veggi in vegetables:
        try:
            water_plant(veggi)
        except PlantError as e:
            print(f"Caught PlantError: {e} '{veggi}'")
            print(".. ending tests and returning to main")
            break
    print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
