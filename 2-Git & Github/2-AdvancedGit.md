
# 🧠 Advanced Git Commands

This guide covers essential advanced Git commands for efficient version control and collaboration.

---

## 🔄 `git restore`

Restore files in your working directory.

- **Discard changes in working directory:**
  ```bash
  git restore filename
  ```

- **Unstage a file:**
  ```bash
  git restore --staged filename
  ```

- **Restore both staged and working directory:**
  ```bash
  git restore --source=HEAD --staged --worktree filename
  ```

---

## ✏️ `git commit --amend`

Modify the most recent commit.

- **Edit the last commit message:**
  ```bash
  git commit --amend
  ```

- **Add a file to the last commit (without changing the message):**
  ```bash
  git add forgotten_file
  git commit --amend --no-edit
  ```

---

## 📜 `git log --oneline`

Display a compact, one-line summary of each commit.

```bash
git log --oneline
```

---

## 🔄 `git checkout`

Switch to a specific commit or branch.

- **Checkout a specific commit:**
  ```bash
  git checkout <commit-hash>
  ```

- **Return to a branch:**
  ```bash
  git checkout main
  ```

---

## 🔀 `git switch`

Modern alternative to `checkout` for branches.

- **Switch to an existing branch:**
  ```bash
  git switch branch-name
  ```

- **Create and switch to a new branch:**
  ```bash
  git switch -c new-branch-name
  ```

---

## 🌳 `git log --all --graph --oneline --decorate`

View all commits in a decorated graph format.

```bash
git log --all --graph --oneline --decorate
```

---

## 🔁 `git revert`

Safely undo changes by creating a new commit that reverses a specific commit.

```bash
git revert <commit-hash>
```

---

## 💣 `git reset`

Reset commits or unstage files.

- **Soft reset (keep changes):**
  ```bash
  git reset --soft <commit-hash>
  ```

- **Mixed reset (default, unstages changes):**
  ```bash
  git reset <commit-hash>
  ```

- **Hard reset (discard all changes):**
  ```bash
  git reset --hard <commit-hash>
  ```

---

## 🍒 `git cherry-pick`

Apply changes from specific commits to your current branch.

- **Single commit:**
  ```bash
  git cherry-pick <commit-hash>
  ```

- **Range of commits:**
  ```bash
  git cherry-pick <start>^..<end>
  ```

- **If conflicts arise:**
  ```bash
  git cherry-pick --continue
  ```

- **Abort cherry-pick:**
  ```bash
  git cherry-pick --abort
  ```

---

## 🧳 `git stash`

Temporarily save changes that you’re not ready to commit.

- **Stash current changes:**
  ```bash
  git stash
  ```

- **Stash with message:**
  ```bash
  git stash save "WIP: description"
  ```

- **Apply latest stash:**
  ```bash
  git stash apply
  ```

- **Apply and remove latest stash:**
  ```bash
  git stash pop
  ```

- **List all stashes:**
  ```bash
  git stash list
  ```

- **Drop a specific stash:**
  ```bash
  git stash drop stash@{0}
  ```

- **Clear all stashes:**
  ```bash
  git stash clear
  ```

---
