## 📚 Resource
- Git documentation
- Online tutorials link : https://youtu.be/S7XpTAnSDL4?si=8VEJCkT0e7JNXEOI
- Community forums (Stack Overflow, GitHub Discussions)

# FOLLOW THIS :

## 1️⃣ Setting Up Git

### Initialize a Git repository (for a new project)

```bash
git init

```

### Check Git version

```bash
git --version

```

### Set up your Git username and email (required for commits)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

```

### Check Git configurations

```bash
git config --list

```

## 2️⃣ Connecting to a Remote Repository (GitHub)

### Link local project to a GitHub repository

```bash
git remote add origin https://github.com/your-username/repo-name.git

```

### Check linked repository

```bash
git remote -v

```

## 3️⃣ Basic Workflow: Tracking & Committing Changes

### Check the status of your files

```bash
git status

```

### Add all changes to staging area

```bash
git add .

```

### Commit changes with a message

```bash
git commit -m "Your commit message"

```

## 4️⃣ Working with Branches

### Create a new branch

```bash
git branch branch-name

```

### Switch to a branch

```bash
git checkout branch-name

```

OR (modern approach)

```bash
git switch branch-name

```

### Create & switch to a new branch in one step

```bash
git checkout -b branch-name

```

### List all branches

```bash
git branch -a

```

### Delete a branch (local)

```bash
git branch -d branch-name

```

### Delete a branch (remote)

```bash
git push origin --delete branch-name

```

## 5️⃣ Pushing & Pulling Changes

### Push changes to a remote repository

```bash
git push origin branch-name

```

### Pull the latest changes from remote

```bash
git pull origin branch-name

```

### Fetch latest changes without merging

```bash
git fetch origin

```

## 6️⃣ Merging Changes

### Merge another branch into your current branch

```bash
git merge branch-name

```

### Merge `main` branch into your current branch

```bash
git merge main

```

### Rebase a branch onto `main` (cleaner history)

```bash
git rebase main

```

## 7️⃣ Fixing Merge Conflicts

### Check for merge conflicts

```bash
git status

```

### Abort a merge if there are issues

```bash
git merge --abort

```

### Resolve conflicts manually:

- Open the conflicted files
- Remove `<<<<<<<`, `=======`, and `>>>>>>>` markers
- Keep the correct version
- Save the file

### Mark conflicts as resolved and continue

```bash
git add file-name
git commit -m "Resolved merge conflict"

```

## 8️⃣ Undoing Mistakes

### Undo last commit (keep changes)

```bash
git reset --soft HEAD~1

```

### Undo last commit completely (remove changes)

```bash
git reset --hard HEAD~1

```

### Undo a pushed commit (remote fix)

```bash
git revert commit-hash
git push origin branch-name

```

## 9️⃣ Working with All Branches

### Push all branches (not recommended for large projects)

```bash
git push --all origin

```

### Merge `main` branch into all branches

```bash
for branch in `git branch | sed 's/*//g'`; do
    git checkout $branch
    git merge main
    git push origin $branch
done

```

## 🔟 Quick Reference Table

| Command | Description |
| --- | --- |
| `git status` | Check current changes |
| `git log --oneline` | View commit history (short) |
| `git branch` | List all branches |
| `git checkout branch-name` | Switch to a branch |
| `git merge main` | Merge `main` into current branch |
| `git push origin branch-name` | Push changes to GitHub |
| `git pull origin main` | Pull latest changes from GitHub |
| `git reset --hard HEAD~1` | Undo last commit completely |
| `git revert commit-hash` | Undo a pushed commit |
| `git remote -v` | Show remote GitHub link |

---

This cheat sheet covers everything from setup to fixing mistakes. Keep practicing! 🚀