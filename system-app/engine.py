"""
[THE SYSTEM] LIVING APP — v0.1: Command Parser & RPG Loot Engine
Skills Used: Sets, Tuples, Strings

Run this anytime to play your own engine:
    python system-app/engine.py
"""

# Locked recipe tuples: item_name -> (rarity, required_materials_set)
RECIPES: dict[str, tuple[str, set[str]]] = {
    "shadow_blade": ("EPIC", {"iron", "dark_crystal"}),
    "health_potion": ("COMMON", {"herb", "water"}),
    "ai_core": ("LEGENDARY", {"dark_crystal", "gold_chip", "mana_stone"}),
}


# ---------------------------------------------------------
# PART 1 — String + Tuple: Parse a player command
# ---------------------------------------------------------
def parse_command(raw: str) -> tuple[str, str]:
    """
    Clean `raw` (e.g. "  LOOT  iron  ") and return (action, target).
    Example:
      "  LOOT  iron  " -> ("loot", "iron")
      "bag"            -> ("bag", "")
    """
    # TODO: strip + lower + split, then return (action, target)
    pass


# ---------------------------------------------------------
# PART 2 — Set Difference: Check if player can craft item
# ---------------------------------------------------------
def craft_item(item_name: str, bag: set[str]) -> str:
    """
    1. If item_name not in RECIPES, return "Unknown recipe."
    2. Unpack (rarity, needed) from RECIPES[item_name]
    3. Find missing materials using set difference: needed - bag
    4. If missing is not empty, return f"Missing: {sorted(missing)}"
    5. Otherwise return f"CRAFTED [{rarity}] {item_name}!"
    """
    # TODO: Implement craft_item
    pass


# ---------------------------------------------------------
# INTERACTIVE GAME LOOP (Runs once Part 1 & 2 work!)
# ---------------------------------------------------------
def play() -> None:
    bag: set[str] = {"iron", "herb"}
    print("=== THE SYSTEM ENGINE v0.1 ===")
    print("Commands: loot <item> | drop <item> | craft <item> | bag | quit")
    print(f"Recipes: {list(RECIPES.keys())}")

    while True:
        raw = input("\n> ")
        action, target = parse_command(raw)

        if action == "quit":
            print("System offline.")
            break
        elif action == "bag":
            print("Inventory:", sorted(bag))
        elif action == "loot" and target:
            bag.add(target)
            print(f"+ Added '{target}' to bag.")
        elif action == "drop" and target:
            bag.discard(target)
            print(f"- Dropped '{target}' (if it was there).")
        elif action == "craft" and target:
            print(craft_item(target, bag))
        else:
            print("Try: loot dark_crystal | craft shadow_blade | bag | quit")


if __name__ == "__main__":
    # Quick self-tests before launching the game
    assert parse_command("  LOOT  iron ") == ("loot", "iron")
    assert parse_command("BAG") == ("bag", "")
    assert craft_item("shadow_blade", {"iron"}) == "Missing: ['dark_crystal']"
    assert craft_item("shadow_blade", {"iron", "dark_crystal"}) == "CRAFTED [EPIC] shadow_blade!"
    assert craft_item("laser", {"iron"}) == "Unknown recipe."

    play()
