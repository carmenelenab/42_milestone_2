class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self._height = height
        self._age = age
        self.show()

    def grow(self, growth_rate: float) -> None:
        self.height += round(growth_rate, 2)

    def age(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height) -> None:
        if new_height < 0:
            self.print_error("height")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age) -> None:
        if new_age < 0:
            self.print_error("age")
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days")

    def print_error(self, parameter) -> None:
        print(f"{self.name} : Error, {parameter} can't be negative")
        print(f"{parameter.capitalize()} update rejected")

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old\n")


def ft_garden_security() -> None:
    print("=== Garden Security system ===")
    print("Plant created: ", end="")
    rose = Plant("rose", 10, 2)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-25)
    rose.set_age(-30)
    print("\nCurrent state: ", end="")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()
