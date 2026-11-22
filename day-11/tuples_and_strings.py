"""
[THE SYSTEM] QUEST — Tuples & String Manipulation
Started: 19:50 (2026-11-21)

Complete each function below, then run:
    python day-11/tuples_and_strings.py
"""


# ---------------------------------------------------------
# WARM-UP ENCOUNTER (+40 XP) — Exception Handling Review
# ---------------------------------------------------------
def safe_to_int(text: str, default: int = 0) -> int:
    """
    Convert `text` to an int.
    If `text` is not a valid integer (e.g., "abc" or "3.5"), return `default`.
    """
    # TODO: Use try/except ValueError
    try:
        return int(text)
    except ValueError:
        return default



# ---------------------------------------------------------
# QUEST 1 — Tuples & Unpacking
# ---------------------------------------------------------
def min_max(numbers: list[int]) -> tuple[int, int]:
    """
    GOAL: Find the smallest and largest number in `numbers`, and return both together.
    EXAMPLE:
      min_max([10, 3, 25, 7]) -> (3, 25)
      min_max([])             -> (0, 0)

    CONCEPT INVOLVED:
      - Empty-list guard: `if not numbers:` means "if the list is empty"
      - Built-in functions: `min(numbers)` and `max(numbers)`
      - Tuple return: `return (smallest, largest)` packs 2 values into one tuple
    """
    # TODO 1: If `numbers` is empty (`if not numbers:`), return (0, 0)
    # TODO 2: Otherwise return (min(numbers), max(numbers))
    if not numbers:
        return (0,0)
    return (min(numbers), max(numbers))


# ---------------------------------------------------------
# QUEST 2 — String Cleaning & Formatting
# ---------------------------------------------------------
def format_tags(raw_tags: str) -> str:
    """
    GOAL: Clean up messy comma-separated tags, remove duplicates, sort, and join with " | ".
    EXAMPLE:
      format_tags("  Python,  AI , python ,  FastAPI ") -> "ai | fastapi | python"
      format_tags("  , , ")                             -> ""

    CONCEPT INVOLVED:
      - String splitting & cleaning: `raw_tags.split(",")`, `.strip()`, `.lower()`
      - Deduplication with a set: `unique = set()` -> `unique.add(tag)` (only if `tag` is not empty!)
      - Sorting & joining: `sorted(unique)` gives an alphabetical list, `" | ".join(...)` combines them
    """
    # TODO 1: Create an empty set `unique = set()`
    # TODO 2: Loop `for item in raw_tags.split(","):`
    #           clean = item.strip().lower()
    #           if clean:  (skip empty strings!)
    #               unique.add(clean)
    # TODO 3: Return `" | ".join(sorted(unique))`
    unique = set()
    for item in raw_tags.split(","):
        clean = item.strip().lower()
        if clean:
            unique.add(clean)
    return " | ".join(sorted(unique))

    


# ---------------------------------------------------------
# QUEST 3 (BUG HUNT) — Fix the Broken Code
# ---------------------------------------------------------
def make_user_badge(username: str) -> tuple[str]:
    """
    GOAL: Return a 1-item tuple with the cleaned, uppercase username.
    EXAMPLE:
      make_user_badge("  zack ") -> ("ZACK",)

    CONCEPT INVOLVED:
      - 1-item tuple trap: `("ZACK")` is just a string! A 1-item tuple MUST have a trailing comma: `("ZACK",)`
    """
    # TODO: Fix the return line so it returns a 1-item tuple instead of a str
    cleaned = username.strip().upper()
    return (cleaned,)


# ---------------------------------------------------------
# SELF-TESTS (Do not edit below — run the file to check!)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Warm-up tests
    assert safe_to_int("42") == 42
    assert safe_to_int("abc", -1) == -1
    assert safe_to_int("3.14") == 0

    # Quest 1 tests
    assert min_max([10, 3, 25, 7]) == (3, 25)
    assert min_max([]) == (0, 0)
    low, high = min_max([5, 1, 9])
    assert low == 1 and high == 9

    # Quest 2 tests
    assert format_tags("  Python,  AI , python ,  FastAPI ") == "ai | fastapi | python"
    assert format_tags("  , , ") == ""

    # Quest 3 tests
    badge = make_user_badge("  zack ")
    assert isinstance(badge, tuple) and badge == ("ZACK",)

    print("ALL QUESTS CLEARED!")
