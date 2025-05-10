### 🐍 Python Virtual Environment – Explained

A **virtual environment** in Python is an isolated workspace that allows you to manage dependencies for a project **independently** of other projects or the system-wide Python installation.

---

## ✅ Why Use a Virtual Environment?

* Avoid version conflicts between projects.
* Keep dependencies organized and separated.
* Prevent polluting the global Python installation.

---

## 📦 How to Create and Use a Virtual Environment

### 1. **Install `virtualenv` (if not using `venv`)**

```bash
pip install virtualenv
```

> Python 3.3+ comes with `venv` by default.

---

### 2. **Create a Virtual Environment**

**Using `venv`** (recommended):

```bash
python3 -m venv myenv
```

**Using `virtualenv`:**

```bash
virtualenv myenv
```

---

### 3. **Activate the Virtual Environment**

* **Linux/macOS:**

  ```bash
  source myenv/bin/activate
  ```

* **Windows (cmd):**

  ```cmd
  myenv\Scripts\activate
  ```

* **Windows (PowerShell):**

  ```powershell
  .\myenv\Scripts\Activate.ps1
  ```

> After activation, you'll see the environment name in the terminal prompt like this:
> `(myenv) user@pc:~$`

---

### 4. **Deactivate the Environment**

```bash
deactivate
```

---

### 5. **Install Packages in the Environment**

```bash
pip install requests
```

---

### 6. **Save Dependencies to a File**

```bash
pip freeze > requirements.txt
```

### 7. **Install from a Requirements File**

```bash
pip install -r requirements.txt
```

---

### 🌲 `tree` Command in Linux

The `tree` command displays **directory structures** in a hierarchical tree-like format.

---

## ✅ Basic Syntax:

```bash
tree [directory]
```

---

## 📂 Example:

```bash
tree
```

**Output:**

```
.
├── file1.txt
├── dir1
│   ├── file2.txt
│   └── file3.txt
└── dir2
    └── file4.txt
```

---

## 🔧 Common Options:

| Command                | Description                              |
| ---------------------- | ---------------------------------------- |
| `tree -L 1`            | Limit the depth of the tree (level 1)    |
| `tree -a`              | Show hidden files too                    |
| `tree -d`              | Show only directories                    |
| `tree -f`              | Show full path of files                  |
| `tree -h`              | Show file sizes in human-readable format |
| `tree > structure.txt` | Save output to a file                    |

---

## 🛠️ Install `tree` (if not available):

### Ubuntu/Debian:

```bash
sudo apt install tree
```

### CentOS/RHEL:

```bash
sudo yum install tree
```

### Arch:

```bash
sudo pacman -S tree
```

---


