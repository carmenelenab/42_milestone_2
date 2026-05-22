class Plant:
    def show(name: str, height: float, age: int) -> None:
        print("=== Garden Plant Growth ===")
        print(f"{name.capitalize()}: {height}cm, {age} days old")

    def grow(name: str, height: float):
        if name == "Rose":
            height += round(0.3, 2)
        elif name == "Sunflower":
            height += round(11, 2)
        elif name == "Cactus":
            height += round(1.156889, 2)
        return (height)

    def age(age: int):
        age += 1
        return age
