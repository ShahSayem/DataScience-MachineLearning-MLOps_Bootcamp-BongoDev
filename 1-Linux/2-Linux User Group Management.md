## 👤 How to Add User in Linux

### ➕ Add a New User

```bash
sudo adduser username
```

This creates a new user and prompts for basic info (like password).

### 🏠 Create Home Directory

```bash
sudo adduser -m username
```

The `-m` flag ensures that a home directory (e.g., `/home/username`) is created.

---

## 🔐 Set Password

### For a Specific User

```bash
sudo passwd username
```

You'll be asked to enter and confirm the password.

### For Current User

```bash
passwd
```

Lets you change your own password.

---

## 🔄 Switch User

### Switch to Another User

```bash
su - username
```

The `-` ensures the full login environment is loaded.

### Switch to Root User

```bash
su -
```

Or (if `su` is disabled):

```bash
sudo -i
```

---

## 🚪 Exit

### Exit Current Session

```bash
exit
```

Logs out from the current user session or closes the terminal.

---

## ❌ Delete User

### Without Home Directory

```bash
sudo deluser username
```

or

```bash
sudo userdel username
```

### With Home Directory

```bash
sudo deluser --remove-home username
```

or

```bash
sudo userdel -r username
```

---

## 📄 View Users in System

### Show Contents of `/etc/passwd`

```bash
cat /etc/passwd
```

Displays basic info for all users on the system:

```
username:x:UID:GID:comment:home_directory:shell
```

**Explanation of fields:**

1. `username`: Login name of the user.
2. `x`: Placeholder for password (actual password is stored in /etc/shadow).
3. `UID`: User ID (0 = root, >1000 = regular users).
4. `GID`: Group ID (links to the user's primary group).
5. `comment`: User's full name or other description.
6. `home_directory`: User's home directory path.
7. `shell`: Default login shell (e.g., /bin/bash).

**Example Entry:**

```
john:x:1001:1001:John Doe:/home/john:/bin/bash
```

---

## 👥 Create Group

### Add a New Group

```bash
sudo groupadd groupname
```

Example:

```bash
sudo groupadd developers
```

### Verify Group

```bash
cat /etc/group | grep developers
```

---

## ➕ Add User to Group

### Add User to a Specific Group

```bash
sudo usermod -aG groupname username
```

Example:

```bash
sudo usermod -aG developers alice
```

This keeps the user in existing groups and appends the new one.

> ⚠️ Changes may require logout/login to take effect.

---

## 📂 Understanding `ls -l` Output

### 1. Directory: `drwxrwxr-x 2 ubuntu ubuntu 4096 Apr 25 17:13 hello_linux`

* `d`: Indicates this is a **directory**
* `rwxrwxr-x`: **Permissions**

  * Owner (ubuntu): `rwx` = read, write, execute
  * Group (ubuntu): `rwx` = read, write, execute
  * Others: `r-x` = read, execute
* `2`: Number of links (subdirectories or references)
* `ubuntu ubuntu`: Owner and group name
* `4096`: Size in bytes (default for directories)
* `Apr 25 17:13`: Last modification date/time
* `hello_linux`: Name of the directory

### 2. File: `-rw-rw-r-- 1 ubuntu ubuntu 75 Apr 26 15:24 my_file.html`

* `-`: Indicates this is a **regular file**
* `rw-rw-r--`: **Permissions**

  * Owner: `rw-` = read, write
  * Group: `rw-` = read, write
  * Others: `r--` = read only
* `1`: Number of links (usually 1 for files)
* `ubuntu ubuntu`: Owner and group name
* `75`: File size in bytes
* `Apr 26 15:24`: Last modification date/time
* `my_file.html`: Name of the file
