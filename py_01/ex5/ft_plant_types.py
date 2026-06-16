class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self._height = height
        self._age = age

    def grow(self, growth_rate: float, days: int) -> None:
        for day in range(0, days):
            self._height += round(growth_rate, 2)

    def age(self, days: int) -> None:
        for day in range(0, days):
            self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            self.print_error("height")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            self.print_error("age")
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days")

    def print_error(self, parameter: str) -> None:
        print(f"{self.name} : Error, {parameter} can't be negative")
        print(f"{parameter.capitalize()} update rejected")

    def show(self) -> None:
        print(f"{self.name}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        print(f"{self.name.capitalize()} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        print(f" {self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def show(self) -> None:
        super().show()
        self.produce_shade()
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide. "
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: float,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def age(self, days: int) -> None:
        super().age(days)
        for day in range(0, days):
            self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant type ===")

    print("\n=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    print()

    # tulip = Flower("tulip", 20, 3, "red")
    # tulip.show()
    # tulip.bloom()
    # print()

    print("=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    print()

    print("=== Vegetable")
    tomato = Vegetable("tomato", 5, 10, "april", 0)
    tomato.show()
    tomato.age(20)
    tomato.grow(2.1, 20)
    tomato.show()


if __name__ == "__main__":
    main()
