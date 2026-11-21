# Master Lesson Book — In-Depth Engineering Guide

A complete, in-depth reference of every topic learned so far — covering **mental models**, **under-the-hood mechanics**, **senior Pythonic patterns**, and **production edge cases**. Updated automatically by **THE SYSTEM** as new topics are mastered.

---

## Phase 1 — Python Foundations

### 1. Variables, Types & Memory Model
- **Mental Model:** In Python, variables are **name tags pointing to objects in memory**, not fixed boxes. Everything (even an `int` or function) is an object with a type and an identity (`id(x)`).
- **Dynamic vs Strong Typing:**
  - *Dynamic:* A variable name can be reassigned to a different type (`x = 5`, then `x = "hi"`).
  - *Strong:* Python refuses unsafe implicit mixing (`"5" + 2` raises `TypeError` instead of silently becoming `"52"` or `7`).
- **Core Primitives:** `int` (arbitrary precision—never overflows like C/Java), `float` (IEEE 754 binary floating-point), `str` (immutable Unicode text), `bool` (`True`/`False`, subclass of `int` where `True == 1`).
- **Production Edge Cases:**
  - `0.1 + 0.2 == 0.30000000000000004` due to binary float precision. Use `round(x, 2)` for display or `decimal.Decimal` for money.
  - `int("3.14")` and `int("abc")` raise `ValueError`. Always validate or wrap user/API inputs in `try/except`.
  - `is` checks **memory identity** (same object); `==` checks **value equality**. Use `is None` / `is not None`, never `== None` or `is 1000`.

---

### 2. Conditions, Truthiness & Loops
- **Truthiness:** Python evaluates values in `if x:` automatically.
  - **Falsy:** `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()`.
  - **Truthy:** Everything else (non-empty collections, non-zero numbers).
  - *Clean pattern:* Write `if items:` instead of `if len(items) > 0:`.
- **Short-Circuit Evaluation:**
  - In `a and b`, Python stops at `a` if `a` is falsy.
  - In `a or b`, Python returns `a` if `a` is truthy, else `b` (great for fallbacks: `name = raw_name or "Guest"`).
- **Loops (`for` vs `while`) & `else`:**
  - `for` iterates over any iterable; use `enumerate(items)` instead of manual `i = 0` counters.
  - `while` runs until a condition becomes `False` (ideal for event loops/retries; always guard against infinite loops).
- **Production Edge Cases:**
  - **Mutating while iterating:** Never `.remove()` from a list inside `for x in my_list:`—it shifts indices and skips elements. Build a filtered list instead.
  - **Off-by-one:** `range(1, 5)` produces `1, 2, 3, 4` (stop is exclusive).

---

### 3. Functions, `return`, Scope (LEGB) & Guard Clauses
- **LEGB Scope Rule:** Python resolves variable names in order:
  1. **L**ocal (inside current function)
  2. **E**nclosing (outer function in nested functions)
  3. **G**lobal (module level)
  4. **B**uilt-in (`len`, `print`, `sum`)
- **`return` vs `print`:** A function without `return` implicitly returns `None`. Always return values so functions can be composed (`f(g(x))`) and unit-tested.
- **Guard Clauses:** Handle invalid/edge cases at the top with early `return`s so the main logic stays flat instead of deeply nested `if` blocks.
- **Production Edge Cases:**
  - **Mutable Default Argument Trap:** Never write `def add_item(item, bag=[]):`! The default `[]` is created **once** when the function is defined and shared across all calls. Use `bag=None` and `if bag is None: bag = []`.
  - Avoid mutating `global` state inside functions; pass arguments in and `return` results.

---

### 4. Lists (`list`) & Memory References
- **Under the Hood:** A Python `list` is a **dynamic array of pointers** to objects.
  - Index access `arr[i]` is **`O(1)`** (instant).
  - `.append(x)` is **`O(1)`** amortized; `.insert(0, x)` or `.pop(0)` is **`O(n)`** because every item shifts.
  - `x in my_list` is **`O(n)`** (linear scan).
- **Slicing:** `arr[start:stop:step]` creates a **new shallow copy** (`arr[::-1]` reverses a list).
- **Production Edge Cases:**
  - **Aliasing vs Copying:** `b = a` only copies the reference—mutating `b` mutates `a`. Use `a.copy()` for a shallow copy, or `copy.deepcopy(a)` if `a` contains nested lists/dicts.
  - **`IndexError`:** Always check `if arr:` before accessing `arr[0]` or `arr[-1]`.

---

### 5. Exception Handling (`try / except / else / finally`)
- **Full Structure:**
  - `try:` risky code (keep this block as small as possible).
  - `except SpecificError as err:` handles expected failure cleanly.
  - `else:` runs **only if `try` succeeded** (keeps non-risky code out of `try`).
  - `finally:` **always runs** (cleanup: closing files, DB connections, locks).
