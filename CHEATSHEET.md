# Personal Knowledge Cheatsheet

A living reference of every core concept I’ve learned across the 6 phases — automatically updated by **THE SYSTEM** as I clear quests.

---

## Phase 1 — Python Foundations

### 1. Variables & Data Types
- `int` (whole numbers), `float` (decimals), `str` (text), `bool` (`True`/`False`).
- Convert types explicitly: `int("42")`, `float("3.14")`, `str(100)`.

### 2. Conditions & Loops
- `if / elif / else` checks conditions top-to-bottom.
- `for item in iterable:` loops over a known sequence (`list`, `dict`, `set`, `range(n)`).
- `while condition:` loops until a condition becomes `False` — always ensure the exit condition can be reached.
- `break` exits the loop early; `continue` skips to the next iteration.

### 3. Functions, `return` & Variable Scope
- `return` sends a value back to the caller so it can be reused; `print()` only displays to the screen.
- **Local variables** live inside a function; prefer passing arguments and returning values over mutating `global` variables.

### 4. Lists (`list`)
- Ordered, mutable, allows duplicates: `items = ["a", "b", "c"]`.
- Common operations: `.append(x)`, `.pop()`, `len(items)`, slicing `items[0:2]`.

### 5. Exception Handling (`try / except`)
- Catch specific errors instead of bare `except:`:
  ```python
  try:
      num = int(user_input)
  except ValueError:
      print("Please enter a valid number.")
  ```

---

## Phase 2 — Python Developer Foundations

### 6. Dictionaries (`dict`)
- Key-value pairs, fast lookup by key: `user = {"name": "Zack", "level": 4}`.
- **Safe lookup:** `user.get("role", "guest")` returns `"guest"` instead of crashing with `KeyError`.
- **Looping:** `for k, v in user.items():` iterates over both keys and values.
- `.keys()`, `.values()`, `.update()`, `.pop(key, default)`.

### 7. Sets (`set`)
- Unordered collection of **unique** items (automatically removes duplicates): `s = {"Ali", "Sara"}`.
- **Adding / Removing:**
  - `s.add("Adam")`
  - `s.remove("Abu")` → raises `KeyError` if missing.
  - `s.discard("Bob")` → safe; does nothing if missing.
- **Set Math:**
  - Union (either): `a.union(b)` or `a | b`
  - Intersection (both): `a.intersection(b)` or `a & b`
  - Difference (only in `a`): `a.difference(b)` or `a - b`

---

## Engineering & GitHub

### 8. Daily Git Workflow
- `git status` — check current branch and modified/untracked files.
- `git add .` → `git commit -m "day-XX: <topic>"` → `git push origin main`.
- `git log --oneline --graph` — inspect commit history cleanly.
