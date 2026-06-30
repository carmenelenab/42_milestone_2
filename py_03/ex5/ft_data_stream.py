import typing
import random

PLAYERS = [
        "Alex", "Andrei", "Antonia", "Ana", "Alin", "Amalia", "Adrian", "Anca",
        "Aurelian", "Augustina", "Bogdan", "Bianca", "Beatrice", "Barbu",
        "Beniamin", "Berta", "Bănel", "Brândușa", "Bucur", "Bella", "Cosmin",
        "Cristina", "Cătălin", "Camelia", "Cezar", "Corina", "Ciprian",
        "Clara", "Crina", "Carmen", "Daniel", "Diana", "Denis", "Doina",
        "Darius", "Daria", "Dumitru", "Dorina", "David", "Dinu", "Elena",
        "Eduard", "Emanoil", "Emilia", "Eugen", "Ecaterina", "Erick", "Erika",
        "Emil", "Eliza", "Florin", "Flavia", "Fabiola", "Filip", "Florentina",
        "Felix", "Felicia", "Flavian", "Fiona", "Fred", "George", "Gabriela",
        "Gheorghe", "Georgiana", "Gabriel", "Geta", "Gigi", "Gloria", "Goran",
        "Gia", "Horia", "Hristina", "Horațiu", "Henrietta", "Horea", "Hanna",
        "Haralambie", "Hilda", "Hansi", "Hugo", "Ioan", "Ioana", "Ionuț",
        "Iulia", "Ilie", "Irina", "Iosif", "Isabela", "Iulian", "Iasmina",
        "Laura", "Liviu", "Larisa", "Laurențiu", "Lidia", "Lucian", "Lucia",
        "Luca", "Loredana", "Liliana"
    ]

ACTIONS = [
        "run", "eat", "sleep", "bike", "code", "text", "work", "swim", "jump",
        "climb", "read", "write", "dance", "sing", "laugh", "cry", "cook",
        "bake", "drive", "fly", "fight", "defend", "loot", "craft", "trade",
        "buy", "sell", "cast_spell", "heal", "teleport", "meditate", "train",
        "level_up", "explore", "fish", "hunt", "mine", "chop_wood", "smelt",
        "forge", "talk", "whisper", "shout", "listen", "think", "study",
        "teach", "learn", "solve", "build", "destroy", "repair", "paint",
        "draw", "sculpt", "photograph", "film", "watch", "hide", "sneak",
        "steal", "gamble", "invest", "rest", "pray", "curse", "enchant",
        "disenchant", "summon", "banish", "travel", "sail", "ride_horse",
        "scout", "track", "trap", "tame", "feed", "pet", "clean", "wash",
        "iron", "dust", "vacuum", "garden", "plant", "harvest", "brew",
        "mix_potion", "gamble", "compete", "win", "lose", "surrender",
        "celebrate", "mourn", "insult", "compliment", "hug", "kiss"
    ]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(list_10: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while len(list_10) > 0:
        consume = random.choice(list_10)
        list_10.remove(consume)
        yield (consume)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event = gen_event()
    for i in range(1000):
        current_event = next(event)
        print(f"Event {i}: Player {current_event[0]} "
              f"did action {current_event[1]}")

    list_10 = []
    event = gen_event()
    for i in range(10):
        list_10.append(next(event))
    print(f"\nBuilt list of 10 events: {list_10}")

    for current_event in consume_event(list_10):
        print(f"Got event from list: {current_event}")
        print(f"Remains in list: {list_10}")


if __name__ == "__main__":
    main()
