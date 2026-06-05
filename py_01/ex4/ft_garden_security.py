class Plant:

    def __init__(self, name: str, _height: float, _age: int, growth_rate: float):
        self.name = "Plant created: " + name.capitalize()
        self._height = 0
        self._age = 0
        self.growth_rate = growth_rate
        # self.show()

    def grow(self) -> None:
        self._height += round(self.growth_rate, 2)

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def print_error(self, parameter) -> None:
        print(f"{self.name} : Error, {parameter}  can't be negative")

    def get_height(self):
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height):
        if new_height < 0:
            self.print_error("height")
        else:
            self._height = new_height
            self.show()

    def set_age(self, new_age):
        if new_age < 0:
            self.print_error("age")
        else:
            self._age = new_age
            self.show()


def ft_garden_security() -> None:
    print("=== Garden Security system ===")
    tulip = Plant("tulip", 5, 2, 1.5)
    tulip.set_height(-5)


if __name__ == "__main__":
    ft_garden_security()
