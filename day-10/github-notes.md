# Day 10: GitHub & Git History Cleanup Notes

## 1. Inspecting the repo and history
- `git status` — Checked the current branch (`main`), whether it was synced with `origin/main`, and whether there were uncommitted changes.
- `git log --oneline --graph` — Displayed a compact commit history tree so we could spot the redundant merge commit, empty commit message, `"update"` commit, and repeated `"day-10: dictionaries"` commits.
- `git diff --stat ab8db5f 1b7ea96` — Verified that the merge commit `1b7ea96` and `ab8db5f` had the exact same file state before removing the merge.

## 2. Building a clean history on a temporary branch
Working on a temporary branch keeps `main` safe until everything is verified:

- `git checkout -b clean-main ab8db5f` — Created and switched to a new branch `clean-main` starting at `ab8db5f` (`day-03`), leaving out the messy merge (`1b7ea96`) and empty-message commit (`9205709`).
- `git cherry-pick d7b381d 7fb1c85 59d1c41` — Replayed the `day-04`, `day-05-day-06`, and `day-07` commits onto `clean-main` with their original dates and messages.
- `git cherry-pick -n c29d0c2 9d3cfa5` — Applied both `day-08` and `"update"` into the staging area without committing (`-n` / `--no-commit`) so they could be combined into one commit.
- `git commit --author="..." -m "..."` — Committed the staged changes with a clean message (and used `$env:GIT_AUTHOR_DATE` / `$env:GIT_COMMITTER_DATE` in PowerShell to preserve the original commit timestamps).
- `git checkout 29c704e -- day-09` (and then `-- day-10`) — Pulled the exact final `day-09/` and `day-10/` folder contents from the old tip commit (`29c704e`) so they could be committed separately by day.

## 3. Verifying no code was lost
- `git diff 29c704e HEAD` — Compared the old tip commit (`29c704e`) against our new `clean-main` tip. Empty output means 100% of your files are identical.

## 4. Updating `main` and pushing to GitHub
- `git checkout main` — Switched back to `main`.
- `git reset --hard clean-main` — Moved `main` to point to the new clean history.
- `git branch -d clean-main` — Deleted the temporary branch.
- `git push --force-with-lease origin main` — Updated GitHub with the rewritten history. `--force-with-lease` is a safer version of `--force` that refuses to overwrite the remote if someone else pushed new commits in the meantime.
