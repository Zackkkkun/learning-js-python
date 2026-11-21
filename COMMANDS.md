# THE SYSTEM — Command Reference

Quick cheatsheet for interacting with **THE SYSTEM** and managing your daily GitHub progress.

---

## 1. Chat Commands (For THE SYSTEM)

| Command / Phrase | Mode | What It Does |
| :--- | :--- | :--- |
| `"start"` / `"next topic"` | **Topic Quest** | Starts the next topic right away (multiple topics/day allowed!), logs start time, and creates `day-XX/<topic>.py`. |
| `"check my code"` / `"review day-11/sets.py"` | **Quest Evaluation** | Runs your `.py` file, checks edge cases, gives feedback via the 3-Step Hint Ladder, and logs gotchas. |
| `"give me a hint"` | **Hint Ladder** | Gives the next hint level (1: concept nudge → 2: line/edge case → 3: pseudocode) without spoiling the answer. |
| `"quiz me"` / `"quick review"` | **Arena Trial** | 3 rapid-fire questions (predict output, spot the bug, architect's choice) for `+40 XP` (`+20 XP` perfect score). |
| `"start phase project"` | **Phase Boss Raid** | Starts the current phase's capstone project in `projects/<slug>/` with milestones (`+500 XP` + Rank Up on clear). |
| `"finish topic"` / `"finish today"` | **Save & Sync** | Logs time spent, updates `README.md`, `CHEATSHEET.md`, and `review-queue.md`, commits, and pushes to GitHub. |

---

## 2. Terminal Commands (Python & Git)

### Run Your Code
```powershell
python day-11/sets.py
```

### Daily Git Workflow (Manual)
```powershell
git status                                  # Check modified/untracked files
git add .                                   # Stage all changes
git commit -m "day-11: sets and operations" # Commit with clean message
git push origin main                        # Push to GitHub
```

### Inspect History
```powershell
git log --oneline --graph                   # View compact commit tree
git diff                                    # See unstaged changes
```
