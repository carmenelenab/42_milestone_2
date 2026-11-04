#!/usr/bin/env python3


def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
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
