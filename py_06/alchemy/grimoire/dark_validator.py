#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    ing_list = ingredients.split(", ") if ingredients else []
    items = [
        ing.capitalize() if i == 0 else ing for i, ing in enumerate(ing_list)
    ]
    if len(items) > 1:
        formatted = ", ".join(items[:-1]) + " and " + items[-1]
    else:
        formatted = "".join(items)
    if any(ing in ingredients_lower for ing in allowed):
        return f"{formatted} - VALID"
    return f"{formatted} - INVALID"
