# Personal Knowledge Cheatsheet

A simple, easy-to-read guide of everything I’ve learned — including **how it works**, **code examples**, and **engineering edge cases** so I don't fall into common traps.

---

## Phase 1 — Python Foundations

### 1. Variables & Data Types
**In simple words:** Variables are labeled boxes that hold data. Python has 4 main basic types:
- `int` → whole numbers (`10`, `-3`)
- `float` → decimal numbers (`3.14`, `0.5`)
- `str` → text inside quotes (`"hello"`)
- `bool` → `True` or `False`

```python
age = int("25")       # "25" (text) -> 25 (number)
price = float("9.99") # "9.99" -> 9.99
text = str(100)       # 100 -> "100"
```

> **Engineering Edge Cases:**
> - `int("abc")` or `int("3.14")` will crash with a `ValueError`! Always validate or wrap user input in `try/except`.
> - `input()` **always** returns a `str`, even if the user types `5`. You must convert it before doing math.

---

### 2. Conditions & Loops
**In simple words:** Conditions let your code make decisions (`if/elif/else`). Loops repeat work (`for` when you know the items, `while` when you loop until something changes).

```python
for i in range(3):      # Runs 0, 1, 2
    print(i)

count = 0
while count < 3:
    count += 1          # Update condition so it stops!
```

> **Engineering Edge Cases:**
> - **Infinite loop:** In a `while` loop, if you forget to update the variable (`count += 1`), it runs forever.
> - **Modifying a list while looping over it:** Removing items from a list inside `for item in my_list:` skips elements. Loop over a copy (`my_list[:]`) or build a new list instead.
> - `=` assigns a value; `==` compares two values. Mixing them up causes bugs.

---

### 3. Functions, `return` & Variable Scope
**In simple words:** A function is a reusable mini-machine.
- `return` hands the result back to your code so you can store or reuse it.
- `print()` only shows text on the screen and gives back `None`.
- **Scope:** Variables created inside a function stay inside it (local).

```python
def add(a, b):
    return a + b

total = add(2, 3)  # total is 5
```

> **Engineering Edge Cases:**
> - If a function has no `return` (or forgets `return` in one `if` branch), it returns `None` by default—which later crashes if you try `total + 1`.
> - Avoid modifying `global` variables inside functions; pass inputs as parameters and `return` the new value instead (much easier to test and debug).

---

### 4. Lists (`list`)
**In simple words:** An ordered collection that keeps items in sequence and allows duplicates.

```python
tasks = ["code", "test", "push"]
tasks.append("sleep")   # Add to end
first = tasks[0]        # "code"
last = tasks[-1]        # "sleep"
```

> **Engineering Edge Cases:**
> - **IndexError:** Accessing `tasks[10]` or `tasks[0]` on an empty list `[]` crashes. Check `if tasks:` before indexing.
> - **Shallow copy trap:** `b = a` does **not** copy a list—both point to the same list! Changing `b` changes `a`. Use `b = a.copy()` when you need an independent copy.

---

### 5. Exception Handling (`try / except`)
**In simple words:** A safety net so bad input or unexpected errors don't crash your whole program.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That wasn't a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

> **Engineering Edge Cases:**
> - **Never use bare `except:`** — it hides real bugs (even typos or `Ctrl+C`). Always catch the specific error (`ValueError`, `KeyError`, `ZeroDivisionError`, `FileNotFoundError`).
> - Keep the `try` block as small as possible so you know *which* line actually failed.

---

## Phase 2 — Python Developer Foundations

### 6. Dictionaries (`dict`)
**In simple words:** Stores data as `key: value` pairs (like a real-world phonebook or JSON object). Super fast lookup by key.

```python
player = {"name": "Zack", "level": 4}

# Safe lookup
role = player.get("role", "Developer")  # Returns "Developer" if missing

# Loop over key and value
for key, value in player.items():
    print(key, "->", value)
```

> **Engineering Edge Cases:**
> - `player["role"]` crashes with `KeyError` if `"role"` doesn't exist. Use `player.get("role")` or `player.get("role", default)` when a key might be missing.
> - Dictionary keys must be **immutable** (strings, numbers, tuples)—you cannot use a `list` as a dictionary key.
> - Assigning `player["level"] = 5` overwrites the old value silently if `"level"` already exists.

---

### 7. Sets (`set`)
**In simple words:** An **unordered** bag of **unique** items. It automatically removes duplicates and makes checking `if x in my_set:` instant.

```python
py_students = {"Ali", "Abu", "Sara", "Zack"}
js_students = {"Sara", "Zack", "Mika", "John"}

py_students.add("Adam")
py_students.discard("Bob")              # Safe remove (no crash if missing)

both = py_students & js_students        # Intersection: {"Sara", "Zack"}
either = py_students | js_students      # Union: all unique students
py_only = py_students - js_students     # Difference: in Python, not JS
```

> **Engineering Edge Cases:**
> - **`remove()` vs `discard()`:** `s.remove("Bob")` crashes with `KeyError` if `"Bob"` isn't there. Use `s.discard("Bob")` when you aren't 100% sure it exists.
> - **Empty set trap:** `{}` creates an empty **dictionary**, NOT an empty set! Always use `set()` for an empty set.
> - **No indexing:** Sets are unordered, so `my_set[0]` crashes with `TypeError`. Convert to `list(my_set)` first if you need order or indexing.

---

## Engineering & GitHub

### 8. Daily Git Workflow
**In simple words:** Git saves snapshots ("commits") of your code locally; GitHub stores them online as your backup and portfolio.

```powershell
git status                          # Check what changed
git add .                           # Stage changes
git commit -m "day-11: sets"        # Save a snapshot with a clear message
git push origin main                # Upload to GitHub
```

> **Engineering Edge Cases:**
> - **Empty folders:** Git only tracks files, not empty folders. Put at least one file inside `day-XX/` before committing.
> - **Never force-push (`--force`) blindly:** If you ever rewrite history, use `--force-with-lease` so you don't accidentally overwrite someone else's commits.
> - **Clean commits:** Always commit with `day-XX: <topic>` instead of vague `"update"` messages so your GitHub history reads like a real engineering log.
