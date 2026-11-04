from ex0.creature_factory import CreatureFactory, FlameFactory, AquaFactory
from ex1.healing_factory import HealingCreatureFactory
from ex1.transform_factory import TransformCreatureFactory
from ex2.battle_strategy import (
    BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy
)


def tournament(
    name: str,
    opponents_config: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print(name)

    creatures_with_strategies = []
    for factory, strategy in opponents_config:
        creature = factory.create_base()
        creatures_with_strategies.append((creature, strategy, factory))

    formatted_opponents = []
    for creature, strategy, factory in creatures_with_strategies:
        strategy_name = strategy.__class__.__name__.replace("Strategy", "")
        factory_class_name = factory.__class__.__name__
        if "Healing" in factory_class_name:
            display_name = "Healing"
        elif "Transform" in factory_class_name:
            display_name = "Transform"
        else:
            display_name = creature.name
        formatted_opponents.append(f"({display_name}+{strategy_name})")

    print(f"[ {', '.join(formatted_opponents)} ]")
    print("*** Tournament ***")
    print(f"{len(creatures_with_strategies)} opponents involved")
    print()

    for i in range(len(creatures_with_strategies)):
        for j in range(i + 1, len(creatures_with_strategies)):
            creature_1, strategy_1, _ = creatures_with_strategies[i]
            creature_2, strategy_2, _ = creatures_with_strategies[j]

            print("* Battle *")
            print(creature_1.describe())
            print(" vs.")
            print(creature_2.describe())
            print(" now fight!")

            try:
                strategy_1.act(creature_1)
                strategy_2.act(creature_2)
                print()
            except Exception as e:
                print(e)
                return


def main() -> None:
    # --- Tournament 0 (basic) ---
    t0_opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    tournament("Tournament 0 (basic)", t0_opponents)
    print()

    # --- Tournament 1 (error) ---
    t1_opponents = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    tournament("Tournament 1 (error)", t1_opponents)
    print()

    # --- Tournament 2 (multiple) ---
    t2_opponents = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    tournament("Tournament 2 (multiple)", t2_opponents)


if __name__ == "__main__":
    main()
