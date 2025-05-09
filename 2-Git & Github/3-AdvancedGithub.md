# 🧠 Git Basics & Advanced Concepts

---

## ✅ 3 Stages of Git

Git tracks changes in three key stages:

1. **Working Directory**

   * Where you edit files
   * Changes are not yet tracked

2. **Staging Area (Index)**

   * Temporary area where changes are added before committing
   * Use: `git add <file>`

3. **Repository (Local Git Directory)**

   * Permanent history of your commits
   * Use: `git commit -m "message"`

---

## 🔄 Common Git Commands

### 🚀 `git push`

Sends local commits to a remote repository (like GitHub).

```bash
git push origin main
```

### 📥 `git pull`

Fetches and merges remote changes into your current branch.

```bash
git pull origin main
```

### 📂 `git clone`

Copies an entire remote repository to your local machine.

```bash
git clone https://github.com/username/repo.git
```

### 🍴 Fork

* A **GitHub**-only feature
* Creates a copy of someone else's repository under your account
* You can push changes and submit a **Pull Request (PR)** to the original repo

---

## 🔐 Connecting Local Repo to Remote (Authentication)

### 1. SSH (Secure Shell)

* Authenticates using SSH key pairs
* Steps:

  ```bash
  ssh-keygen -t ed25519 -C "your_email@example.com"
  # Add the key to your GitHub SSH settings
  ```
* Remote URL looks like:

  ```
  git@github.com:username/repo.git
  ```

### 2. PAT (Personal Access Token)

* Used when HTTPS is preferred
* Replace your GitHub password with a token
* Remote URL:

  ```
  https://github.com/username/repo.git
  ```
* When prompted for password, use the token instead

---

## 🪝 Git Hooks

Git hooks are scripts that run automatically at specific points in the Git workflow.

### 🔧 Location:

```
.git/hooks/
```

### 🧪 Common Client-Side Hooks:

| Hook Name     | When It Runs             | Example Use            |
| ------------- | ------------------------ | ---------------------- |
| `pre-commit`  | Before commit is saved   | Run linters or tests   |
| `commit-msg`  | After message is written | Enforce message format |
| `post-commit` | After commit is complete | Notify or log          |

### 🌐 Server-Side Hooks:

Used in Git servers for CI/CD pipelines (e.g., `pre-receive`, `post-receive`)

### 💡 Example Pre-Commit Hook:

```bash
#!/bin/bash

FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')
for file in $FILES; do
  black "$file"
  git add "$file"
done
```

> Make sure the script has LF line endings and is executable (`chmod +x`).

---

## 📌 Summary

* Git has 3 core stages: working directory, staging area, and repo
* Use SSH or PAT to connect to GitHub securely
* Git hooks automate pre/post commit tasks
* Understand push/pull/clone/fork to collaborate effectively

---

## **Detailed explanation of the difference between `git fetch` and `git pull`**:


## 🔄 `git fetch` vs `git pull`

Both `git fetch` and `git pull` are used to **update your local repository** with changes from a remote repository, but they behave differently.

---

### 🧲 `git fetch`

* **What it does:**
  Downloads commits, files, and references from a remote repository **but does NOT merge them** into your current branch.

* **Usage:**

  ```bash
  git fetch origin
  ```

* **What happens next:**
  You manually review and merge the changes using commands like:

  ```bash
  git merge origin/main
  ```

* **Use case:**

  * When you want to **review changes first** before integrating.
  * Safer in production environments.

* **Analogy:**
  It's like checking the mailbox but not opening the letters yet.

---

### ⚡ `git pull`

* **What it does:**
  Combines `git fetch` **and** `git merge` in one step.
  It **downloads changes** from the remote and **merges** them into your current branch immediately.

* **Usage:**

  ```bash
  git pull origin main
  ```

* **Use case:**

  * When you are ready to immediately integrate remote changes.
  * Quicker for personal projects or non-critical branches.

* **Analogy:**
  It’s like checking the mailbox and opening all letters immediately.

---

### 🔍 Summary Table

| Command     | Fetches Remote Changes | Merges Automatically | Safe for Reviewing | Common in Scripts |
| ----------- | ---------------------- | -------------------- | ------------------ | ----------------- |
| `git fetch` | ✅ Yes                  | ❌ No                 | ✅ Yes              | ✅ Yes             |
| `git pull`  | ✅ Yes                  | ✅ Yes                | ❌ No               | ⚠️ With Caution   |

---

### ✅ Which Should You Use?

* Use `git fetch` when:

  * You want to check what’s changed before merging.
  * You work in a team and need more control over updates.

* Use `git pull` when:

  * You want fast updates and trust the remote branch.
  * You're working on a personal project or prototype.

---
