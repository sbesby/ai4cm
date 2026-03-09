# AI4CM - Artificial Intelligence for Communication and Marketing

Welcome to the **AI4CM** exercises repository. This project contains the necessary tools and environments for the exercises. You can use this project to perform the exercises with a pre-configured environment.

## 📥 How to get the project

You can get the code in several ways:

1. **Fork the repository**: Click the **"Fork"** button at the top right to create your own copy of the project (you must have a GitHub account).
2. **Clone the repository**: If you have Git installed, follow our [Git Quick Guide](quick-guide/git.md).
3. **Download ZIP**: Click the green **"Code"** button at the top right and select **"Download ZIP"**.

## 🚀 1. Software Installation (Mamba)

**Mamba** is an ultra-fast package manager. We recommend installing **Miniforge**, which includes Mamba.

### 🍎 macOS

You can install **Miniforge** using [Homebrew](https://brew.sh/) or the manual script:

**Option A: via Homebrew**

Open a terminal and run the following command:

```bash
brew install --cask miniforge
```

**Option B: via Script**

Open a terminal and run the following command:

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh"
bash Miniforge3-MacOSX-arm64.sh
```

_(If you are using an Intel-based Mac, download `Miniforge3-MacOSX-x86_64.sh` in Option B)_

### 🪟 Windows

1. Download [Miniforge3-Windows-x86_64.exe](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe).
2. Run the installer and follow the wizard.

### 🐧 Linux

Open a terminal and run the following command:

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh"
bash Miniforge3-Linux-x86_64.sh
```

## 🛠️ 2. Environment Configuration

Once Mamba is installed, open your terminal and move to the project folder - the one containing the `environment.yml` file - and create the environment:

_(see our [Terminal Quick Guide](quick-guide/terminal.md) if you need help moving to the project folder in the terminal)_

```bash
mamba env create -f environment.yml
```

> [!NOTE]
> **Windows users**: Run these commands using the **Miniforge Prompt** (which you can find in the Start Menu) to ensure `mamba` is recognized correctly.

## 📓 3. Notebook Configuration

We recommend using [VS Code](https://code.visualstudio.com/) (or [Antigravity](https://antigravity.google/)) for the best coding experience. These editors provide seamless integration with Jupyter notebooks and the project's environment.

To work with Jupyter notebooks (`.ipynb`):

1. **Open the project folder**: Open the root folder of the project (where the `environment.yml` file is located) in your editor.

   > [!IMPORTANT]
   > The project includes a `.vscode` folder with recommended settings. When you open the folder, VS Code will ask if you want to install the **recommended extensions** (Python, Jupyter, etc.). Click **"Install"** to ensure everything works correctly.

2. **Open a notebook**: Open a file like `setup/test_notebook.ipynb`.

3. **Kernel Selection**: In the top right corner, click on **"Select Kernel"** (or the displayed Python version) and select the **`ai4cm-env`** environment.

> [!TIP]
> If the environment does not appear, make sure you have correctly selected the Python interpreter by pressing `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows), typing **`Python: Select Interpreter`**, and choosing the entry labeled **`ai4cm-env`**. If you still don't see it, try restarting VS Code.

## 📚 Appendix

### Running Python Scripts

To run Python scripts from the terminal, you need to ensure your shell is initialized and the environment is active.

#### 1. Shell Initialization (First time only)

Initialize your shell:

- **macOS/Linux**:
  ```bash
  mamba shell init --shell zsh  # or bash
  source ~/.zshrc              # or ~/.bashrc
  ```
- **Windows**:
  We recommend using the **Miniforge Prompt** (search for it in the Start Menu).
  Alternatively, to use standard PowerShell, initialize it once:
  ```powershell
  mamba shell init powershell
  # Then restart your terminal
  ```

#### 2. Environment Activation

Before running a script, activate the project environment:

```ba sh
mamba activate ai4cm-env
```

#### 3. Execution

Once the environment is active, you can run your scripts:

```bash
python setup/test_script.py
```

---

### Direct Command Execution

If you want to run a command directly without activating the environment first, use `mamba run`:

```bash
mamba run -n ai4cm-env python setup/test_script.py
```

### Basic Mamba Commands

| Action                   | Command                                       |
| :----------------------- | :-------------------------------------------- |
| **Activate environment** | `mamba activate ai4cm-env`                    |
| **Update environment**   | `mamba env update -f environment.yml --prune` |
| **List environments**    | `mamba env list`                              |
| **Remove environment**   | `mamba env remove -n ai4cm-env`               |
