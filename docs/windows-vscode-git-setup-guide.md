# Windows Setup Guide: Install VS Code + Git and Pull This Repo

## Who This Is For
You are an engineer, not an IT support wizard, and that is completely fine.  
This guide assumes zero software setup experience and explains everything with engineering-style analogies.

## What You Are Building (Big Picture)
Think of this setup like preparing a workshop:

- **Git** = your revision control cabinet.  
  It stores every drawing revision, who changed what, and when.
- **GitHub** = the central project vault in the cloud.  
  Everyone pulls the latest approved drawing set from here.
- **Repository (repo)** = one project folder with files + history.
- **Clone** = bring a full copy of the project vault onto your machine.
- **Pull** = fetch the newest approved revisions into your local copy.
- **VS Code** = your smart workbench/editor where you view and edit files.

If you can follow an assembly manual, you can do this.

---

## Step 0: One-Time Prerequisites

1. Have a Windows 10 or 11 machine.
2. Make sure you can access this repo URL in your browser:  
   `https://github.com/BicycleJeanre/coding-playground`
3. If the repo is private, ask the repo owner to grant your GitHub account access.

---

## Step 1: Install Git on Windows

### 1.1 Download Git
1. Open: <https://git-scm.com/download/win>
2. Download starts automatically.
3. Run the installer (`Git-*.exe`).

### 1.2 Installer choices (safe defaults)
You can click **Next** through most screens.  
If these options appear, use:

- **Default editor used by Git**: choose **Visual Studio Code** (if available).
- **Adjusting your PATH environment**: choose **Git from the command line and also from 3rd-party software**.
- **Configuring the line ending conversions**: choose **Checkout Windows-style, commit Unix-style line endings**.

Everything else can stay default.

### 1.3 Verify Git install
1. Open **PowerShell** (Start menu -> type `PowerShell`).
2. Run:

```powershell
git --version
```

You should see something like:
`git version 2.xx.x.windows.x`

If you see that, Git is installed correctly.

---

## Step 2: Install Visual Studio Code

### 2.1 Download and install
1. Open: <https://code.visualstudio.com/>
2. Click **Download for Windows**.
3. Run the installer.

### 2.2 Important install checkboxes
When prompted, check:

- **Add "Open with Code" action**
- **Add to PATH** (so `code` command works in terminal)

Finish installation, then launch VS Code once.

### 2.3 Verify VS Code in terminal (optional but useful)
In PowerShell, run:

```powershell
code --version
```

If a version prints, terminal integration works.

---

## Step 3: Clone This Repository to Your Windows Machine

### 3.1 Pick a local project location
Example location:

`C:\Users\<YourName>\Documents\GitHub`

### 3.2 Create folder and clone
Run these commands in PowerShell:

```powershell
cd $HOME\Documents
mkdir GitHub -ErrorAction SilentlyContinue
cd GitHub
git clone https://github.com/BicycleJeanre/coding-playground.git
cd coding-playground
```

What just happened (engineering analogy):

- `git clone ...` is like receiving the full latest drawing package + revision log.
- `cd coding-playground` is walking into that project bay on your local machine.

### 3.3 Open repo in VS Code
Still in PowerShell:

```powershell
code .
```

If `code .` fails, open VS Code manually:

1. Open VS Code.
2. **File -> Open Folder**
3. Select your local `coding-playground` folder.

---

## Step 4: Pull Latest Changes (the command you will use often)

Any time you want the newest repo updates:

1. Open PowerShell.
2. Go to your repo:

```powershell
cd $HOME\Documents\GitHub\coding-playground
```

3. Pull latest:

```powershell
git pull origin main
```

Engineering analogy: this is like syncing your local drawing copy to the latest approved revision from document control.

---

## Step 5: Basic Daily Workflow (No IT jargon mode)

1. Open the project folder in VS Code.
2. Before starting work, run:

```powershell
git pull origin main
```

3. Do your edits.
4. Save files.
5. (Later, when needed) commit and push your changes.

If all you need today is to get the project and keep it updated, clone + pull is enough.

---

## Common Problems and Fast Fixes

### Problem: `'git' is not recognized`
Meaning: Windows cannot find Git in PATH.

Fix:
1. Restart terminal/PC once.
2. If still broken, reinstall Git and ensure PATH option above is selected.

### Problem: `'code' is not recognized`
Fix:
1. Reinstall VS Code and tick **Add to PATH**.
2. Or open VS Code manually and open folder via menu.

### Problem: Git asks for login when cloning/pulling
This is normal for private repos.

Fix:
1. Sign in to GitHub in the prompt/browser when asked.
2. Ensure your GitHub account has access to the repo.

### Problem: `Permission denied` on repo
Meaning: your GitHub account has no access yet.

Fix:
Ask the repo owner to add your account as a collaborator.

---

## Tiny Glossary (Plain English)

- **Terminal**: text-based control panel for commands.
- **Command**: typed instruction (like pressing a machine control button, but with words).
- **Branch**: alternate design path; `main` is usually the primary approved path.
- **Commit**: saved checkpoint with notes.
- **Origin**: nickname for the cloud repo URL.

---

## Optional Friendly Roast Lines (Mild and Safe)
If you want light banter while helping your friend, keep it playful:

- "If you can read a stress-strain chart, you can click `Next` in an installer."
- "This is easier than explaining tolerances to procurement."
- "You literally solve harder problems before lunch."

---

## Final Copy-Paste Command Block
Use this exact block in PowerShell on Windows:

```powershell
cd $HOME\Documents
mkdir GitHub -ErrorAction SilentlyContinue
cd GitHub
git clone https://github.com/BicycleJeanre/coding-playground.git
cd coding-playground
git pull origin main
code .
```

Done. You now have Git installed, VS Code installed, the repo cloned locally, and a repeatable way to pull updates.
