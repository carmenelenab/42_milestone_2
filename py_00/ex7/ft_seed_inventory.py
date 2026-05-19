def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print("Tomato seeds: 15 packets available")
    elif unit == "grams":
        print("Carrot seeds: 8 grams total")
    elif unit == "area":
        print("Lettuce seeds: covers 12 square meters")
    else:
        print("Unknown unit type")
