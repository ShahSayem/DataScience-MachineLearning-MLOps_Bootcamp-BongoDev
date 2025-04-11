# Basic Git Commands

## Setup Git (first time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Initialize a Git Repository
```bash
git init
# This creates a new .git directory to track changes in the project.
```

## Check Git Status
```bash
git status
# To check the current status of your files (staged, modified, or untracked).
```

## Add Files to Staging Area
```bash
git add filename        # To add a single file
git add .               # To add all modified files
```

## Commit Changes
```bash
git commit -m "Commit message describing the change"
```

## View Commit History
```bash
git log
# This shows the list of commits made with details.
```

## Create a New Branch
```bash
git branch new-branch-name
```

## Switch Between Branches
```bash
git checkout branch-name
git checkout -b new-branch-name   # Create and switch to a new branch
```

## Merge Branches
```bash
git merge branch-name    # Merge changes into the current branch
```

## Push Changes to Remote Repository
```bash
git push origin branch-name
```

## Pull Changes from Remote Repository
```bash
git pull origin branch-name
```

## Clone a Repository
```bash
git clone https://github.com/user/repository.git
```

## Remove Files
```bash
git rm --cached filename    # Unstage but keep locally
git rm filename             # Remove from staging and local
```

## Create and Manage Remote Repositories
```bash
git remote add origin https://github.com/user/repository.git
git remote -v               # List remotes
```
