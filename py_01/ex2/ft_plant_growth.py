class Plant:

    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float):
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate
        self.show()

    def grow(self) -> None:
        self.height += round(self.growth_rate, 3)

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.2f}cm, \
              {self.days} days old")


def ft_plant_growth() -> None:
    week_days = 7
    print("=== Garden Plant Growth ===")
    tulip = Plant("tulip", 5, 2, 1.5)
    growth = tulip.height
    for day in range(week_days):
        print(f"=== Day {day + 1} ===")
        tulip.grow()
        tulip.age()
        print(f"{tulip.name.capitalize()}: {tulip.height:.1f}cm, \
              {tulip.days} days old")
    print(f"Growth this week: {tulip.height - growth:.1f}cm\n")


if __name__ == "__main__":
    ft_plant_growth()
