from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_behavior() -> None:
    print("Testing Creature with healing capability")
    healing_factory = HealingCreatureFactory()
    print(" base:")
    base_heal = healing_factory.create_base()
    print(base_heal.describe())
    print(base_heal.attack())
    print(base_heal.heal())
    print(" evolve:")
    base_evolve = healing_factory.create_evolved()
    print(base_evolve.describe())
    print(base_evolve.attack())
    print(base_evolve.heal())
    print()


def test_transform_behavior() -> None:
    print("Testing Creature with transform capability")
    transforming_factory = TransformCreatureFactory()
    print(" base:")
    base_transform = transforming_factory.create_base()
    print(base_transform.describe())
    print(base_transform.attack())
    print(base_transform.transform())
    print(base_transform.attack())
    print(base_transform.revert())
    print(" evolved:")
    base_evolve = transforming_factory.create_evolved()
    print(base_evolve.describe())
    print(base_evolve.attack())
    print(base_evolve.transform())
    print(base_evolve.attack())
    print(base_evolve.revert())
    print()


def main() -> None:
    test_healing_behavior()
    test_transform_behavior()


if __name__ == "__main__":
    main()
