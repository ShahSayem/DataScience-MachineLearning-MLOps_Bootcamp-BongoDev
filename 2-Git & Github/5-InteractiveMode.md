
# ✍️ Git Interactive Mode – Editing with Vim

When using commands like `git commit --amend`, `git rebase -i`, or `git merge`, Git often opens your **default text editor**, which is usually **Vim** on Unix systems.

Here are some basic Vim commands to navigate interactive mode effectively:

---

## 📝 Enter Insert Mode

- Press `i`  
  👉 This switches Vim from **command mode** to **insert mode**, allowing you to type or edit text.

---

## 💾 Save and Exit

- Press `Esc` to exit insert mode
- Type `:wq`  
  👉 This means:
  - `:w` – write/save
  - `:q` – quit  
  Then press `Enter` to confirm

---

## ❌ Exit Without Saving

- Press `Esc`
- Type `:q!` and press `Enter`

---

## 🔁 Common Use Case in Git

During `git commit --amend`, Git might open Vim to edit the previous commit message:

1. Press `i` to insert/edit your message
2. After editing, press `Esc`
3. Type `:wq` and hit `Enter` to save and finish the amend

---

## 🧠 Tips

- Don’t panic if you can’t type — you’re probably not in **insert mode** (`i`)
- Always hit `Esc` to leave insert mode before issuing commands like `:wq`

---

Vim can feel intimidating at first, but these few commands are all you need to handle basic Git operations.

