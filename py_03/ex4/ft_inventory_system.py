import sys


class Raise_Exceptions(Exception):
    pass


def check_min(inventory: dict[str, int]) -> tuple[str, int]:
    if not inventory:
        return ("None", 0)
    item_names = list(inventory.keys())
    item_min = item_names[0]
    min_q = inventory[item_min]
    for item in item_names:
        if inventory[item] < min_q:
            min_q = inventory[item]
            item_min = item
    return (item_min, min_q)


def check_max(inventory: dict[str, int]) -> tuple[str, int]:
    if not inventory:
        return ("None", 0)
    item_names = list(inventory.keys())
    item_max = item_names[0]
    max_q = inventory[item_max]
    for item in item_names:
        if inventory[item] > max_q:
            max_q = inventory[item]
            item_max = item
    return (item_max, max_q)


def create_inventory(user_input: str | None = None) -> dict[str, int]:
    inventory = {}
    arguments: list[str] = []
    if user_input is None:
        arguments = sys.argv[1:]
    else:
        arguments = list(user_input.split())

    for arg in arguments:
        try:
            if ":" not in arg:
                raise Raise_Exceptions(f"Error - invalid parameter '{arg}'")
            item_name = arg.split(":")[0]
            val = arg.split(":")[1]
            if not item_name:
                raise Raise_Exceptions(f"Warning: '{val}' has no valid key!")
            elif item_name in inventory:
                raise Raise_Exceptions(
                    f"Redundand item '{item_name}' - discarding")
            if not int(val):
                raise Exception()
            quantity = int(val)
            inventory.update({item_name: quantity})
        except Raise_Exceptions as e:
            print(e)
        except Exception as e:
            print(f"Quantity error for '{item_name}': {e}")
    return inventory


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print("Missing arguments!")
        user_input = input("Add your parameters: ")
        inventory = create_inventory(user_input)
    else:
        inventory = create_inventory()
    if not inventory:
        print("Warning: Empty or invalid inventory state.")
        return None
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

# Interactive methode, trust THE user :D
# new_item = input("Add a new item. "
#                  "Parameter must follow this format: "
#                  "<item_name>:<quantity>: ")
# new_key = new_item.split(":")[0]
# new_value = int(new_item.split(":")[1])
# inventory.update({new_key: new_value})
