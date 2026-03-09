# 💻 Terminal Quick Guide

This guide provides the basics for using the terminal (or command line) to manage the project on **macOS/Linux (Zsh/Bash)** and **Windows (PowerShell)**.

## ⚠️ Golden Rule: One command at a time

To avoid errors, it is essential to execute commands **one line at a time**.

1. **Copy** the single command line.
2. **Paste** it into the terminal.
3. **Press Enter** to execute it.
4. **Wait** for the command to finish: you will see the prompt cursor (e.g., `$` or `>`) reappear before entering the next command.

## 📂 Navigation with `cd`

The **`cd`** (_Change Directory_) command allows you to move between folders on your computer.

### 📍 Absolute Paths

These indicate a fixed position starting from the root of the disk. They are useful when you want to be sure you reach a specific point regardless of where you currently are.

- **macOS/Linux**: Always start with `/`
  ```bash
  cd /Users/username/Documents/ai4cm
  ```
- **Windows (PowerShell)**: Start with the drive letter (e.g., `C:\`)
  ```powershell
  cd C:\Users\username\Documents\ai4cm
  ```

### 🏃 Relative Paths

These indicate a position relative to the folder you are currently in.

- **`.` (Single dot)**: Represents the current folder.
- **`..` (Double dot)**: Represents the parent folder (one level up).

```bash
# If you are in the project's root folder and want to enter 'setup':
cd setup

# If you are in 'setup' and want to go back to the root folder:
cd ..

# To see where you are now:
pwd             # (macOS/Linux)
Get-Location    # (PowerShell - or simply type 'pwd')
```

## ⌨️ Useful Tips

- **Autocompletion**: Type the first few letters of a folder or file and press **Tab**. The terminal will complete the name for you. If there are multiple options, press Tab twice to see them all.
- **Command History**: Use the **Up and Down arrows** to scroll through commands you have previously typed.
- **Spaces in Names**: If a folder has spaces in its name, wrap the path in quotes:
  ```bash
  cd "Folder With Spaces"
  ```