- **Custom Exceptions:** Subclass `Exception` (e.g., `class InsufficientFundsError(Exception): pass`) for domain-specific business errors.
- **Production Edge Cases:**
  - **Never use bare `except:`** — it catches `KeyboardInterrupt` (`Ctrl+C`) and hides real bugs (`NameError`, `TypeError`). Catch specific exceptions (`ValueError`, `KeyError`, `OSError`).
  - Don't swallow errors silently (`except ValueError: pass`) without logging or a deliberate fallback.

---

### 6. Classes (OOP), Modules & File I/O
- **Classes:** Bundle **state** (`self.hp`, `self.name`) and **behavior** (methods) together. `__init__` runs automatically when an instance is created.
- **Modules:** Any `.py` file is a module. Use `if __name__ == "__main__":` so test/run code only executes when the file is run directly, not when imported by another file.
- **File I/O (`pathlib` + `with`):**
  - Always use `with open(...)` (or `Path.read_text()`/`write_text()`) so file handles close automatically even if an exception occurs.
  - Always specify `encoding="utf-8"` on Windows so special characters don't fail with `UnicodeDecodeError`.

---

## Phase 2 — Python Developer Foundations

### 7. Dictionaries (`dict`) & Hash Tables
- **Under the Hood:** Implemented as a **hash table** (`O(1)` average lookup, insert, delete). Preserves insertion order (Python 3.7+).
- **Hashability:** Keys must be **immutable & hashable** (`str`, `int`, `tuple` of immutables, `frozenset`). Lists and dicts cannot be keys (`TypeError: unhashable type`).
- **Senior Patterns:**
  - Safe read: `d.get(key, default)` avoids `KeyError`.
  - Initialize-if-missing: `d.setdefault(key, []).append(val)` (or `collections.defaultdict`).
  - Order-preserving deduplication of a list: `list(dict.fromkeys(items))`.
  - Merge two dicts cleanly: `merged = defaults | overrides` (Python 3.9+).
- **Production Edge Cases:**
  - `d[key]` crashes with `KeyError` when missing; use `.get()` for optional keys.
  - Mutating a dict (adding/deleting keys) while iterating over `d.items()` raises `RuntimeError: dictionary changed size during iteration`. Iterate over `list(d.items())` if you must mutate.

---

### 8. Sets (`set` & `frozenset`)
- **Under the Hood:** Backed by a hash table (keys only, no values). Membership check `x in my_set` is **`O(1)`**—hundreds/thousands of times faster than `x in my_list` (`O(n)`) on large data.
- **Set Algebra:**
  - Union (`a | b`): in `a` or `b`
  - Intersection (`a & b`): in both `a` and `b`
  - Difference (`a - b`): in `a`, not in `b`
  - Symmetric Difference (`a ^ b`): in `a` or `b`, not both
  - Subset / Superset (`a <= b`, `a >= b`): permission & requirement checks
- **`frozenset`:** Immutable set—can be stored inside another `set` or used as a `dict` key.
- **Production Edge Cases:**
  - **`{}` is an empty `dict`, NOT an empty `set`!** Always use `set()`.
  - **`remove()` vs `discard()`:** `.remove(x)` raises `KeyError` if `x` is missing; `.discard(x)` is a safe no-op.
  - Sets are unordered and cannot be indexed (`s[0]` raises `TypeError`).

---

### 9. Tuples (`tuple`) & String Manipulation (`str`)
- **Tuples (`tuple`):**
  - Immutable sequences, lighter in memory than lists, and hashable (if all elements are hashable).
  - **Star Unpacking:** `name, rank, *scores = record` captures remaining items into a list.
  - **1-Line Swap:** `a, b = b, a` uses tuple packing/unpacking under the hood.
  - **Edge Cases:**
    - 1-item tuple requires a trailing comma: `("ZACK",)` is a `tuple`; `("ZACK")` is a `str`.
    - **Mutable-inside-immutable trap:** `t = ("ok", [1, 2])` — you can't reassign `t[1]`, but `t[1].append(3)` mutates the inner list!
- **Strings (`str`):**
  - Immutable Unicode sequences. Methods like `.strip()`, `.lower()`, `.replace()` return **new** strings.
  - **Performance:** Building large strings with `+=` inside a loop is `O(n²)` (copies the string every step). Collect pieces in a list and use `"".join(parts)` (`O(n)`).
  - **Senior Patterns:**
    - `header.partition(": ")` always returns a 3-tuple `(before, sep, after)` safely.
    - `filename.endswith((".csv", ".json"))` accepts a tuple of suffixes.
    - F-string specifiers: `f"{pi:.2f}"`, `f"{xp:,}"`, `f"{name:>8}"`.
  - **Edge Case:** `"".split()` returns `[]`, whereas `"".split(",")` returns `[""]`!

---

## Engineering & GitHub

### 10. Git Internals & Clean History
- **Core Model:** Git stores snapshots (commits) in a directed graph. Branches (`main`) are just movable pointers to a commit hash.
- **Safe History Hygiene:**
  - Always commit with descriptive messages (`day-XX: <topic>` or `phase-X-project: <milestone>`).
  - Git tracks **files**, not empty folders.
  - When rewriting history on a personal branch, verify with `git diff <old_sha> HEAD` (empty = zero code lost) and push with `--force-with-lease` (safer than `--force`).
