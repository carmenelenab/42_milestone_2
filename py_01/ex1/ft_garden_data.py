#!/usr/bin/env python3


class Plant:
    def show(name: str, height: int, age: int) -> None:
        print(f"{name.capitalize()}: {height}cm, {age} days old")


def ft_garden_intro() -> None:
    print("=== Garden Plant Registry ===")
    Plant.show("rose", 25, 30)
    Plant.show("sunflower", 80, 45)
    Plant.show("Cactus", 15, 120)


if __name__ == "__main__":
    ft_garden_intro()
