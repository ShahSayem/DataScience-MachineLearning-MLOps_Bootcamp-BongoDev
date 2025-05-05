# 🧹 Using `black` and `flake8` for Python Code Quality

Improve code readability and maintainability with two essential tools:

---

## ✅ What They Do

| Tool     | Purpose        | Key Feature                               |
| -------- | -------------- | ----------------------------------------- |
| `black`  | Code formatter | Auto-formats code to a standard style     |
| `flake8` | Linter         | Checks for syntax issues, styling, errors |

---

## 🔧 Installation

Install both tools with pip:

```bash
pip install black flake8
```

Or for local use:

```bash
pip install black flake8 --user
```

---

## 🧪 Usage

### ▶️ Format Code with Black

```bash
black your_script.py
```

Format all files in a directory:

```bash
black .
```

### 🧪 Lint Code with Flake8

```bash
flake8 your_script.py
```

Check all Python files recursively:

```bash
flake8 .
```

---

## ⚙️ Configuration Files

### `.flake8`

```ini
[flake8]
max-line-length = 88
exclude =
    .git,
    __pycache__,
    env,
    venv
```

### `pyproject.toml` (for Black)

```toml
[tool.black]
line-length = 88
skip-string-normalization = false
```

---

## 🔄 Combine Both in One Command

```bash
black . && flake8 .
```

---

## 🪝 Pre-commit Hook Example

Automate formatting and linting before each commit:

**`.git/hooks/pre-commit`**

```bash
#!/bin/bash

FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')

for file in $FILES; do
  echo "Formatting $file with black..."
  black "$file"

  echo "Linting $file with flake8..."
  flake8 "$file"

  git add "$file"
done
```

> Remember to give execution permission and use LF endings:
>
> ```bash
> chmod +x .git/hooks/pre-commit
> dos2unix .git/hooks/pre-commit
> ```

---

Keep your codebase clean, consistent, and error-free!
