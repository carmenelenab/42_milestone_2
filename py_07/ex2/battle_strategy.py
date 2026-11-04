from abc import ABC, abstractmethod
from typing import cast
from ex0.creature import Creature
from ex1.capability import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                "Battle error, aborting tournament:"
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        transfomable_creature = cast(TransformCapability, creature)
        print(transfomable_creature.transform())
        print(creature.attack())
        print(transfomable_creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        healing_creature = cast(HealCapability, creature)
        print(creature.attack())
        print(healing_creature.heal())
