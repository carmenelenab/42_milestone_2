import random
def gen_player_achievements() -> set:
    achievments_pool = [
    "First Step", "Cartographer", "Night Owl", "Treasure Hunter", "Globetrotter",
    "Deep Diver", "Alchemist", "Scholar", "Monster Slayer", "Unstoppable",
    "Eagle Eye", "Giant Tamer", "Pacifist", "Last Stand", "Weapon Master",
    "Brawler", "Rich Zone", "Hoarder", "Investor", "Black Market",
    "Collector", "Master Chef", "Lumberjack", "Speedrunner", "Ghost",
    "Survivor", "Lucky Seven", "Serious Bug", "Mentor", "Completionist"
    ]

    achievements_no = random.randint(1, len(achievments_pool))
    player_achievements = random.sample(achievments_pool, achievements_no)
    return set(player_achievements)

def main() -> None:
    print("=== Achievement Tracker System ===")
    alice_achiev = gen_player_achievements()
    bob_achiev = gen_player_achievements()
    charlie_achiev = gen_player_achievements()
    dylan_achiev = gen_player_achievements()
    ion_achiev = gen_player_achievements()
    print(f"Player Alice: {alice_achiev}\n")
    print(f"Player Bob: {bob_achiev}\n")
    print(f"Player Charlie: {charlie_achiev}\n")
    print(f"Player Dylan: {dylan_achiev}\n")
    print(f"Player Ion: {ion_achiev}\n")

    distinct_achiev = set.union(
        alice_achiev, bob_achiev, charlie_achiev, dylan_achiev, 
        ion_achiev
    )
    print(f"All distinct achievements: {distinct_achiev}")

    common_achiev = set.intersection(alice_achiev, bob_achiev, charlie_achiev,
        dylan_achiev, ion_achiev
    )
    print(f"\nCommon achievements: {common_achiev}\n")
    print(f"Only Alice has: {set.difference(alice_achiev, bob_achiev, charlie_achiev, dylan_achiev, ion_achiev)}")
    print(f"Only Bob has: {set.difference(bob_achiev, alice_achiev, charlie_achiev, dylan_achiev, ion_achiev)}")
    print(f"Only Charlie has: {set.difference(charlie_achiev, bob_achiev, alice_achiev, dylan_achiev, ion_achiev)}")
    print(f"Only Dylan has: {set.difference(dylan_achiev, alice_achiev, bob_achiev, charlie_achiev, ion_achiev)}")
    print(f"Only Ion has: {set.difference(ion_achiev, alice_achiev, bob_achiev, charlie_achiev, dylan_achiev)}")
    # for achiev in ana:
    #     print(achiev, end=" ")

    
if __name__ == "__main__":
    main()