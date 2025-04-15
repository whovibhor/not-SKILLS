
# 🐧 Linux Beginner Commands – Notes

Your beginner's guide to Linux commands. These are essential for navigating and managing files, users, and processes through the terminal.

---

## 📌 Basics

### `pwd` – Print Working Directory
```bash
pwd
```
Displays the full path of the current directory.

---

### `ls` – List Directory Contents
```bash
ls         # List files and folders
ls -l      # Long format listing
ls -a      # Include hidden files
ls -lh     # Human-readable sizes
```

---

### `cd` – Change Directory
```bash
cd /path/to/folder
cd ~       # Go to home
cd ..      # Go one level up
```

---

### `clear` – Clear the Terminal
```bash
clear
```

---

## 🗃️ File & Folder Management

### `mkdir` – Make Directory
```bash
mkdir new_folder
mkdir -p parent/child  # Create nested folders
```

---

### `touch` – Create File
```bash
touch file.txt
```

---

### `cp` – Copy Files and Directories
```bash
cp source.txt dest.txt
cp -r dir1 dir2  # Recursive copy for folders
```

---

### `mv` – Move or Rename
```bash
mv file.txt /path/to/new/location/
mv oldname.txt newname.txt
```

---

### `rm` – Remove Files or Directories
```bash
rm file.txt
rm -r folder/      # Recursively delete folder
rm -rf folder/     # Force delete (be careful!)
```

---

## 📄 File Content Commands

### `cat` – View File Content
```bash
cat file.txt
```

---

### `less` / `more` – View Large Files
```bash
less bigfile.txt
more bigfile.txt
```

---

### `head` / `tail` – View Start/End of File
```bash
head file.txt     # First 10 lines
tail file.txt     # Last 10 lines
tail -f log.txt   # Live monitoring
```

---

### `nano` / `vim` / `vi` – Text Editors
```bash
nano file.txt   # Easy editor
vi file.txt     # Powerful but harder
```

---

## 🔍 Searching and Filtering

### `find` – Locate Files
```bash
find . -name "file.txt"
```

---

### `grep` – Search Inside Files
```bash
grep "text" file.txt
grep -r "text" .  # Recursive search
```

---

## 📦 Package Management (Ubuntu/Debian)

### `apt` – Install/Remove Packages
```bash
sudo apt update               # Update package lists
sudo apt upgrade              # Upgrade packages
sudo apt install nginx        # Install a package
sudo apt remove nginx         # Remove a package
```

---

## 👤 User & Permission Management

### `whoami` – Current User
```bash
whoami
```

---

### `adduser` / `deluser`
```bash
sudo adduser username
sudo deluser username
```

---

### `chmod` – Change Permissions
```bash
chmod 755 file.sh
chmod +x script.sh  # Make executable
```

---

### `chown` – Change Ownership
```bash
sudo chown user:group file.txt
```

---

## 🧠 System Information

### `uname` – System Info
```bash
uname -a
```

---

### `top` / `htop` – Process Viewer
```bash
top         # Built-in
htop        # Needs installation
```

---

### `df` – Disk Usage
```bash
df -h
```

---

### `free` – Memory Usage
```bash
free -h
```

---

## 🔁 Networking Commands

### `ping` – Test Connectivity
```bash
ping google.com
```

---

### `ifconfig` / `ip a` – Network Info
```bash
ip a
```

---

### `netstat` / `ss` – Port and Connection Info
```bash
ss -tuln
```

---

## 🧪 Others

### `history` – Show Previous Commands
```bash
history
```

---

### `alias` – Create Shortcut for Commands
```bash
alias ll='ls -la'
```

---

### `man` – Manual Pages
```bash
man ls
```

---

## 🧹 Cleanup

### `sudo apt autoremove`
```bash
sudo apt autoremove   # Remove unused packages
```

---

## 🧰 Pro Tip: Combine Commands

```bash
cd mydir && ls -la
```

Use `&&` to run commands only if the previous one succeeds.

---
