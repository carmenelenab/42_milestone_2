from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory_behavior(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print("Testing factory")
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def test_battle_behavior(
    flame_fact: FlameFactory,
    aqua_fact: AquaFactory
) -> None:
    flame_base = flame_fact.create_base()
    aqua_base = aqua_fact.create_base()
    print("Testing battle")
    print(flame_base.describe())
    print(" vs.")
    print(aqua_base.describe())
    print(" fight!")
    print(flame_base.attack())
    print(aqua_base.attack())
    print()


def main() -> None:
    test_factory_behavior(FlameFactory())
    test_factory_behavior(AquaFactory())
    test_battle_behavior(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
