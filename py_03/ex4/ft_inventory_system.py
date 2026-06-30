import sys


def check_min(inventory: dict[str, int]) -> tuple[str, int]:
    item_names = list(inventory.keys())
    item_min = item_names[0]
    min_q = inventory[item_min]
    for item in item_names:
        if inventory[item] < min_q:
            min_q = inventory[item]
            item_min = item
    return (item_min, min_q)


def check_max(inventory: dict[str, int]) -> tuple[str, int]:
    item_names = list(inventory.keys())
    item_max = item_names[0]
    max_q = inventory[item_max]
    for item in item_names:
        if inventory[item] < max_q:
            max_q = inventory[item]
            item_max = item
    return (item_max, max_q)


def create_inventory() -> dict[str, int]:
    inventory = {}
    for arg in sys.argv[1:]:
        if ":" not in arg:
            continue
        i = 0
        while i < len(arg):
            if arg[i] == ":":
                break
            i += 1
        val = arg[i + 1: len(arg)]
        try:
            item_name = arg[:i]
            quantity = int(val)
            if item_name in inventory:
                print(f"Redundand item '{item_name}' - discarding")
                continue
            inventory.update({item_name: quantity})
        except Exception as e:
            print(f"Error - invalid parameter '{val}'")
            print(f"Quantity error for '{item_name}': {e}")
    return inventory


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    inventory = create_inventory()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: "
          f"{sum(inventory.values())}")
    for item in inventory.keys():
        print(f"Item {item} represents "
              f"{(inventory[item] / sum(inventory.values()) * 100):.1f}%")
    max_stats = check_max(inventory)
    min_stats = check_min(inventory)
    print(f"Item most abundent: '{max_stats[0]}' with quatity {max_stats[1]}")
    print(f"Item least abundent: '{min_stats[0]}' with quatity {min_stats[1]}")

    inventory.update({"magic powder": 10})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
