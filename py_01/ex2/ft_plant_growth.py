class Plant:
    def grow(height: float):
        height += round(1.5, 3)
        return height


    def age(age: int):
        age += 1
        return age
    

    def show(name: str, height: float, days: int) -> None:
        week_days = 7
        growth = height;
        print("=== Garden Plant Growth ===")
        print(f"{name.capitalize()}: {height:.2f}cm, {days} days old")
        for day in range(week_days):
            print(f"=== Day {day + 1} ===")
            height = Plant.grow(height)
            days = Plant.age(days)
            print(f"{name.capitalize()}: {height:.2f}cm, {days} days old")
        print(f"Growth this week:{(height - growth):.2f}cm")


if __name__ == "__main__":
    Plant.show("tulip", 5, 2)
    # Plant.show("rose", 10, 3)
    # Plant.show("sunflower", 40, 20)
    # Plant.show("daisy", 7, 7)
