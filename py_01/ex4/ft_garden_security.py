class Plant:

    def __init__(self, name: str, height: float, days: int, growth_rate: float):
        self.name = "Plant created: " + name.capitalize()
        self.height = height
        self.days = days
        self.growth_rate = growth_rate
        # self.show()

    def grow(self) -> None:
        self.height += round(self.growth_rate, 2)

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def print_error(self, parameter) -> None:
        print(f"{self.name} : Error, {parameter}  can't be negative")

    def get_height(self):
        return self.get_height

    def get_age(self):
        return self.get_age

    def set_height(self):
        if self.get_height < 0:
            self.print_error()
        else:
            self.show()

    def set_age(self):
        if self.get_age < 0:
            self.print_error()
        else:
            self.show()


def ft_garden_security() -> None:
    print("=== Garden Security system ===")
    tulip = Plant("tulip", 5, 2, 1.5).set_height()


if __name__ == "__main__":
    ft_garden_security()
