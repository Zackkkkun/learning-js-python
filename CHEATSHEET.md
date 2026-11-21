# Personal Knowledge Cheatsheet

A simple, easy-to-read guide of everything I’ve learned — with **topics**, **explanations**, **examples**, and **engineering edge cases** nested by indent level.

---

## Phase 1 — Python Foundations

1. **Variables & Data Types**
   - **In simple words:** Variables are labeled boxes that hold data.
     - `int` → whole numbers (`10`, `-3`)
     - `float` → decimal numbers (`3.14`, `0.5`)
     - `str` → text inside quotes (`"hello"`)
     - `bool` → `True` or `False`
   - **Example:**
     ```python
     age = int("25")       # "25" (text) -> 25 (number)
     price = float("9.99") # "9.99" -> 9.99
     text = str(100)       # 100 -> "100"
     ```
   - **Engineering Edge Cases:**
     - `int("abc")` or `int("3.14")` crashes with a `ValueError`. Always validate or wrap user input in `try/except`.
     - `input()` **always** returns a `str`, even if the user types `5`. Convert it before doing math.

2. **Conditions & Loops**
   - **In simple words:**
     - Conditions (`if / elif / else`) let your code make decisions.
     - `for` loops repeat over a known sequence (`list`, `dict`, `set`, `range`).
     - `while` loops repeat until a condition becomes `False`.
   - **Example:**
     ```python
     for i in range(3):      # Runs 0, 1, 2
         print(i)

     count = 0
     while count < 3:
         count += 1          # Update condition so it stops!
     ```
   - **Engineering Edge Cases:**
     - **Infinite loop:** In a `while` loop, forgetting to update the variable (`count += 1`) makes it run forever.
     - **Mutating a list while looping:** Removing items inside `for item in my_list:` skips elements. Loop over a copy (`my_list[:]`) or build a new list instead.
     - `=` assigns a value; `==` compares two values.

3. **Functions, `return` & Variable Scope**
   - **In simple words:** A function is a reusable mini-machine.
     - `return` sends a result back to your code so you can store or reuse it.
     - `print()` only shows text on the screen and gives back `None`.
     - **Scope:** Variables created inside a function stay inside it (local).
   - **Example:**
     ```python
     def add(a, b):
         return a + b

     total = add(2, 3)  # total is 5
     ```
   - **Engineering Edge Cases:**
     - If a function has no `return` (or misses `return` in one `if` branch), it returns `None`—which crashes later if you do `total + 1`.
     - Avoid modifying `global` variables inside functions; pass inputs as parameters and `return` the new value instead.

4. **Lists (`list`)**
   - **In simple words:** An ordered collection that keeps items in sequence and allows duplicates.
   - **Example:**
     ```python
     tasks = ["code", "test", "push"]
     tasks.append("sleep")   # Add to end
     first = tasks[0]        # "code"
     last = tasks[-1]        # "sleep"
     ```
   - **Engineering Edge Cases:**
     - **`IndexError`:** Accessing `tasks[10]` or `tasks[0]` on an empty list `[]` crashes. Check `if tasks:` before indexing.
     - **Shallow copy trap:** `b = a` does **not** copy a list—both point to the same list. Use `b = a.copy()` when you want an independent copy.

5. **Exception Handling (`try / except`)**
   - **In simple words:** A safety net so bad input or unexpected errors don't crash your whole program.
   - **Example:**
     ```python
     try:
         num = int(input("Enter a number: "))
         result = 10 / num
     except ValueError:
         print("That wasn't a number!")
     except ZeroDivisionError:
         print("Cannot divide by zero!")
     ```
   - **Engineering Edge Cases:**
     - **Never use bare `except:`** — it hides real bugs (typos, `Ctrl+C`, etc.). Always catch the specific error (`ValueError`, `KeyError`, `ZeroDivisionError`).
     - Keep the `try` block as small as possible so you know *which* line failed.

---

## Phase 2 — Python Developer Foundations

6. **Dictionaries (`dict`)**
   - **In simple words:** Stores data as `key: value` pairs (like a phonebook or JSON object) for fast lookup by key.
   - **Example:**
     ```python
     player = {"name": "Zack", "level": 4}

     # Safe lookup
     role = player.get("role", "Developer")  # Returns "Developer" if missing

     # Loop over key and value
     for key, value in player.items():
         print(key, "->", value)
     ```
   - **Engineering Edge Cases:**
     - `player["role"]` crashes with `KeyError` if `"role"` is missing. Use `player.get("role", default)` when a key might not exist.
     - Dictionary keys must be **immutable** (`str`, `int`, `tuple`)—you cannot use a `list` as a key.
     - Assigning `player["level"] = 5` overwrites the old value silently if `"level"` already exists.

7. **Sets (`set`)**
   - **In simple words:** An **unordered** bag of **unique** items. It removes duplicates automatically and makes `if x in my_set:` instant.
   - **Example:**
     ```python
     py_students = {"Ali", "Abu", "Sara", "Zack"}
     js_students = {"Sara", "Zack", "Mika", "John"}

     py_students.add("Adam")
     py_students.discard("Bob")              # Safe remove (no crash if missing)

     both = py_students & js_students        # Intersection: {"Sara", "Zack"}
     either = py_students | js_students      # Union: all unique students
     py_only = py_students - js_students     # Difference: in Python, not JS
     ```
   - **Engineering Edge Cases:**
     - **`remove()` vs `discard()`:** `s.remove("Bob")` crashes with `KeyError` if `"Bob"` is missing. Use `s.discard("Bob")` when you aren't 100% sure it exists.
     - **Empty set trap:** `{}` creates an empty **dictionary**, NOT an empty set. Always use `set()`.
     - **No indexing:** Sets are unordered, so `my_set[0]` crashes with `TypeError`. Convert with `list(my_set)` if you need order.

---

## Engineering & GitHub

8. **Daily Git Workflow**
   - **In simple words:** Git saves snapshots ("commits") of your code locally; GitHub stores them online as your backup and portfolio.
   - **Example:**
     ```powershell
     git status                          # Check what changed
     git add .                           # Stage changes
     git commit -m "day-11: sets"        # Save a snapshot with a clear message
     git push origin main                # Upload to GitHub
     ```
   - **Engineering Edge Cases:**
     - **Empty folders:** Git only tracks files, not empty folders. Put at least one file inside `day-XX/` before committing.
     - **Never force-push (`--force`) blindly:** If you rewrite history, use `--force-with-lease` so you don't overwrite someone else's commits.
     - **Clean commits:** Always use `day-XX: <topic>` instead of vague `"update"` messages so your GitHub history reads like a real engineering log.
