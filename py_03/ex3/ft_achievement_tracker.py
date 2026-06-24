import random

ACHIEV_POOL = {
    "First Step",
    "Cartographer",
    "Night Owl",
    "Treasure Hunter",
    "Globetrotter",
    "Deep Diver",
    "Alchemist",
    "Scholar",
    "Monster Slayer",
    "Unstoppable",
    "Eagle Eye",
    "Giant Tamer",
    "Pacifist",
    "Last Stand",
    "Weapon Master",
    "Brawler",
    "Rich Zone",
    "Hoarder",
    "Investor",
    "Black Market",
    "Collector",
    "Master Chef",
    "Lumberjack",
    "Speedrunner",
    "Ghost",
    "Survivor",
    "Lucky Seven",
    "Serious Bug",
    "Mentor",
    "Completionist",
}


def gen_player_achievements() -> set[str]:
    achievements_no = random.randint(1, 15)
    player_achievements = random.sample(list(ACHIEV_POOL), achievements_no)
    return set(player_achievements)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    players = []
    i = 0
    for name in names:
        achievement = gen_player_achievements()
        players.append(achievement)
        print(f"\tPlayer {name.capitalize()}: {players[i]}")
        i += 1
    print(
        "\n\tAll distinct achievements: "
        f"{set.union(players[0], players[1], players[2], players[3])}"
    )

    print(
        "\n\tCommon achievements: "
        f"{set.intersection(players[0], players[1], players[2], players[3])}\n"
    )

    print(
        "\tOnly Alice has: "
        f"{players[0].difference(players[1], players[2], players[3])}"
    )
    print(
        "\tOnly Bob has: "
        f"{players[1].difference(players[2], players[3], players[0])}"
    )
    print(
        "\tOnly Charlie has: "
        f"{players[2].difference(players[3], players[0], players[1])}"
    )
    print(
        "\tOnly Dylan has: "
        f"{players[3].difference(players[0], players[1], players[2])}"
    )
    print()
    i = 0
    for name in names:
        players[i]
        print(f"\t{name} is missing: {ACHIEV_POOL - players[i]}")
        i += 1


if __name__ == "__main__":
    main()
