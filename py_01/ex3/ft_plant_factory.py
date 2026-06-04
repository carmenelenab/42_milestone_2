class Plant:

    def __init__(self, name: str, height: float, days: int, growth_rate: float):
        self.name = "Created: " + name.capitalize()
        self.height = height
        self.days = days
        self.growth_rate = growth_rate
        self.show()

    def grow(self) -> None:
        self.height += round(self.growth_rate, 2)

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ==")
    tulip = Plant("tulip", 5, 2, 1.5)
    rose = Plant("rose", 10, 5, 0.3)
    oak = Plant("oak", 200, 365, 1.1)
    sunflower = Plant("sunflower", 15, 3, 2.45)
    cactus = Plant("cactus", 15, 3, 2.45)
    fern = Plant("fern", 15, 3, 2.45)


if __name__ == "__main__":
    ft_plant_factory()
