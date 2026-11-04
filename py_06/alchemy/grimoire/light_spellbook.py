#!/usr/bin/env python3

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["fire", "air", "earth", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validation_result = validate_ingredients(ingredients)
    if "VALID" in validation_result:
        return (f" Spell recorded: {spell_name}: {validation_result})")
    return f"Spell rejected: {spell_name}: {validation_result})"
