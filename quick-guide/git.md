# 🐙 Git Quick Guide

Welcome to the essential **Git** command guide. This guide will help you manage version control for your project in a simple and efficient way.

## 🛠️ 1. Setup (Clone & Init)

Before working on a project, you need to "connect" it to Git.

- **Initialize a new local project:**

  ```bash
  git init
  ```

  _Creates a new Git repository in the current folder._

- **Clone an existing project:**
  ```bash
  git clone <repository-url>
  ```
  _Downloads a complete copy of a remote repository to your computer._

## 💾 2. Saving Work (Commit)

A commit is like a "save" while working on a file offline.

1. **Stage files for saving:**

   ```bash
   git add .
   ```

   _(`.` adds all modified files, or you can specify one like `git add file.py`)_

2. **Create the save point:**
   ```bash
   git commit -m "Description of changes"
   ```

## 🚀 3. Synchronization (Push & Pull)

Keep your code aligned with the server (e.g., GitHub).

- **Download updates (Pull):**

  ```bash
  git pull
  ```

  _IMPORTANT: Always run this before starting work to avoid conflicts._

- **Send your updates (Push):**
  ```bash
  git push
  ```

## 🌿 4. Parallel Work (Checkout & Merge)

Branches allow you to experiment without breaking the main code.

- **Move to another branch (Checkout):**

  ```bash
  git checkout <branch-name>
  ```

  _To create a new branch and switch to it immediately:_ `git checkout -b new-branch`

- **Combine branches (Merge):**
  Switch to the "destination" branch (e.g., `main`) and run:
  ```bash
  git merge <branch-to-merge>
  ```

## 🔍 5. Inspecting the Status

Keep track of what's happening in your repository.

- **Check which files are modified:**

  ```bash
  git status
  ```

  _Shows which files are staged, unstaged, or untracked._

- **View commit history:**

  ```bash
  git log
  ```

  _Lists recent commits in chronological order._

- **See line-by-line changes:**
  ```bash
  git diff
  ```
  _Shows exactly what you changed before staging._

## 📋 Summary Table

| Command                | Description                                      |
| :--------------------- | :----------------------------------------------- |
| **`git init`**         | Initialize a new Git repository.                 |
| **`git clone`**        | Download a complete copy of a remote repository. |
| **`git status`**       | Check which files have been modified.            |
| **`git add .`**        | Stage all modified files for saving.             |
| **`git commit -m ""`** | Create a save point with a description.          |
| **`git push`**         | Send your updates to the remote server.          |
| **`git pull`**         | Download updates from the remote server.         |
| **`git branch`**       | List available branches.                         |
| **`git checkout`**     | Switch to another branch.                        |
| **`git merge`**        | Combine changes from another branch.             |
| **`git log`**          | View the commit history.                         |
| **`git diff`**         | Compare changes not yet staged.                  |

### 🎨 Tip: Initial Configuration

If it's your first time using Git, remember to identify yourself:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```
