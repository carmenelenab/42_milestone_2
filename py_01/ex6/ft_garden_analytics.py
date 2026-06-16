def display(plant: "Plant") -> None:
    plant._analytics.display()


class Plant:
    class _Analytics:
        def __init__(self) -> None:
            self._age_count = 0
            self._grow_count = 0
            self._show_count = 0
            self._shade_count = 0
            self._is_tree = False

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def increment_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )
            if self._is_tree:
                print(f" {self._shade_count} shade")

    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self._height = height
        self._age = age
        self._analytics = self._Analytics()

    def grow(self, growth_rate: float, days: int) -> None:
        self._analytics.increment_grow()
        for day in range(0, days):
            self._height += round(growth_rate, 2)

    def age(self, days: int) -> None:
        self._analytics.increment_age()
        for day in range(0, days):
            self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    @staticmethod
    def age_check(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

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
        self._analytics.increment_show()
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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._analytics._is_tree = True

    def produce_shade(self) -> None:
        self._analytics.increment_shade()

    def show(self) -> None:
        super().show()
        # self.produce_shade()
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
        print("=== Vegetable")

    def age(self, days: int) -> None:
        super().age(days)
        for day in range(0, days):
            self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")


def main() -> None:
    # print("=== Garden statistics ===")
    # print("=== Check year-old")
    # print(f"Is 30 days more than a year? -> {Plant.age_check(30)}")
    # print(f"Is 400 days more than a year? -> {Plant.age_check(400)}")

    # print()
    # print("=== Flower")
    # rose = Flower("rose", 15, 10, "red")
    # rose.show()
    # display(rose)
    # rose.grow(0.8, 10)
    # rose.bloom()
    # display(rose)

    print()
    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display(oak)
    oak.produce_shade()
    display(oak)

    # print()
    # print("=== Seed")
    # sunflower = Seed("sunflower", 80.0, 45, "yellow")
    # sunflower.show()
    # sunflower.grow(1.5, 20)
    # sunflower.age(20)
    # sunflower.bloom()
    # display(sunflower)

    # print()
    # print("=== Anonymous")
    # anonymous_plant = Plant.anonymous()
    # anonymous_plant.show()
    # display(anonymous_plant)


if __name__ == "__main__":
    main()
