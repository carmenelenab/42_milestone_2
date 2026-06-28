import random

PLAYERS = ["John", "sarah", "Michael", "emily", "jake", "Amanda", "Bob",
           "matthew", "Jessica", "david", "Ashley", "cody", "Taylor",
           "megan", "Alex"]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {PLAYERS}")
    cap_name = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names calitalized: {cap_name}")
    capitalized_only = [name for name in PLAYERS if name == name.capitalize()]
    print(f"New list of capitalized name only: {capitalized_only}")
    print()
    game_data = {name: random.randint(10, 1000) for name in cap_name}
    print(f"Score dict: {game_data}")
    score_avg = sum(game_data.values()) / len(game_data)
    print(f"Score average is {score_avg:.2f}")
    high_scores = {name: game_data[name] for name in game_data.keys()
                   if game_data[name] > score_avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
