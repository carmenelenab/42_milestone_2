class Plant:

    def __init__(self, name: str, height: float, days: int, growth_rate: float):
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate
        print(f"Created: {self.name.capitalize()}: {self.height:.2f}cm, {self.days} days old")



    def grow(self) -> None:
        self.height += round(self.growth_rate, 3)


    def age(self) -> None:
        self.days += 1
    

    def show(self) -> None:
        week_days = 7
        growth = self.height;
        print("=== Garden Plant Growth ===")
        print(f"{self.name.capitalize()}: {self.height:.2f}cm, {self.days} days old")
        for day in range(week_days):
            print(f"=== Day {day + 1} ===")
            self.grow()
            self.age()
            print(f"{self.name.capitalize()}: {self.height:.2f}cm, {self.days} days old")
        print(f"Growth this week: {self.height - growth:.2f}cm\n")
        
        
if __name__ == "__main__":
    print("=== Plant Factory Output ==")
    tulip = Plant("tulip", 5, 2, 1.5)
    tulip.show()
    rose = Plant("rose", 10, 5, 0.3)
    rose.show()
    sunflower = Plant("sunflower", 15, 3, 2.45)
    sunflower.show()
    cactus = Plant("cactus", 15, 3, 2.45)
    cactus.show()
    fern = Plant("fern", 15, 3, 2.45)
    fern.show()