import math


def get_player_pos() -> tuple:
    while True:
        try:
            received = input(
                "Enter new coordinates as floats in format 'x,y,z': ")
            coordonates_list = []
            current_text = ""

            for elem in received:
                if elem == ",":
                    coordonates_list += [float(current_text)]
                    current_text = ""
                else:
                    if elem != ' ':
                        current_text += elem
            coordonates_list += [float(current_text)]
            if len(coordonates_list) != 3:
                print("Invalid syntax")
                continue
            return tuple(coordonates_list)
        except Exception as e:
            print(f"Error on parameter '{current_text}': {e}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    print(
        f"Distance to center: {math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2):.4f}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    print(
        f"Distance between the 2 sets of coordinates: {math.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2 + (pos2[2]-pos1[2])**2):.4f}")


if __name__ == "__main__":
    main()
