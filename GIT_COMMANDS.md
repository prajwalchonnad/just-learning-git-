# 📚 Complete Git Commands Handbook & Cheatsheet

> A comprehensive, beginner-to-advanced reference guide for mastering Git.  
> Whether you are taking your first steps or troubleshooting a complex merge conflict, this guide covers everything you need.

---

## 📑 Table of Contents

- [🧠 Git Core Concepts & Architecture](#-git-core-concepts--architecture)
- [1. Configuration & Setup](#1-configuration--setup)
- [2. Starting & Cloning Repositories](#2-starting--cloning-repositories)
- [3. Everyday Snapshotting (Basic Workflow)](#3-everyday-snapshotting-basic-workflow)
- [4. Inspecting Status & Diffs](#4-inspecting-status--diffs)
- [5. Commit History & Logging](#5-commit-history--logging)
- [6. Branching & Switching](#6-branching--switching)
- [7. Merging & Integration](#7-merging--integration)
- [8. Rebasing & History Rewriting](#8-rebasing--history-rewriting)
- [9. Stashing (Temporary Shelving)](#9-stashing-temporary-shelving)
- [10. Undoing Changes & Recovery](#10-undoing-changes--recovery)
- [11. Remote Repositories & Collaboration](#11-remote-repositories--collaboration)
- [12. Tagging & Versioning](#12-tagging--versioning)
- [13. Debugging & Investigation (Bisect, Blame, Grep)](#13-debugging--investigation-bisect-blame-grep)
- [14. Repo Maintenance & Housekeeping](#14-repo-maintenance--housekeeping)
- [🚨 "Oh No, Git!" - Common Real-World Scenarios](#-oh-no-git---common-real-world-scenarios)
- [⚡ Supercharge Your Workflow: Git Aliases](#-supercharge-your-workflow-git-aliases)
- [🌟 Git Best Practices Checklist](#-git-best-practices-checklist)

---

## 🧠 Git Core Concepts & Architecture

Git tracks your project through four primary environments / stages:

```
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [ Working Directory ]  ---( git add )--->   [ Staging Area (Index) ]             |
|   (Unstaged files)                             (Files ready to commit)            |
|          ^                                                |                       |
|          |                                                | ( git commit )        |
|          | ( git checkout / git restore )                 v                       |
|          +-----------------------------------   [ Local Repository ]              |
|                                                (Committed history in .git)        |
|                                                           |                       |
|                                                           | ( git push / pull )   |
|                                                           v                       |
|                                                 [ Remote Repository ]             |
|                                                (GitHub / GitLab / Bitbucket)      |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

---

## 1. Configuration & Setup

Configure user identity, defaults, and global settings across your machine.

| Command | Description |
|---|---|
| `git config --global user.name "Your Name"` | Set global author name |
| `git config --global user.email "you@example.com"` | Set global author email |
| `git config --global init.defaultBranch main` | Default initial branch name to `main` |
| `git config --global core.editor "code --wait"` | Set default editor (VS Code, nano, vim, etc.) |
| `git config --global core.autocrlf true` | Convert CRLF to LF on Windows (set `input` on macOS/Linux) |
| `git config --list` | List all resolved configurations |
| `git config --list --show-origin` | List configuration items along with the file they originate from |
| `git config --global alias.<shortname> <command>` | Create a shortcut / alias for a command |

#### Example:
```bash
# Check current config
git config user.name
git config user.email
```

---

## 2. Starting & Cloning Repositories

| Command | Description |
|---|---|
| `git init` | Initialize a new local Git repository in the current folder |
| `git init <directory-name>` | Create a directory and initialize a Git repository inside it |
| `git clone <repo-url>` | Clone an existing remote repository into a new folder |
| `git clone <repo-url> <folder-name>` | Clone a remote repository into a custom named directory |
| `git clone --depth 1 <repo-url>` | Shallow clone with only the most recent commit (fast, saves space) |
| `git clone --branch <name> <repo-url>` | Clone a specific branch directly |

---

## 3. Everyday Snapshotting (Basic Workflow)

Stage, commit, remove, and rename files.

| Command | Description |
|---|---|
| `git add <file>` | Stage a specific file for the next commit |
| `git add .` | Stage all modified, new, and deleted files in the current folder |
| `git add -A` or `git add --all` | Stage all changes across the entire repository |
| `git add -p` | Interactive staging: stage parts/hunks of files selectively |
| `git commit -m "Your message"` | Commit staged snapshot with an inline message |
| `git commit -am "Your message"` | Stage tracked modified files and commit in one step (skips untracked) |
| `git commit --amend` | Replace the last commit with new changes or edit the commit message |
| `git rm <file>` | Remove a file from both working directory and Git index |
| `git rm --cached <file>` | Stop tracking a file but keep it on local disk (useful for `.gitignore`) |
| `git mv <old-filename> <new-filename>` | Rename or move a tracked file and stage the change automatically |

---

## 4. Inspecting Status & Diffs

| Command | Description |
|---|---|
| `git status` | Show status of working tree, unstaged, and staged changes |
| `git status -s` or `git status --short` | Give short-format status output |
| `git diff` | Show changes between working directory and the staging area |
| `git diff --staged` or `git diff --cached` | Show changes between staging area and last commit |
| `git diff HEAD` | Show all changes in working directory and staging area relative to HEAD |
| `git diff branchA..branchB` | Show differences between two branches |
| `git diff <commit1> <commit2>` | Compare two arbitrary commits |
| `git diff --stat` | Show summary statistics of changed lines per file |

---

## 5. Commit History & Logging

Explore who made what changes and when.

| Command | Description |
|---|---|
| `git log` | Show full commit history in chronological order |
| `git log --oneline` | Compact view: 1 commit per line (short hash + title) |
| `git log --graph --oneline --decorate --all` | ASCII graph of branches, merges, tags, and commits across all refs |
| `git log -n <number>` | Limit output to the last `N` commits (e.g. `git log -n 5`) |
| `git log --author="Name"` | Filter commits by author name |
| `git log --since="2 weeks ago"` | Show commits made within a specific time window |
| `git log --grep="bug fix"` | Search commit messages containing a keyword |
| `git log -p <file>` | Show full patch/diff history for a specific file |
| `git log -S "secretKey"` | Find commits that introduced or deleted a specific string (pickaxe) |
| `git shortlog -sn` | Summary count of commits per contributor |
| `git show <commit-hash>` | Show metadata and full diff of a specific commit |
| `git show <commit-hash>:<path>` | View the content of a file as it existed in a specific commit |

---

## 6. Branching & Switching

Branches represent independent lines of development.

| Command | Description |
|---|---|
| `git branch` | List all local branches (current branch highlighted) |
| `git branch -a` | List all local and remote-tracking branches |
| `git branch -r` | List remote-tracking branches only |
| `git branch <branch-name>` | Create a new branch at current commit (does not switch to it) |
| `git switch <branch-name>` | Modern way to switch to an existing branch |
| `git switch -c <new-branch>` | Create and switch to a new branch (same as `git checkout -b`) |
| `git checkout <branch-name>` | Traditional command to switch to an existing branch |
| `git checkout -b <new-branch>` | Create and switch to a new branch in one command |
| `git branch -m <new-name>` | Rename the current branch |
| `git branch -m <old-name> <new-name>` | Rename an arbitrary local branch |
| `git branch -d <branch-name>` | Safe-delete a merged local branch |
| `git branch -D <branch-name>` | Force-delete an unmerged branch |
| `git branch --merged` | List branches that have been merged into current HEAD |
| `git branch --no-merged` | List branches with commits not yet merged into HEAD |

---

## 7. Merging & Integration

Combine independent histories into one.

| Command | Description |
|---|---|
| `git merge <branch-name>` | Merge `<branch-name>` into your currently active branch |
| `git merge --no-ff <branch>` | Always create a merge commit even if fast-forward is possible |
| `git merge --squash <branch>` | Combine all branch commits into a single staged change |
| `git merge --abort` | Abort a conflicted merge and restore the pre-merge state |
| `git mergetool` | Launch configured visual merge tool to resolve conflicts |
| `git merge-base branchA branchB` | Find the common ancestor commit of two branches |

---

## 8. Rebasing & History Rewriting

Rebasing reapplies commits on top of another base tip, producing a clean linear history.

| Command | Description |
|---|---|
| `git rebase <base-branch>` | Rebase current branch on top of `<base-branch>` |
| `git rebase -i HEAD~<n>` | Interactive rebase over the last `N` commits (squash, reorder, edit, drop) |
| `git rebase --continue` | Continue rebasing after resolving a conflict |
| `git rebase --skip` | Skip the current conflicted patch during rebase |
| `git rebase --abort` | Cancel the rebase operation and restore the original branch state |
| `git cherry-pick <commit-hash>` | Apply changes introduced by an existing commit onto current branch |
| `git cherry-pick -n <commit>` | Cherry-pick changes to staging area without creating a commit |
| `git revert <commit-hash>` | Create a new commit that inverts / undoes a past commit (safe for shared branches) |

> ⚠️ **The Golden Rule of Rebasing:** Never rebase branches that have already been pushed to a public/shared repository. Rebase local, unpushed feature branches only!

---

## 9. Stashing (Temporary Shelving)

Save modified and untracked files temporarily to clean your working tree without committing.

| Command | Description |
|---|---|
| `git stash` or `git stash push` | Save uncommitted changes to a new stash entry |
| `git stash save "Work in progress description"` | Save stash with a descriptive label |
| `git stash -u` or `git stash --include-untracked` | Stash both tracked modifications AND untracked files |
| `git stash list` | List all stashed changes in stack order (`stash@{0}`, `stash@{1}`, ...) |
| `git stash pop` | Apply the most recent stash and remove it from the stack |
| `git stash pop stash@{n}` | Apply specific stash and drop it |
| `git stash apply` | Apply the most recent stash without removing it from stack |
| `git stash show -p` | Inspect the diff contained inside the most recent stash |
| `git stash drop stash@{n}` | Delete a specific stash entry |
| `git stash clear` | Remove all stashed entries permanently |
| `git stash branch <new-branch>` | Create a new branch, checkout to it, and apply stashed work |

---

## 10. Undoing Changes & Recovery

| Command | Description |
|---|---|
| `git restore <file>` | Discard changes in working directory for a file (uncommitted changes lost) |
| `git restore .` | Discard all local uncommitted changes in current directory |
| `git restore --staged <file>` | Unstage a file without losing its working directory changes |
| `git reset HEAD <file>` | Older syntax to unstage a file |
| `git reset --soft HEAD~1` | Undo the last commit, keep changes in the Staging Area |
| `git reset --mixed HEAD~1` (default) | Undo the last commit, keep changes in the Working Directory (unstaged) |
| `git reset --hard HEAD~1` | 💣 Discard the last commit and all changes completely |
| `git clean -n` | Dry run: preview untracked files that would be deleted |
| `git clean -fd` | Force-remove untracked files and directories |
| `git reflog` | Record of every HEAD movement (lifesaver for recovering "lost" commits) |
| `git reset --hard HEAD@{n}` | Reset HEAD to an entry recorded in the reflog |

---

## 11. Remote Repositories & Collaboration

Communicate with remote servers (GitHub, GitLab, etc.).

| Command | Description |
|---|---|
| `git remote -v` | List all configured remote names with fetch & push URLs |
| `git remote add <name> <url>` | Add a new remote repository (usually `origin`) |
| `git remote rename <old> <new>` | Rename a remote shortcut |
| `git remote remove <name>` | Disconnect a remote repository |
| `git remote show origin` | Display detailed information about the remote and branches |
| `git fetch <remote>` | Download objects and refs from remote, but do NOT merge |
| `git fetch --all --prune` | Fetch from all remotes and prune stale deleted tracking branches |
| `git pull` | Fetch changes from tracking branch and merge into current local branch |
| `git pull --rebase` | Fetch changes and rebase local commits on top of incoming commits |
| `git push <remote> <branch>` | Push local branch commits to the remote |
| `git push -u origin <branch>` | Push branch and set upstream tracking reference |
| `git push origin --delete <branch>` | Delete a remote branch on GitHub/remote server |
| `git push --force-with-lease` | Safer force-push: pushes only if remote branch hasn't changed unexpectedly |

---

## 12. Tagging & Versioning

Create pointers to specific milestones in release history.

| Command | Description |
|---|---|
| `git tag` | List all tags |
| `git tag -l "v1.*"` | List tags matching a pattern |
| `git tag v1.0.0` | Create a lightweight tag at current commit |
| `git tag -a v1.0.0 -m "Release v1.0.0"` | Create an annotated tag with metadata and message (recommended) |
| `git tag -a v1.0.0 <commit-hash>` | Tag a past commit retrospectively |
| `git show v1.0.0` | View tag details and the associated commit |
| `git push origin v1.0.0` | Push a single tag to remote repository |
| `git push origin --tags` | Push all local tags to remote repository |
| `git tag -d v1.0.0` | Delete a local tag |
| `git push origin --delete v1.0.0` | Delete a tag on remote |

---

## 13. Debugging & Investigation (Bisect, Blame, Grep)

| Command | Description |
|---|---|
| `git blame <file>` | Show who last modified each line in a file and in which commit |
| `git blame -L 15,30 <file>` | Show blame for lines 15 through 30 only |
| `git grep "functionName"` | Search repository tracked files for text or regex |
| `git grep -n "functionName"` | Search and display matching line numbers |
| `git bisect start` | Start a binary search to pinpoint which commit introduced a bug |
| `git bisect bad` | Mark current commit as broken / bugged |
| `git bisect good <commit>` | Mark a known good past commit |
| `git bisect reset` | Finish bisect session and return to original HEAD |
| `git fsck` | Verify connectivity and integrity of internal objects |

---

## 14. Repo Maintenance & Housekeeping

| Command | Description |
|---|---|
| `git gc` | Cleanup unnecessary files and optimize local repo storage |
| `git gc --prune=now` | Garbage collect and remove unreachable loose objects immediately |
| `git prune -v` | Prune all unreachable objects from database |
| `git archive --format=zip HEAD -o release.zip` | Export current repo state into a clean zip archive (no `.git` directory) |
| `git bundle create repo.bundle --all` | Package complete repo into a single standalone portable file |

---

## 🚨 "Oh No, Git!" - Common Real-World Scenarios

### 1. I made a typo in the last commit message:
```bash
git commit --amend -m "Corrected commit message"
```

### 2. I forgot to include a file in the last commit:
```bash
git add forgotten_file.txt
git commit --amend --no-edit
```

### 3. I accidentally committed changes to `main` instead of a feature branch:
```bash
# 1. Create a new branch with your commits
git branch feature-branch

# 2. Reset main back 1 commit (or however many you made)
git reset --hard HEAD~1

# 3. Switch to your new feature branch
git switch feature-branch
```

### 4. I accidentally ran `git reset --hard` and lost my commits!
```bash
# 1. Inspect recent HEAD positions
git reflog

# 2. Find the commit hash right before your accidental reset (e.g., HEAD@{1} or abc1234)
git reset --hard HEAD@{1}
```

### 5. I want to undo a commit that was already pushed to GitHub:
```bash
# Create a new commit that reverts the changes without altering past history
git revert <commit-hash>
git push origin main
```

### 6. I want to discard all local uncommitted changes:
```bash
# Discard modified tracked files
git restore .

# Remove untracked files and directories
git clean -fd
```

### 7. How do I resolve a merge conflict?
```bash
# 1. Check which files have conflicts
git status

# 2. Open the conflicted files. Look for conflict markers:
# <<<<<<< HEAD
# Your current branch changes
# =======
# Incoming branch changes
# >>>>>>> incoming-branch

# 3. Edit the file to keep the desired code and remove markers.
# 4. Stage resolved file:
git add <file>

# 5. Finalize the merge:
git commit -m "Merge resolved: integrated updates"
```

---

## ⚡ Supercharge Your Workflow: Git Aliases

Run these once in your terminal to save thousands of keystrokes:

```bash
# Quick status
git config --global alias.st status

# Quick checkout / switch
git config --global alias.co checkout
git config --global alias.sw switch

# Quick branch & commit
git config --global alias.br branch
git config --global alias.cm "commit -m"

# Beautiful graphical log
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# Unstage shortcut
git config --global alias.unstage "restore --staged"

# Show last commit
git config --global alias.last "log -1 HEAD --stat"
```

Now you can simply type:
```bash
git st          # git status
git lg          # gorgeous visual graph log
git cm "msg"    # git commit -m "msg"
```

---

## 🌟 Git Best Practices Checklist

- [ ] **Commit Small & Atomic:** Each commit should represent one logical unit of work.
- [ ] **Write Clear Imperative Commit Messages:** Use messages like `Fix login validation error` rather than `fixed bug` or `stuff`.
- [ ] **Always Pull Before You Push:** Run `git pull --rebase` to avoid messy merge bubbles.
- [ ] **Keep `.gitignore` Up to Date:** Never commit binaries, `.env` files with secret API keys, or dependencies (`node_modules/`, `venv/`).
- [ ] **Protect Shared History:** Never force-push (`push -f`) to public branches like `main` or `dev`.
- [ ] **Use Feature Branches:** Always work in a branch (`git switch -c feature/new-idea`) rather than committing directly to `main`.

---

<div align="center">

**Happy Coding & Version Controlling! 🚀**  
*Found this helpful? Share it with fellow developers!*

</div>
