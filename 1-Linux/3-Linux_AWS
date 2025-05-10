# 📦 Linux Package Managers & System Management

## 🔹 `apt` in Linux

`apt` (Advanced Package Tool) is a package manager used in **Debian-based distributions** like Ubuntu.

### ✅ Common `apt` Commands:

```bash
sudo apt update         # Update package list
sudo apt upgrade        # Upgrade installed packages
sudo apt install <pkg>  # Install a package
sudo apt remove <pkg>   # Remove a package
sudo apt purge <pkg>    # Remove a package including configs
sudo apt autoremove     # Clean up unused packages
```

### ✅ Example:

```bash
sudo apt install curl -y
```

* The `-y` flag automatically answers "yes" to prompts.

---

## 🧰 Other Linux Package Managers

| Package Manager | Used In         | Description                                |
| --------------- | --------------- | ------------------------------------------ |
| `apt`           | Debian, Ubuntu  | Advanced Package Tool                      |
| `dnf`           | Fedora, RHEL 8+ | Modernized YUM replacement                 |
| `yum`           | CentOS, RHEL    | Yellowdog Updater Modified                 |
| `rpm`           | CentOS, Fedora  | Red Hat Package Manager (lower-level tool) |
| `pacman`        | Arch Linux      | Package manager with simple syntax         |

---

## 🧮 File Permission Table (`chmod`)

| Octal | Binary | Symbol | Meaning                  |
| ----- | ------ | ------ | ------------------------ |
| 0     | 000    | ---    | No permissions           |
| 1     | 001    | --x    | Execute only             |
| 2     | 010    | -w-    | Write only               |
| 3     | 011    | -wx    | Write and execute        |
| 4     | 100    | r--    | Read only                |
| 5     | 101    | r-x    | Read and execute         |
| 6     | 110    | rw-    | Read and write           |
| 7     | 111    | rwx    | Read, write, and execute |

### Examples:

* `chmod 400 file` → Owner can read, no one else can access
* `chmod 764 file` → Owner: full, Group: rw, Others: r
* `chmod 755 file` → Owner: full, Others: read & execute
* `chmod 644 file` → Owner: read/write, Others: read only

---

## 🚀 Transfer Files from Local to AWS EC2

### ✅ Using SCP:

```bash
scp -i ~/aws-key.pem ./file.txt ubuntu@<ec2-ip>:/home/ubuntu/
```

> Ensure key permissions: `chmod 400 aws-key.pem`

### ✅ Using WinSCP:

1. Protocol: SFTP
2. Enter EC2 Public IP, Username (e.g., `ubuntu`)
3. Load `.pem` file under Advanced → Authentication

### ✅ Using `rsync`:

```bash
rsync -avz -e "ssh -i aws-key.pem" file.txt ubuntu@<ec2-ip>:/home/ubuntu/
```

---

## 🔐 IAM Role in AWS

### 🧠 What is IAM Role?

* A **temporary set of permissions** granted to a service, user, or resource to access AWS services.

### 🧾 Examples:

* EC2 instance accessing S3
* Lambda accessing DynamoDB
* Cross-account access

### 👤 IAM Role vs IAM User

| Feature   | IAM User     | IAM Role                |
| --------- | ------------ | ----------------------- |
| Permanent | ✅ Yes        | ❌ No (Temporary)        |
| Login     | ✅ With creds | ❌ No direct login       |
| Use Case  | Human/Admin  | EC2, Lambda, Automation |

---

## ⚙️ `systemctl` & System Commands

### ✅ `systemctl list-units`

* Lists all **active units** (services, devices, etc.)

```bash
systemctl list-units
systemctl list-units --type=service
```

### ✅ `systemctl status ssh`

* Shows current status & logs for the SSH service

```bash
systemctl status ssh
```

### ✅ Start/Stop/Restart Services

```bash
sudo systemctl stop nginx      # Stop Nginx
sudo systemctl restart nginx   # Restart Nginx
```

### ✅ Reboot the system

```bash
sudo reboot
```

---
