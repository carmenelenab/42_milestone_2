class Plant:

    def __init__(self, name: str, height: float, days: int):
        self.name = "Created: " + name.capitalize()
        self.height = height
        self.days = days
        self.show()

    def grow(self, growth_rate: float) -> None:
        self.height += round(growth_rate, 2)

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ==")
    tulip = Plant("tulip", 5, 2)
    rose = Plant("rose", 10, 5)
    oak = Plant("oak", 200, 365)
    sunflower = Plant("sunflower", 15, 3)
    cactus = Plant("cactus", 15, 3)
    fern = Plant("fern", 15, 3)


if __name__ == "__main__":
    ft_plant_factory()
