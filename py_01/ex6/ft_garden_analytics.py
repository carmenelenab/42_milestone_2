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


def main(self):
    pass


if __name__ == "__main__":
    main()