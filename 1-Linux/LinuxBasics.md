# 🐧 Basic Linux Commands Cheat Sheet

Here’s a quick reference for commonly used Linux commands for beginners and developers.

---

## 📁 File and Directory Management

| Command                    | Description                                                          |                                             |
| -------------------------- | -------------------------------------------------------------------- | ------------------------------------------- |
| `ls`                       | Lists files and directories in the current directory                 |                                             |
| `ls -a`                    | Lists all files including hidden ones                                |                                             |
| `ls -l`                    | Lists files with details like permissions, ownership, size, and date |                                             |
| `ls -la`                   | Lists all files (including hidden) with permissions                  |                                             |
| `cd <dir>`                 | Changes the current directory to `<dir>`                             |                                             |
| `cd ..`                    | Moves one directory level up                                         |                                             |
| `cd /`                     | Navigates to the root directory                                      |                                             |
| `pwd`                      | Displays the current directory path                                  |                                             |
| `mkdir <dir>`              | Creates a new directory named `<dir>`                                |                                             |
| `mkdir folder{1..5}`       | Creates multiple directories folder1 to folder5                      |                                             |
| `rmdir <dir>`              | Removes an empty directory                                           |                                             |
| `rm <file>`                | Deletes a file                                                       |                                             |
| `rm -r <dir>`              | Deletes a directory and its contents recursively                     |                                             |
| `rm -r folder*`            | Deletes all directories beginning with 'folder'                      |                                             |
| `touch <file>`             | Creates a new empty file                                             |                                             |
| `touch file{1..5}.txt`     | Creates multiple files file1.txt to file5.txt                        |                                             |
| `cp <src> <dest>`          | Copies a file or directory                                           |                                             |
| `mv <src> <dest>`          | Moves or renames a file or directory                                 |                                             |
| `find <path> -name <file>` | Searches for files by name under a path                              |                                             |
| \`seq 1 10 \| grep -vE '(3 \| 4)' \| xargs -I{} mkdir "folder{}"\`                                 | Creates folders from 1 to 10 except 3 and 4 |

---

## 📄 Viewing and Editing Files

| Command                     | Description                                 |
| --------------------------- | ------------------------------------------- |
| `cat <file>`                | Displays the content of a file              |
| `less <file>`               | Views file one page at a time               |
| `head <file>`               | Shows the first 10 lines                    |
| `head -n 2 <file>`          | Shows the first 2 lines                     |
| `tail <file>`               | Shows the last 10 lines                     |
| `tail -3 <file>`            | Shows the last 3 lines                      |
| `nano <file>`               | Opens file in Nano editor (easy CLI editor) |
| `vi <file>` or `vim <file>` | Opens file in Vi/Vim editor                 |

---

## 🛠️ Package Management

**For Debian/Ubuntu (APT):**

| Command                      | Description                 |
| ---------------------------- | --------------------------- |
| `sudo apt update`            | Updates package index       |
| `sudo apt upgrade`           | Upgrades installed packages |
| `sudo apt install <package>` | Installs a package          |
| `sudo apt remove <package>`  | Removes a package           |

---

## 👤 User Management

| Command          | Description                       |
| ---------------- | --------------------------------- |
| `whoami`         | Shows current logged-in user      |
| `adduser <name>` | Adds a new user                   |
| `passwd <name>`  | Sets password for user            |
| `su <user>`      | Switches user account             |
| `sudo <command>` | Runs command with root privileges |

**What is `sudo`?**

* `sudo` stands for “superuser do”. It allows a permitted user to execute a command as the superuser or another user.
* Often used to install software, access system files, or manage users.

---

## 🔍 System Monitoring

| Command        | Description                                     |
| -------------- | ----------------------------------------------- |
| `top`          | Shows live system processes                     |
| `htop`         | Interactive process viewer (install separately) |
| `ps aux`       | Lists all running processes                     |
| `df -h`        | Shows disk space usage                          |
| `du -sh <dir>` | Shows size of a directory                       |
| `free -h`      | Shows memory usage                              |
| `uptime`       | Shows how long the system has been running      |

---

## 🌐 Network Commands

| Command              | Description                                       |
| -------------------- | ------------------------------------------------- |
| `ping <host>`        | Pings a host to test connectivity                 |
| `ping example.com`   | Example: pings example.com to check response time |
| `ifconfig` or `ip a` | Shows network interfaces (deprecated: ifconfig)   |
| `netstat -tulpn`     | Lists active ports and processes                  |
| `curl <url>`         | Fetches content from URL                          |
| `wget <url>`         | Downloads file from the internet                  |

---

## 🔐 Permissions

| Command                       | Description                   |
| ----------------------------- | ----------------------------- |
| `chmod <mode> <file>`         | Changes file permissions      |
| `chown <user>:<group> <file>` | Changes file owner and group  |
| `ls -l`                       | Displays permissions of files |

---

## 📦 Archive and Compression

| Command                         | Description                  |
| ------------------------------- | ---------------------------- |
| `tar -czvf file.tar.gz folder/` | Compress folder to `.tar.gz` |
| `tar -xzvf file.tar.gz`         | Extract `.tar.gz` file       |
| `zip -r file.zip folder/`       | Create a zip archive         |
| `unzip file.zip`                | Extract a zip archive        |

---

## 🧪 Miscellaneous

| Command                   | Description                               |
| ------------------------- | ----------------------------------------- |
| `echo "Hello"`            | Prints text to console                    |
| `echo "Text" >> file.txt` | Appends "Text" to `file.txt`              |
| `date`                    | Displays the current system date and time |
| `history`                 | Shows command history                     |
| `clear`                   | Clears the terminal screen                |
| `alias ll='ls -la'`       | Creates a shortcut command                |
| `man <command>`           | Shows manual for a command                |

---

## 📴 Shutdown & Reboot

| Command             | Description                       |
| ------------------- | --------------------------------- |
| `sudo shutdown now` | Shuts down the system immediately |
| `sudo reboot`       | Reboots the system                |

---

## 🚑 Help

Use `--help` with any command to get usage instructions:

```bash
command --help
```

---

This cheat sheet is great for developers, sysadmins, and beginners using Linux or WSL environments.
