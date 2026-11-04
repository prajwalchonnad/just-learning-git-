#!/usr/bin/env python3
"""
🎮 JUST LEARNING GIT - THE INTERACTIVE TERMINAL GAME
Author: Prajwal D. Chonnad
Repository: prajwalchonnad/just-learning-git-

An interactive, laugh-out-loud Git learning adventure and real-world developer survival trainer.
For everyone learning Git — from self-taught beginners to students and engineers worldwide.
"""

import sys
import time
import random
import os

import subprocess

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        os.system("chcp 65001 >nul 2>&1")
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stdin.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Auto-launch into a dedicated spacious window on Windows
if sys.platform == "win32" and "--new-window" not in sys.argv and "--no-window" not in sys.argv:
    script_path = os.path.abspath(__file__)
    try:
        subprocess.Popen(
            [sys.executable, script_path, "--new-window"],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        print("\n\033[92m[*] Launching 'JUST LEARNING GIT' in a new dedicated arcade window! 🚀\033[0m\n")
        sys.exit(0)
    except Exception:
        # Fallback to current window if popup fails
        pass

# Configure the window if running in dedicated mode
if sys.platform == "win32":
    try:
        os.system("title 🎮 JUST LEARNING GIT - Arcade")
        os.system("mode con: cols=108 lines=40 >nul 2>&1")
    except Exception:
        pass

# Terminal Colors & Formatting
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

def print_slow(text, delay=0.012, color=""):
    """Prints text with a subtle typing effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Color.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

BANNER_ART = r"""
     _ _   _ ____ _____   _     _____    _    ____  _   _ ___ _   _  ____    ____ ___ _____ 
    | | | | / ___|_   _| | |   | ____|  / \  |  _ \| \ | |_ _| \ | |/ ___|  / ___|_ _|_   _|
 _  | | | | \___ \ | |   | |   |  _|   / _ \ | |_) |  \| || ||  \| | |  _  | |  _ | |  | |  
| |_| | |_| |___) || |   | |___| |___ / ___ \|  _ <| |\  || || |\  | |_| | | |_| || |  | |  
 \___/ \___/|____/ |_|   |_____|_____/_/   \_\_| \_\_| \_|___|_| \_|\____|  \____|___| |_|  
"""

BANNER = f"""{Color.CYAN}{Color.BOLD}{BANNER_ART}{Color.RESET}
{Color.YELLOW}{Color.BOLD}              🚀 Learn Git with real scenarios — interactive, fun, and practical.
{Color.RESET}"""

# ----------------- GAME DATA -----------------

VIVA_QUESTIONS = [
    {
        "q": "What is the difference between 'git fetch' and 'git pull'?",
        "options": [
            "A) They are identical commands with different names.",
            "B) git fetch downloads remote changes but does NOT merge; git pull downloads AND merges.",
            "C) git fetch only works on GitHub; git pull works everywhere.",
            "D) git fetch merges automatically; git pull asks for confirmation first."
        ],
        "ans": "B",
        "tip": "git fetch is safe — it updates your remote tracking branches without touching your local files. git pull = fetch + merge in one step.",
        "praise": "Correct! Knowing this distinction helps you avoid surprise merges on important branches.",
        "roast": "Not quite. git fetch downloads changes but leaves your local branch untouched. git pull goes further and merges them in."
    },
    {
        "q": "You pushed a buggy commit directly to 'main' and teammates have already pulled it. What is the safest way to undo it?",
        "options": [
            "A) git reset --hard HEAD~1  then force push",
            "B) git revert <commit-id>",
            "C) Delete the repository and start fresh",
            "D) Manually edit the files and commit again without documenting it"
        ],
        "ans": "B",
        "tip": "git revert creates a new commit that undoes the changes — it does NOT rewrite history, so it is safe for shared branches.",
        "praise": "Exactly right. git revert is the go-to for undoing shared commits because it preserves the full history everyone else already has.",
        "roast": "git reset --hard + force push would rewrite history that your teammates already have — that breaks their repositories."
    },
    {
        "q": "You are halfway through a feature when an urgent bug is reported on 'main'. You cannot commit unfinished code. What do you do?",
        "options": [
            "A) git stash  — to save your current work temporarily",
            "B) git commit -m 'WIP do not review'  and push to main",
            "C) Copy all files to a backup folder manually",
            "D) git checkout main -f  which discards all your in-progress changes"
        ],
        "ans": "A",
        "tip": "git stash shelves your uncommitted changes and gives you a clean working tree so you can safely switch branches.",
        "praise": "Perfect. git stash is exactly the tool for this — your work is saved, your workspace is clean, and you can fix the bug.",
        "roast": "git stash is the right answer. It saves your in-progress work without committing it, so you can switch branches cleanly."
    },
    {
        "q": "How do you cherry-pick commits from commit A through commit B inclusive?",
        "options": [
            "A) git cherry-pick A..B",
            "B) git cherry-pick A^..B",
            "C) git cherry-pick --range A B",
            "D) git cherry-pick A B  (listing both SHA IDs separated by a space)"
        ],
        "ans": "B",
        "tip": "In Git range syntax, A..B excludes A itself. Using A^..B (caret before A) includes commit A in the range.",
        "praise": "Correct! The caret ^ is the key detail here. Without it you'd miss the first commit in the range.",
        "roast": "Close! A..B actually excludes commit A. You need A^..B so the range starts from A and goes through B inclusive."
    },
    {
        "q": "What does this command output? → git log --author=\"Alice\" --since=\"2024-01-01\"",
        "options": [
            "A) All commits across the entire repository regardless of author or date",
            "B) Deletes all of Alice's commits made after Jan 1, 2024",
            "C) Shows only commits made by Alice since January 1, 2024",
            "D) Changes the author of recent commits to Alice"
        ],
        "ans": "C",
        "tip": "git log supports powerful filters: --author filters by contributor, --since filters by date. Very useful for auditing or reviewing.",
        "praise": "Correct. This is a commonly used combination for reviewing a team member's recent contributions.",
        "roast": "git log only reads and displays history — it never modifies commits. --author and --since are filters that narrow down what is shown."
    },
    {
        "q": "What is the difference between a lightweight tag and an annotated tag?",
        "options": [
            "A) There is no functional difference — it is just a naming preference.",
            "B) Lightweight tags are simple commit pointers; annotated tags store author, date, and a message.",
            "C) Annotated tags can only be pushed to private repositories.",
            "D) Lightweight tags expire after 30 days."
        ],
        "ans": "B",
        "tip": "Use lightweight tags for temporary bookmarks. Use annotated tags (git tag -a) for official releases — they carry full metadata.",
        "praise": "Exactly right. For software releases, annotated tags are the standard because they include context about who tagged and why.",
        "roast": "Lightweight tags are essentially just named pointers to a commit. Annotated tags (-a flag) store a full object with author, date, and message."
    },
    {
        "q": "You are on branch 'feature'. Running 'git merge main' does what?",
        "options": [
            "A) Pushes your feature branch commits to main",
            "B) Deletes your feature branch",
            "C) Brings the latest commits from main into your current feature branch",
            "D) Resets your feature branch to match main exactly"
        ],
        "ans": "C",
        "tip": "Merge direction matters: you're ON feature, merging FROM main. So main's changes come INTO feature — keeping feature up to date.",
        "praise": "Correct. This is a common workflow — keeping your feature branch updated with what others have merged into main.",
        "roast": "The merge target is always your CURRENT branch. Since you're on feature, main's commits flow INTO feature, not the other way around."
    },
    {
        "q": "What is the primary role of the Git staging area (also known as the 'index')?",
        "options": [
            "A) It is a temporary cache that gets wiped when you restart your terminal.",
            "B) An intermediate holding area where you prepare and curate exactly what changes go into the next commit.",
            "C) A cloud backup hosted on GitHub servers.",
            "D) A folder where Git stores deleted files."
        ],
        "ans": "B",
        "tip": "The staging area lets you split your working changes into clean, focused commits rather than saving everything at once.",
        "praise": "Exactly right! The staging area gives you surgical control over what goes into each snapshot.",
        "roast": "The staging area (index) is where Git holds changes that are queued up for the next commit (via git add)."
    },
    {
        "q": "What does 'HEAD' represent in a Git repository?",
        "options": [
            "A) The very first commit ever made when the repo was created.",
            "B) The server address of the remote repository on GitHub.",
            "C) A pointer to the current active branch or commit you are currently looking at.",
            "D) The user account currently logged into Git."
        ],
        "ans": "C",
        "tip": "HEAD is your current location marker in Git. When you switch branches or check out a commit, HEAD moves with you.",
        "praise": "Spot on! HEAD is essentially Git's 'You are here' bookmark.",
        "roast": "HEAD points to your current checkout location — usually the tip of your active branch."
    },
    {
        "q": "What does it mean when Git says you are in a 'detached HEAD' state?",
        "options": [
            "A) You have checked out a specific commit or tag directly, rather than a named branch.",
            "B) Your Git configuration file has been deleted.",
            "C) The remote repository has lost internet connection.",
            "D) Your computer does not have permission to commit."
        ],
        "ans": "A",
        "tip": "In detached HEAD, commits you make aren't attached to any branch. To keep them, create a branch: git switch -c new-branch.",
        "praise": "Correct! Detached HEAD happens when you checkout a specific commit SHA or tag. Create a branch to save new work.",
        "roast": "Detached HEAD just means HEAD points directly to a commit SHA rather than to a branch name."
    },
    {
        "q": "What is the key difference between 'git merge' and 'git rebase'?",
        "options": [
            "A) merge only works on Windows; rebase only works on Linux.",
            "B) merge preserves original history with a merge commit; rebase rewrites commits linearly on top of the target branch.",
            "C) merge deletes the source branch; rebase keeps both branches untouched.",
            "D) There is no difference; they are exact synonyms."
        ],
        "ans": "B",
        "tip": "Rebase produces a clean linear commit graph, but rewrites commit SHAs. Never rebase public shared branches!",
        "praise": "Clean, accurate explanation! Rebase creates a linear history by re-applying commits atop the target branch.",
        "roast": "Merge ties branches together with a merge commit; rebase re-plays your branch's commits on top of the other branch."
    },
    {
        "q": "What do the markers '<<<<<<<', '=======', and '>>>>>>>' inside a file indicate?",
        "options": [
            "A) Syntax errors generated by the Python interpreter.",
            "B) Merge conflict markers inserted by Git showing conflicting changes from two branches.",
            "C) Markdown formatting for block quotes and tables.",
            "D) Git security certificates for encrypted commits."
        ],
        "ans": "B",
        "tip": "When a merge conflict occurs, Git inserts these markers so you can manually inspect both versions and choose the right code.",
        "praise": "Correct! These are Git's conflict markers. Edit the code, remove the markers, stage, and commit to resolve.",
        "roast": "Those are merge conflict markers! Code between <<<<<<< and ======= is yours; code between ======= and >>>>>>> is theirs."
    },
    {
        "q": "What does running 'git commit --amend' allow you to do?",
        "options": [
            "A) Delete the entire commit history and restart.",
            "B) Combine all branches into one single branch.",
            "C) Update the most recent commit by adding staged changes or editing the commit message.",
            "D) Push commits directly to production without code review."
        ],
        "ans": "C",
        "tip": "Amend is great for fixing typos or adding a forgotten file to your latest local commit before pushing.",
        "praise": "Perfect. git commit --amend replaces the tip of your branch with a revised commit containing your updates.",
        "roast": "git commit --amend modifies your most recent commit — perfect for catching a forgotten file or fixing a typo."
    },
    {
        "q": "What is 'git bisect' primarily used for?",
        "options": [
            "A) Using binary search across commit history to quickly find the exact commit that introduced a bug.",
            "B) Splitting a single large commit into two equal halves.",
            "C) Converting a Git repository into a Subversion (SVN) repository.",
            "D) Compressing git files to save disk space."
        ],
        "ans": "A",
        "tip": "git bisect cuts debugging time from hours to minutes by automating binary search between a known good and bad commit.",
        "praise": "Senior-level Git knowledge! git bisect is one of Git's most potent debugging superpowers.",
        "roast": "git bisect uses binary search through history to isolate which commit caused a bug."
    },
    {
        "q": "Why is running 'git push --force' dangerous on shared branches like 'main'?",
        "options": [
            "A) It permanently disables GitHub Actions CI/CD pipelines.",
            "B) It costs money per forced gigabyte on cloud hosts.",
            "C) It overwrites remote history, potentially erasing teammates' pushed commits and corrupting their local trees.",
            "D) It converts all LF line endings to CRLF automatically."
        ],
        "ans": "C",
        "tip": "Force pushing replaces remote history with your local history. If teammates pushed work in between, their work is wiped out.",
        "praise": "Exactly right. Use --force-with-lease if you ever must force-push, and never do it on shared branches!",
        "roast": "Force push overwrites remote history. If teammates pulled or pushed in between, you risk deleting their work."
    }
]

DISASTER_SCENARIOS = [
    {
        "title": "You committed directly to main instead of your feature branch",
        "story": "You were heads-down coding and forgot to switch branches. You just ran\n  'git commit -m \"add payment feature\"' — and the commit landed on main.\n  Your team has a rule: no direct commits to main.",
        "prompt": "You haven't pushed yet. What is the cleanest way to move that commit to your feature branch and undo it on main?",
        "choices": [
            "git checkout feature && git cherry-pick main && git checkout main && git reset --hard HEAD~1",
            "git reset --hard HEAD~1  (just delete the commit on main, losing your work)",
            "git push -f origin main  (force push and hope nobody notices)",
            "git revert HEAD  (create an undo commit on main, then manually copy code to feature)"
        ],
        "ans_idx": 1,
        "reaction": "Correct! Cherry-pick moves the commit to feature, then reset --hard removes it from main cleanly — since it hasn't been pushed, rewriting local history is safe here."
    },
    {
        "title": "You accidentally staged your .env file (it has real API keys)",
        "story": "You ran 'git add .' and then noticed '.env' is now staged.\n  It contains your database password and API tokens. It has NOT been committed yet.\n  You need to unstage it without losing the file.",
        "prompt": "Which command removes '.env' from the staging area but keeps the file on disk?",
        "choices": [
            "rm -f .env  (deletes the file entirely — worst option)",
            "git restore --staged .env",
            "git commit -m 'oops'  (commits it anyway)",
            "git push origin main  (uploads the secret to GitHub)"
        ],
        "ans_idx": 2,
        "reaction": "Correct! git restore --staged removes the file from staging without touching it on disk. Next step: add .env to your .gitignore file!"
    },
    {
        "title": "You ran 'git reset --hard' and your last 3 commits seem gone",
        "story": "You ran 'git reset --hard HEAD~3' trying to undo 3 commits.\n  But you actually needed those commits — they had a week of work.\n  'git log' doesn't show them anymore. Panic sets in.",
        "prompt": "Which Git tool records every movement of HEAD and can recover the lost commit SHA?",
        "choices": [
            "git log  (only shows the current reachable history — the commits are gone from here)",
            "git status  (shows working directory state, not lost commits)",
            "git reflog  (records all HEAD movements including resets — your commits are still here)",
            "git stash list  (shows stashed changes, not reset commits)"
        ],
        "ans_idx": 3,
        "reaction": "Correct! git reflog is your safety net. Run it, find the SHA of your lost commit, then run 'git reset --hard <that-SHA>' to recover everything."
    },
    {
        "title": "Merge conflict in server.py halts your work",
        "story": "You ran 'git merge feature' into 'main'. Git stopped with:\n  'CONFLICT (content): Merge conflict in server.py. Automatic merge failed.'\n  Git placed conflict markers inside server.py.",
        "prompt": "After opening server.py, choosing the right code, and removing the conflict markers, what do you run to finish?",
        "choices": [
            "git add server.py && git commit -m \"resolve merge conflict\"",
            "git reset --hard  (aborts the merge and discards all progress)",
            "git push origin main  (pushes the conflict markers to production)",
            "rm server.py  (deletes the conflicting file)"
        ],
        "ans_idx": 1,
        "reaction": "Correct! Once conflict markers are resolved manually, staging the resolved file with 'git add' and running 'git commit' concludes the merge cleanly."
    },
    {
        "title": "Accidentally committed a 500MB dataset zip file locally",
        "story": "You just ran 'git commit -m \"add data\"' and realized you accidentally included a 500MB 'archive.zip'!\n  GitHub rejects any push containing files over 100MB. You haven't pushed yet.",
        "prompt": "How do you remove archive.zip from the latest commit while keeping the file on your local disk?",
        "choices": [
            "git rm --cached archive.zip && git commit --amend --no-edit",
            "git push --force origin main  (attempt to force upload the 500MB file)",
            "git revert HEAD  (revert creates a new commit but keeps the 500MB file in Git history)",
            "Delete your entire repository folder from your laptop"
        ],
        "ans_idx": 1,
        "reaction": "Correct! 'git rm --cached' unstages the file without deleting it from disk, and '--amend' rewires the latest commit so the giant file is never saved in Git history."
    }
]

LAB_EXPERIMENTS = [
    ("Step 01", "Setting Up and Basic Commands", "git init\necho 'Hello' > file.txt\ngit add file.txt\ngit commit -m 'Initial commit'"),
    ("Step 02", "Creating and Managing Branches", "git checkout -b feature-branch\n# make changes\ngit checkout master\ngit merge feature-branch"),
    ("Step 03", "Stashing Changes", "git stash save 'WIP'\ngit checkout master\n# do urgent work\ngit checkout feature-branch\ngit stash apply"),
    ("Step 04", "Cloning a Remote Repository", "git clone https://github.com/user/repo.git"),
    ("Step 05", "Fetch and Rebase", "git checkout main\ngit fetch origin\ngit rebase origin/main"),
    ("Step 06", "Merge with Custom Commit Message", "git checkout master\ngit merge feature-branch -m 'Custom merge message'"),
    ("Step 07", "Git Tags and Releases", "git tag v1.0\n# or annotated:\ngit tag -a v1.0 -m 'Release v1.0'"),
    ("Step 08", "Cherry-Picking a Range of Commits", "git cherry-pick start_commit^..end_commit"),
    ("Step 09", "Inspecting a Specific Commit", "git show <commit-id>\n# or summary only:\ngit log -n 1 <commit-id>"),
    ("Step 10", "Filtering by Author and Date Range", "git log --author='JohnDoe' --since='2023-01-01' --until='2023-12-31'"),
    ("Step 11", "Display Last 5 Commits", "git log -n 5 --oneline"),
    ("Step 12", "Undoing Changes via Revert", "git revert <commit-id> --no-edit")
]

# ----------------- GAME MODES -----------------

def mode_viva_gauntlet():
    clear_screen()
    print(f"{Color.CYAN}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
    print("║        🎓 MODE 1: SURVIVE THE TECH INTERVIEW & VIVA GAUNTLET       ║")
    print("╚════════════════════════════════════════════════════════════════════╝\n")
    print_slow("A lead interviewer walks into the room with a notepad, a hot cup of coffee, and zero patience.", 0.02, Color.YELLOW)
    print_slow("Answer the questions correctly to earn your developer cred. You have 3 lives (☕ Coffee Cups).\n", 0.02)
    
    score = 0
    lives = 3
    questions = list(VIVA_QUESTIONS)
    random.shuffle(questions)

    total_viva = min(10, len(questions))
    for i, item in enumerate(questions[:total_viva], 1):
        print(f"\n{Color.BOLD}{Color.WHITE}─── QUESTION {i}/{total_viva} | Lives: {'☕ ' * lives} | Score: {score} ───{Color.RESET}")
        print_slow(f"\n{Color.CYAN}{item['q']}{Color.RESET}", 0.015)
        print()
        for opt in item["options"]:
            print(f"  {Color.YELLOW}{opt}{Color.RESET}")
        
        while True:
            choice = input(f"\n{Color.BOLD}Your Answer [A / B / C / D] (or '0' for Menu): {Color.RESET}").strip().upper()
            if choice in ["0", "MENU", "HOME", "Q", "EXIT"]:
                print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
                time.sleep(0.5)
                return
            if choice in ["A", "B", "C", "D"]:
                break
            print(f"{Color.RED}Please type A, B, C, or D (or '0' for Menu)!{Color.RESET}")

        if choice == item["ans"]:
            score += 100
            print(f"\n{Color.GREEN}{Color.BOLD}🎉 CORRECT! (+100 pts){Color.RESET}")
            print(f"{Color.GREEN}{item['praise']}{Color.RESET}")
        else:
            lives -= 1
            print(f"\n{Color.RED}{Color.BOLD}❌ WRONG! Correct Answer was ({item['ans']}){Color.RESET}")
            print(f"{Color.RED}{item['roast']}{Color.RESET}")
            if lives == 0:
                print_slow(f"\n{Color.RED}{Color.BOLD}💀 OUT OF LIVES! The interview is cut short. Time to read GIT_COMMANDS.md!{Color.RESET}", 0.03)
                break
        
        print(f"{Color.DIM}💡 Tip: {item['tip']}{Color.RESET}")
        time.sleep(1.2)

    max_viva = total_viva * 100
    print(f"\n{Color.BOLD}{Color.MAGENTA}═══════════════════════════════════════════════════")
    print(f"   CHALLENGE FINISHED! Final Score: {score}/{max_viva}")
    if score >= max_viva * 0.8:
        print(f"   🏆 Rank: Git Master! Ready for senior engineering!")
    elif score >= max_viva * 0.5:
        print(f"   ⭐ Rank: Solid Developer! You survived with confidence!")
    else:
        print(f"   🌱 Rank: Apprentice. Check GIT_COMMANDS.md and try again!")
    print(f"═══════════════════════════════════════════════════{Color.RESET}\n")
    input(f"{Color.DIM}Press Enter to return to main menu...{Color.RESET}")

def mode_disaster_recovery():
    clear_screen()
    print(f"{Color.RED}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
    print("║           🚨 MODE: REAL-WORLD GIT PROBLEM SOLVER                   ║")
    print("╚════════════════════════════════════════════════════════════════════╝\n")
    print_slow("These are problems that actually happen to developers every day.", 0.015, Color.CYAN)
    print_slow("Read the situation carefully and pick the right Git command to fix it.\n", 0.015)

    score = 0
    total_scenarios = len(DISASTER_SCENARIOS)
    for i, scenario in enumerate(DISASTER_SCENARIOS, 1):
        clear_screen()
        print(f"{Color.RED}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
        print("║           🚨 MODE: REAL-WORLD GIT PROBLEM SOLVER                   ║")
        print(f"╚════════════════════════════════════════════════════════════════════╝\n")
        print(f"{Color.BOLD}{Color.YELLOW}── SCENARIO {i}/{total_scenarios} ──────────────────────────────────────────────────{Color.RESET}")
        print(f"\n{Color.BOLD}{Color.WHITE}{scenario['title']}{Color.RESET}\n")
        print_slow(scenario['story'], 0.013, Color.WHITE)
        print(f"\n{Color.CYAN}{Color.BOLD}What do you do?{Color.RESET}\n  {scenario['prompt']}\n")

        for idx, ch in enumerate(scenario["choices"], 1):
            print(f"  {Color.YELLOW}[{idx}]{Color.RESET} {ch}")

        while True:
            raw_pick = input(f"\n{Color.BOLD}Your answer [1 - {len(scenario['choices'])}] (or '0' for Menu): {Color.RESET}").strip().lower()
            if raw_pick in ["0", "menu", "home", "q", "exit"]:
                print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
                time.sleep(0.5)
                return
            try:
                pick = int(raw_pick)
                if 1 <= pick <= len(scenario["choices"]):
                    break
            except ValueError:
                pass
            print(f"{Color.RED}Enter a number from 1 to {len(scenario['choices'])} (or '0' for Menu).{Color.RESET}")

        if pick == scenario["ans_idx"]:
            score += 150
            print(f"\n{Color.GREEN}{Color.BOLD}✅ Correct! (+150 pts){Color.RESET}")
            print(f"{Color.GREEN}{scenario['reaction']}{Color.RESET}\n")
        else:
            correct_choice = scenario["choices"][scenario["ans_idx"] - 1]
            print(f"\n{Color.RED}{Color.BOLD}❌ Not quite. The right answer was [{scenario['ans_idx']}]:{Color.RESET}")
            print(f"   {Color.WHITE}{correct_choice}{Color.RESET}")
            print(f"\n{Color.DIM}{scenario['reaction']}{Color.RESET}\n")
        time.sleep(1.5)

    max_scenarios = total_scenarios * 150
    print(f"\n{Color.BOLD}{Color.MAGENTA}═══════════════════════════════════════════════════")
    print(f"   Problem Solver Complete! Score: {score}/{max_scenarios}")
    if score >= max_scenarios * 0.8:
        print(f"   ✅ Excellent! You handle real Git emergencies with confidence.")
    elif score >= max_scenarios * 0.5:
        print(f"   👍 Good job! Review the ones you missed to build confidence.")
    else:
        print(f"   📖 Check the GIT_COMMANDS.md cheatsheet to review these scenarios.")
    print(f"═══════════════════════════════════════════════════{Color.RESET}\n")
    input(f"{Color.DIM}Press Enter to return to main menu...{Color.RESET}")

def mode_vtu_cheatbook():
    clear_screen()
    print(f"{Color.GREEN}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
    print("║          📚 MODE 3: 12-STEP PRACTICAL LAB & WORKFLOW CHEATBOOK      ║")
    print("╚════════════════════════════════════════════════════════════════════╝\n")
    print("Select any step to view the exact problem, commands & output:\n")

    for idx, (step_code, name, _) in enumerate(LAB_EXPERIMENTS, 1):
        print(f"  {Color.YELLOW}[{idx:2d}] {step_code}: {name}{Color.RESET}")

    print(f"\n  {Color.CYAN}[ 0] Return to Main Menu{Color.RESET}")

    while True:
        try:
            choice = int(input(f"\n{Color.BOLD}Enter Step [1 - 12] or 0 to exit: {Color.RESET}").strip())
            if choice == 0:
                return
            if 1 <= choice <= 12:
                step_code, name, code = LAB_EXPERIMENTS[choice - 1]
                print(f"\n{Color.GREEN}{Color.BOLD}═════════════════════════════════════════════════════")
                print(f"📖 {step_code}: {name}")
                print(f"═════════════════════════════════════════════════════{Color.RESET}")
                print(f"{Color.WHITE}{code}{Color.RESET}")
                print(f"{Color.GREEN}═════════════════════════════════════════════════════{Color.RESET}")
        except ValueError:
            pass

def _gfh_pause(label="Continue"):
    """Helper: press Enter to proceed, or type 0 to go back to menu."""
    s = input(f"\n{Color.DIM}[ Press Enter to {label}, or type '0' to return to Menu ]{Color.RESET} ").strip().lower()
    return s not in ["0", "menu", "q", "exit"]

def mode_git_for_humans():
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
    print("║              🐣  GIT FOR HUMANS — THE COMPLETE GUIDE               ║")
    print("╚════════════════════════════════════════════════════════════════════╝\n")
    print_slow("Never used Git before? Good. This guide walks you through everything.", 0.013, Color.CYAN)
    print_slow("Read every part. By the end you'll understand Git well enough to actually use it.\n", 0.013)
    print(f"  {Color.DIM}10 parts + a final quiz. Type '0' at any [Enter] prompt to go back to menu.{Color.RESET}\n")
    if not _gfh_pause("start Part 1"): return

    # ─── PART 1 ───────────────────────────────────────────────────────────────
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}── PART 1 / 10 : Why Does Git Exist? ───────────────────────────────{Color.RESET}\n")
    print_slow("Everyone has done this at some point:", 0.013)
    print(f"""
  📄 report.docx
  📄 report_v2.docx
  📄 report_FINAL.docx
  📄 report_FINAL_actual.docx
  📄 report_USE_THIS_ONE_FOR_REAL.docx
""")
    print_slow("That is called manual version control.", 0.013)
    print_slow("You're making a new copy every time you're scared to overwrite your old work.", 0.013)
    print_slow("It works for a while, but it breaks down fast:\n", 0.013)
    print(f"  • Which file is actually the latest?\n  • What changed between v2 and FINAL?\n  • How do you undo just one specific change from 3 days ago?\n  • How do two people work on the same file simultaneously?\n")
    print_slow("Git solves ALL of this — automatically, cleanly, and without duplicate files.", 0.013, Color.GREEN)
    print_slow("Your project stays in ONE folder. Git tracks every single change inside it.", 0.013, Color.GREEN)
    if not _gfh_pause("Part 2"): return

    # ─── PART 2 ───────────────────────────────────────────────────────────────
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}── PART 2 / 10 : What Git Actually Is ──────────────────────────────{Color.RESET}\n")
    print_slow("Git is a version control system. That means it tracks changes to files over time.", 0.013)
    print_slow("Think of it as a detailed timeline of your project:\n", 0.013)
    print(f"""  {Color.DIM}── Jan 10 ──► Jan 11 ──► Jan 12 ──► Jan 15 ──► today{Color.RESET}
       |          |          |          |          |
    "init"    "added     "fixed    "added     "updated
              login"     bug"     signup"    README"
""")
    print_slow("Each point on that timeline is called a commit.", 0.013, Color.CYAN)
    print_slow("You can go back to any commit at any time. Nothing is ever truly lost.\n", 0.013)
    print_slow("Git runs locally on your machine. GitHub is a website that hosts your Git history online", 0.013)
    print_slow("— it's a backup and sharing platform. Git ≠ GitHub. Git is the tool, GitHub is the cloud.\n", 0.013, Color.WHITE)
    if not _gfh_pause("Part 3"): return

    # ─── PART 3 ───────────────────────────────────────────────────────────────
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}── PART 3 / 10 : The 5 Commands That Cover 80% of Daily Git ────────{Color.RESET}\n")
    print_slow("You don't need to memorize everything. Start with these five:\n", 0.013)
    print(f"  {Color.GREEN}{Color.BOLD}git init{Color.RESET}        — Start tracking a folder with Git. Run this once per project.")
    print(f"  {Color.GREEN}{Color.BOLD}git add .{Color.RESET}       — Stage all changed files (select what goes in the next snapshot).")
    print(f"  {Color.GREEN}{Color.BOLD}git commit -m{Color.RESET}   — Save a snapshot with a message. e.g. git commit -m \"add login form\"")
    print(f"  {Color.GREEN}{Color.BOLD}git push{Color.RESET}        — Upload your commits to GitHub (backup + share with team).")
    print(f"  {Color.GREEN}{Color.BOLD}git pull{Color.RESET}        — Download your teammate's latest commits from GitHub.\n")
    print_slow("That's it for the basics. Everything else in Git is built on top of these.", 0.013, Color.WHITE)
    print_slow("\nThe typical daily workflow looks like this:\n", 0.013)
    print(f"  1. Edit your files")
    print(f"  2. {Color.GREEN}git add .{Color.RESET}                       ← stage everything changed")
    print(f"  3. {Color.GREEN}git commit -m \"what you did\"{Color.RESET}    ← save a snapshot")
    print(f"  4. {Color.GREEN}git push{Color.RESET}                        ← upload to GitHub")
    print(f"  5. Next day: {Color.GREEN}git pull{Color.RESET}              ← get teammate changes first\n")
    if not _gfh_pause("Part 4"): return

    # ─── PART 4 ───────────────────────────────────────────────────────────────
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}── PART 4 / 10 : Understanding What Changed ─────────────────────────{Color.RESET}\n")
    print_slow("Before committing, you can inspect what changed.\n", 0.013)
    print(f"  {Color.CYAN}git status{Color.RESET}         — Shows which files are changed, staged, or untracked.")
    print(f"                       Red  = changed but NOT yet staged")
    print(f"                       Green = staged and ready to commit\n")
    print(f"  {Color.CYAN}git diff{Color.RESET}           — Shows the EXACT lines that changed in unstaged files.")
    print(f"                       Lines starting with + are additions.")
    print(f"                       Lines starting with - are deletions.\n")
    print(f"  {Color.CYAN}git diff --staged{Color.RESET}  — Shows the diff for files that ARE staged (after git add).\n")
    print_slow("Good habit: always run 'git status' and 'git diff' before committing.", 0.013, Color.GREEN)
    print_slow("Never commit blindly. Know exactly what you're saving.", 0.013, Color.GREEN)
    if not _gfh_pause("Part 5"): return

    # ─── PART 5 ───────────────────────────────────────────────────────────────
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}── PART 5 / 10 : Branching — Working Safely ────────────────────────{Color.RESET}\n")
    print_slow("Problem: your app works perfectly on 'main'. You want to add a search feature.", 0.013)
    print_slow("If you code directly on main and break something, the working version is gone.\n", 0.013, Color.RED)
    print_slow("Solution: branches.\n", 0.013, Color.GREEN)
    print(f"  A branch is an independent copy of your code where you can work freely.")
    print(f"  When the feature is done and tested, you merge it back into main.\n")
    print(f"  {Color.CYAN}git checkout -b search-feature{Color.RESET}   ← create new branch + switch to it")
    print(f"  {Color.DIM}... write code, commit as usual ...{Color.RESET}")
    print(f"  {Color.CYAN}git checkout main{Color.RESET}                ← go back to main")
    print(f"  {Color.CYAN}git merge search-feature{Color.RESET}         ← bring search-feature code into main\n")
    print_slow("The key point: main was untouched the entire time you were building.", 0.013, Color.WHITE)
    print_slow("If the feature was bad, just delete the branch. Zero damage to main.", 0.013)
    print(f"\n  {Color.CYAN}git branch{Color.RESET}            ← list all branches")
    print(f"  {Color.CYAN}git branch -d feature{Color.RESET}  ← delete a merged branch\n")
    if not _gfh_pause("Part 6"): return

    # ─── PART 6 ───────────────────────────────────────────────────────────────
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}── PART 6 / 10 : Working With Teammates ────────────────────────────{Color.RESET}\n")
    print_slow("Git becomes very powerful when multiple people work on the same project.\n", 0.013)
    print(f"  {Color.CYAN}git clone <url>{Color.RESET}       — Download an entire repository from GitHub to your machine.")
    print(f"                         You only do this once per project.\n")
    print(f"  {Color.CYAN}git fetch origin{Color.RESET}      — Check what your teammates pushed WITHOUT merging it in.")
    print(f"                         Safe to run any time — doesn't affect your code.\n")
    print(f"  {Color.CYAN}git pull{Color.RESET}              — Download AND merge teammate commits into your current branch.")
    print(f"                         Do this every morning before starting work.\n")
    print(f"  {Color.CYAN}git push origin main{Color.RESET}  — Upload your commits to the shared remote.\n")
    print_slow("Common team workflow:\n", 0.013)
    print(f"  1. {Color.GREEN}git pull{Color.RESET}                     ← get latest before you start")
    print(f"  2. Create a branch, do your work, commit")
    print(f"  3. {Color.GREEN}git push origin your-branch{Color.RESET}  ← push your branch")
    print(f"  4. Open a Pull Request on GitHub for teammates to review")
    print(f"  5. After approval, merge it into main\n")
    print_slow("This workflow prevents conflicts and keeps everyone in sync.", 0.013, Color.WHITE)
    if not _gfh_pause("Part 7"): return

    # ─── PART 7 ───────────────────────────────────────────────────────────────
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}── PART 7 / 10 : Undoing Mistakes ──────────────────────────────────{Color.RESET}\n")
    print_slow("Everyone makes mistakes. Git almost always lets you undo them.\n", 0.013)
    print(f"  {Color.CYAN}Scenario 1: You committed something wrong (not pushed yet){Color.RESET}")
    print(f"  → {Color.GREEN}git reset --soft HEAD~1{Color.RESET}   ← undo the commit, keep changes staged")
    print(f"  → {Color.GREEN}git reset HEAD~1{Color.RESET}          ← undo commit, unstage changes (keep files)\n")
    print(f"  {Color.CYAN}Scenario 2: You committed wrong (already pushed to shared branch){Color.RESET}")
    print(f"  → {Color.GREEN}git revert <commit-id>{Color.RESET}    ← creates a NEW commit that undoes it")
    print(f"     Safe for shared branches — doesn't rewrite history\n")
    print(f"  {Color.CYAN}Scenario 3: You have unfinished work but need to switch branches{Color.RESET}")
    print(f"  → {Color.GREEN}git stash{Color.RESET}                 ← temporarily shelves your changes")
    print(f"  → {Color.GREEN}git stash pop{Color.RESET}             ← brings them back when you're ready\n")
    print(f"  {Color.CYAN}Scenario 4: You forgot to include a file in your last commit{Color.RESET}")
    print(f"  → {Color.GREEN}git add forgotten-file.txt{Color.RESET}")
    print(f"  → {Color.GREEN}git commit --amend --no-edit{Color.RESET}  ← adds it to the previous commit\n")
    print_slow("Rule of thumb: if the commit was pushed, use revert. If not, use reset.", 0.013, Color.YELLOW)
    if not _gfh_pause("Part 8"): return

    # ─── PART 8 ───────────────────────────────────────────────────────────────
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}── PART 8 / 10 : Reading Project History ───────────────────────────{Color.RESET}\n")
    print_slow("Git stores the full history of everything. Here's how to read it:\n", 0.013)
    print(f"  {Color.CYAN}git log{Color.RESET}                       — Full commit history (newest first)")
    print(f"  {Color.CYAN}git log --oneline{Color.RESET}             — Compact one-line-per-commit view")
    print(f"  {Color.CYAN}git log -n 5{Color.RESET}                  — Show only the last 5 commits")
    print(f"  {Color.CYAN}git log --author=\"Prajwal\"{Color.RESET}    — Filter by who made the commit")
    print(f"  {Color.CYAN}git log --since=\"2024-01-01\"{Color.RESET}  — Filter by date\n")
    print(f"  {Color.CYAN}git show <commit-id>{Color.RESET}          — See exactly what changed in one commit")
    print(f"  {Color.CYAN}git diff main..feature{Color.RESET}        — See all differences between two branches\n")
    print_slow("Every commit has a unique ID (called a SHA) that looks like: a3f9c12", 0.013)
    print_slow("You can use those IDs to refer to specific commits in other commands.\n", 0.013)
    print(f"  {Color.GREEN}git reflog{Color.RESET}  — The ultimate safety net: shows every HEAD movement.")
    print(f"              Even if commits look 'gone' after a reset, reflog shows them.\n")
    if not _gfh_pause("Part 9"): return

    # ─── PART 9 ───────────────────────────────────────────────────────────────
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}── PART 9 / 10 : Good Habits That Save You Later ───────────────────{Color.RESET}\n")
    print_slow("These habits take 10 seconds each but save hours of debugging:\n", 0.013)
    print(f"  {Color.GREEN}1. Write clear commit messages{Color.RESET}")
    print(f"     Bad:  git commit -m \"stuff\"")
    print(f"     Bad:  git commit -m \"fix\"")
    print(f"     Good: git commit -m \"fix: prevent crash when user submits empty form\"\n")
    print(f"  {Color.GREEN}2. Create a .gitignore file{Color.RESET}")
    print(f"     This tells Git which files to NEVER track:")
    print(f"     → .env  (passwords and API keys — NEVER commit these)")
    print(f"     → node_modules/  (auto-generated, huge, should be rebuilt from package.json)")
    print(f"     → __pycache__/   (Python build files)\n")
    print(f"  {Color.GREEN}3. Commit small and often{Color.RESET}")
    print(f"     One logical change per commit. Not 'everything I did in 3 days'.")
    print(f"     Small commits are easy to review, revert, and understand.\n")
    print(f"  {Color.GREEN}4. Never commit directly to main on a team project{Color.RESET}")
    print(f"     Always use a branch. Even for a one-line fix.\n")
    print(f"  {Color.GREEN}5. Pull before you push{Color.RESET}")
    print(f"     Always run git pull before git push to avoid conflicts.\n")
    if not _gfh_pause("the final quiz"): return

    # ─── PART 10: QUIZ ───────────────────────────────────────────────────────
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}── PART 10 / 10 : Final Quiz — 7 Questions ─────────────────────────{Color.RESET}\n")
    print_slow("Answer these based on what you just read. No tricks — just checking you got it.\n", 0.013)

    quiz = [
        {
            "q": "1. You're on a team and your app is working. You want to add a new feature safely.\n   What should you do FIRST?",
            "opts": ["A) Start editing files directly on main", "B) Create a new branch for the feature", "C) Fork the entire repository"],
            "ans": "B",
            "explain": "Always branch before feature work. Main stays safe while you build on the branch."
        },
        {
            "q": "2. You edited 4 files. You only want to include 'login.js' in this commit. What do you run?",
            "opts": ["A) git add .", "B) git commit login.js", "C) git add login.js"],
            "ans": "C",
            "explain": "git add <filename> stages just that one file. 'git add .' would stage all 4 files."
        },
        {
            "q": "3. You committed a bug and your teammates already pulled it. What is the safe way to undo it?",
            "opts": ["A) git reset --hard HEAD~1 then force push", "B) git revert <commit-id>", "C) Delete the repository"],
            "ans": "B",
            "explain": "git revert creates a new undo commit. It never rewrites history that teammates already have."
        },
        {
            "q": "4. You're halfway through writing code when an urgent bug appears on main.\n   You can't commit yet. What do you do?",
            "opts": ["A) git stash to temporarily save your work", "B) git commit -m 'WIP' to main", "C) Copy files to Desktop manually"],
            "ans": "A",
            "explain": "git stash shelves your changes cleanly. Run git stash pop to get them back later."
        },
        {
            "q": "5. What is the difference between git fetch and git pull?",
            "opts": [
                "A) They do the same thing",
                "B) git fetch downloads but doesn't merge; git pull downloads AND merges",
                "C) git pull is for GitHub only; git fetch works everywhere"
            ],
            "ans": "B",
            "explain": "git fetch is safe — it updates remote tracking without touching your local branch. git pull = fetch + merge."
        },
        {
            "q": "6. You ran 'git reset --hard HEAD~3' by accident and your commits look gone.\n   Which command can still find them?",
            "opts": ["A) git log", "B) git status", "C) git reflog"],
            "ans": "C",
            "explain": "git reflog records every HEAD movement including resets. Your commits are still there — find their SHA and reset back to it."
        },
        {
            "q": "7. Which file tells Git which files to never track?",
            "opts": ["A) .gitconfig", "B) .gitignore", "C) .gitkeep"],
            "ans": "B",
            "explain": ".gitignore lists patterns of files Git should skip — like .env, node_modules, __pycache__, etc."
        }
    ]

    h_score = 0
    for item in quiz:
        print(f"{Color.CYAN}{Color.BOLD}{item['q']}{Color.RESET}")
        for opt in item["opts"]:
            print(f"  {opt}")
        choice = input(f"{Color.BOLD}  Your answer [A/B/C] (or '0' to exit): {Color.RESET}").strip().upper()
        if choice in ["0", "MENU", "Q", "EXIT"]:
            print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
            return
        if choice == item["ans"]:
            h_score += 1
            print(f"{Color.GREEN}  ✅ Correct! {item['explain']}{Color.RESET}\n")
        else:
            print(f"{Color.RED}  ❌ Not quite. {item['explain']}{Color.RESET}\n")
        time.sleep(0.8)

    clear_screen()
    print(f"{Color.BOLD}{Color.MAGENTA}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║                 GIT FOR HUMANS — COMPLETE                          ║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Color.RESET}\n")
    print(f"  Final Quiz Score: {Color.BOLD}{h_score}/7{Color.RESET}\n")
    if h_score == 7:
        print(f"  {Color.GREEN}✅ Perfect score! You genuinely understand Git. Jump into the Practice Arena next.{Color.RESET}")
    elif h_score >= 5:
        print(f"  {Color.GREEN}👍 Strong result. Re-read the parts you missed, then try the Practice Arena.{Color.RESET}")
    elif h_score >= 3:
        print(f"  {Color.YELLOW}📖 Getting there. Go back through Parts 5–8 and try the quiz again.{Color.RESET}")
    else:
        print(f"  {Color.YELLOW}📖 Take your time — re-read from Part 3 onwards, then come back.{Color.RESET}")
    print(f"\n  {Color.DIM}Next step → Mode 2: Practice Arena (Low difficulty) to type the commands yourself.{Color.RESET}\n")
    input(f"{Color.DIM}Press Enter to return to the main menu...{Color.RESET}")

# ----------------- COMMAND CHALLENGES BY DIFFICULTY (30 TOTAL) -----------------

CHALLENGES_LOW = [
    {
        "concept": "Starting fresh — initializing a repository",
        "situation": "You just created a new folder called 'my-project' for your work.\n  Right now it is a plain folder. Git doesn't know about it yet.\n  You need to tell Git to start tracking this folder.",
        "task": "Run the command that initializes Git in the current folder:",
        "valid": ["git init", "git init ."],
        "hint": "Think of the subcommand used to 'initialize' a repository: git <subcommand>",
        "why": "This creates a hidden '.git' folder inside your project. That's where Git stores all your history."
    },
    {
        "concept": "Checking what has changed",
        "situation": "You edited a file called 'index.html'.\n  Before doing anything else, you want to see what files have changed,\n  which are staged, and which are untracked.",
        "task": "Run the command to see the current state of your working directory:",
        "valid": ["git status", "git st", "git status -s", "git status --short"],
        "hint": "Look for the subcommand that reports working tree 'status' (starts with 's')",
        "why": "git status is the most used Git command. Run it constantly — it always tells you what's going on."
    },
    {
        "concept": "Staging all files before saving",
        "situation": "You edited two files today. You want to include all of them\n  in your next commit. Git doesn't save anything automatically —\n  you have to explicitly select what goes into the next snapshot.",
        "task": "Stage all changed files in the current directory:",
        "valid": ["git add .", "git add -A", "git add --all"],
        "hint": "Use the 'add' subcommand followed by a symbol meaning 'current directory / everything here'",
        "why": "The dot '.' means 'everything here'. git add picks what goes into your next commit."
    },
    {
        "concept": "Staging one specific file only",
        "situation": "You modified 'README.md' and 'app.py'. You only want to stage\n  'README.md' right now so your commit is focused on documentation.",
        "task": "Stage only the file 'README.md':",
        "valid": ["git add README.md"],
        "hint": "Use 'git add' followed by the exact filename you want to stage",
        "why": "Naming a specific file stages only that file, leaving other modified files unstaged."
    },
    {
        "concept": "Saving a snapshot with a message",
        "situation": "You staged your changes. Now you want to permanently save\n  that snapshot with a note describing what you did.\n  The message should be: 'add homepage layout'",
        "task": "Commit your staged files with the message: 'add homepage layout'",
        "valid": [
            'git commit -m "add homepage layout"',
            "git commit -m 'add homepage layout'",
            'git commit -m"add homepage layout"',
            "git commit -m'add homepage layout'"
        ],
        "hint": "Use 'git commit' with the message flag (-m) followed by the message in quotes",
        "why": "Every commit needs a message (-m flag). It describes what changed so you (and your team) can understand the history."
    },
    {
        "concept": "Viewing the commit history",
        "situation": "You've made a few commits over the past few days.\n  You want to see all of them — who made them, when, and what the message said.",
        "task": "Show the full commit history of this repository:",
        "valid": ["git log", "git lg", "git log --oneline", "git log -n 5"],
        "hint": "A 3-letter word meaning record or history log: git <subcommand>",
        "why": "git log lists every commit in reverse order (newest first). Each has a unique ID, author, date, and message."
    },
    {
        "concept": "Viewing compact one-line commit log",
        "situation": "You want to quickly scan past commits without reading multi-line blocks for each one.",
        "task": "Display the commit history with each commit on a single line:",
        "valid": ["git log --oneline", "git lg"],
        "hint": "Add a flag to 'git log' that condenses each commit to a single line: --one...",
        "why": "'--oneline' condenses each commit to its 7-character SHA and commit subject message."
    },
    {
        "concept": "Inspecting line-by-line differences",
        "situation": "You edited 'style.css'. Before staging it, you want to see the exact lines added or removed.",
        "task": "Show the unstaged modifications in your working tree:",
        "valid": ["git diff", "git diff style.css"],
        "hint": "The subcommand name is short for 'differences' (4 letters)",
        "why": "'git diff' shows + (green) for added lines and - (red) for deleted lines in files that haven't been staged yet."
    },
    {
        "concept": "Listing local branches",
        "situation": "You want to check what branches exist in your local repository and see which one you are currently on.",
        "task": "List all local branches in the repository:",
        "valid": ["git branch", "git branch --list"],
        "hint": "Use the command named after tree limbs: git <subcommand>",
        "why": "'git branch' lists all branches, marking the currently checked-out branch with an asterisk (*)."
    },
    {
        "concept": "Checking your installed Git version",
        "situation": "You opened a new terminal and want to quickly verify that Git is installed and see which version is running.",
        "task": "Check the installed Git version:",
        "valid": ["git --version", "git version", "git -v"],
        "hint": "Use the standard double-dash version flag with git: git --v...",
        "why": "Verifies that the Git binary is available on your system PATH."
    }
]

CHALLENGES_MEDIUM = [
    {
        "concept": "Creating and switching to a new branch",
        "situation": "You're on 'main' and want to start building a new 'search' feature.\n  You don't want to work directly on main — you need a separate branch\n  so the working code stays safe while you build.",
        "task": "Create a new branch called 'search-feature' and switch to it in one command:",
        "valid": ["git checkout -b search-feature", "git switch -c search-feature"],
        "hint": "Use 'checkout' with the new-branch flag (-b) or 'switch' with (-c), followed by the branch name",
        "why": "The -b flag creates the branch AND switches to it. (Modern syntax: git switch -c search-feature)."
    },
    {
        "concept": "Switching back to an existing branch",
        "situation": "You're on 'search-feature'. Your team lead just told you to\n  review something on the 'main' branch. You need to switch without losing anything.",
        "task": "Switch to the already-existing branch called 'main':",
        "valid": ["git checkout main", "git switch main"],
        "hint": "Use 'git checkout <branch>' or 'git switch <branch>' (no -b or -c needed for existing branches)",
        "why": "No -b flag here — that would try to create a new branch. Without -b, git checkout just switches to main."
    },
    {
        "concept": "Uploading your commits to GitHub",
        "situation": "You've made 3 commits locally on the 'main' branch.\n  None of them are on GitHub yet. You want to upload them so\n  they're backed up and visible to your team.",
        "task": "Push your local 'main' branch to the remote called 'origin':",
        "valid": ["git push origin main", "git push", "git push -u origin main"],
        "hint": "Use 'push' followed by the remote name ('origin') and branch name ('main')",
        "why": "'origin' is the default name for your GitHub remote. 'main' is the branch you're pushing."
    },
    {
        "concept": "Downloading your teammate's new commits",
        "situation": "Your teammate pushed a bug fix to GitHub an hour ago.\n  Your local copy doesn't have it. You need to download\n  AND apply their latest commits to your machine.",
        "task": "Download and merge the latest commits from the remote repository:",
        "valid": ["git pull", "git pull origin main"],
        "hint": "A 4-letter command that downloads AND merges remote changes into your active branch",
        "why": "git pull = git fetch + git merge. It downloads remote changes and applies them to your current branch."
    },
    {
        "concept": "Downloading remote updates WITHOUT merging",
        "situation": "You want to see what your teammates pushed to 'origin' without touching or merging into your local files yet.",
        "task": "Fetch remote updates from 'origin' safely without modifying your local working files:",
        "valid": ["git fetch", "git fetch origin", "git fetch --all"],
        "hint": "A 5-letter command that downloads remote commits without touching your working directory",
        "why": "'git fetch' downloads remote commits and updates remote branches (origin/main) without changing your local working directory."
    },
    {
        "concept": "Merging a feature branch into main",
        "situation": "You switched to 'main'. Your work on 'search-feature' is complete and tested.\n  Now you want to bring the commits from 'search-feature' into 'main'.",
        "task": "Merge 'search-feature' into the current branch:",
        "valid": ["git merge search-feature"],
        "hint": "Use the 'merge' command followed by the name of the branch you want to bring in",
        "why": "'git merge <branch>' brings the target branch's commits into your current checked-out branch."
    },
    {
        "concept": "Deleting a completed feature branch",
        "situation": "You already merged 'search-feature' into 'main'. You want to clean up your local branch list.",
        "task": "Safely delete the local branch named 'search-feature':",
        "valid": ["git branch -d search-feature"],
        "hint": "Use 'git branch' with the safe delete flag (-d) and the branch name",
        "why": "The lowercase '-d' safely deletes the branch only if it has already been merged."
    },
    {
        "concept": "Cloning a repository from GitHub",
        "situation": "You joined a new project. You need to download the full repository from GitHub onto your computer.",
        "task": "Clone the repo at 'https://github.com/example/repo.git':",
        "valid": ["git clone https://github.com/example/repo.git"],
        "hint": "Use the command that creates a full copy of a remote repo: git <subcommand> <url>",
        "why": "'git clone' copies the entire Git database, remote connections, and working files in one command."
    },
    {
        "concept": "Inspecting the last 5 commits concisely",
        "situation": "You want to inspect only the latest 5 commits in concise format.",
        "task": "Show exactly the last 5 commits on one line each:",
        "valid": ["git log -n 5 --oneline", "git log --oneline -n 5", "git log -5 --oneline"],
        "hint": "Combine 'git log' with a count limit flag (-n 5) and the single-line flag (--oneline)",
        "why": "'-n 5' limits the output count to 5, keeping your terminal uncluttered."
    },
    {
        "concept": "Filtering commit history by author",
        "situation": "You are doing code review and want to view only the commits made by contributor 'Alice'.",
        "task": "Filter git log to show commits by author 'Alice':",
        "valid": ['git log --author="Alice"', "git log --author='Alice'", "git log --author=Alice"],
        "hint": "Pass the author filter flag to git log: git log --author=\"...\"",
        "why": "'--author' filters history by author name or email pattern."
    }
]

CHALLENGES_HIGH = [
    {
        "concept": "Safely undoing a pushed commit",
        "situation": "You pushed commit 'a3f9c12' to main and teammates already pulled it.\n  It has a bug. You cannot use git reset because that would rewrite\n  history that your teammates already have.",
        "task": "Create a new commit that undoes commit 'a3f9c12' without rewriting history:",
        "valid": ["git revert a3f9c12", "git revert a3f9c12 --no-edit", "git revert --no-edit a3f9c12"],
        "hint": "Use the command that creates an inverse commit to safely undo changes: git <subcommand> <commit-id>",
        "why": "git revert doesn't erase the bad commit — it creates a new one that undoes it. Safe for shared branches."
    },
    {
        "concept": "Saving unfinished work before switching branches",
        "situation": "You're halfway through writing new code on 'feature' branch.\n  An urgent bug was just reported on 'main'. You need to switch branches\n  but you can't commit unfinished code.",
        "task": "Temporarily save your uncommitted changes so the workspace is clean:",
        "valid": ["git stash", "git stash save", "git stash push"],
        "hint": "A 5-letter command that shelves your uncommitted changes into a temporary drawer",
        "why": "git stash shelves your in-progress changes. Your workspace is clean, you switch to main, fix the bug, then come back."
    },
    {
        "concept": "Restoring stashed work after fixing the bug",
        "situation": "You fixed the urgent bug on main. Now you're back on 'feature' branch.\n  Your unfinished code from before is still in the stash.\n  You want to get it back and remove it from the stash in one step.",
        "task": "Restore and remove the most recent stash entry:",
        "valid": ["git stash pop", "git stash apply"],
        "hint": "Use 'git stash' with the action that applies and drops the entry (like popping a stack)",
        "why": "git stash pop applies the stashed changes back to your working directory and removes the stash entry."
    },
    {
        "concept": "Marking a release version with a lightweight tag",
        "situation": "Your team just finished testing v2.0 of the app.\n  You want to mark the current commit as an official release\n  so the team can always refer back to exactly this version.",
        "task": "Create a lightweight tag named 'v2.0' on the current commit:",
        "valid": ["git tag v2.0", "git tag -a v2.0 -m 'v2.0'", 'git tag -a v2.0 -m "v2.0"'],
        "hint": "Use the tag command followed by the version name: git <subcommand> <tagname>",
        "why": "Tags are permanent named pointers to specific commits. Use them for version releases so you can always find them."
    },
    {
        "concept": "Creating an annotated tag with metadata and message",
        "situation": "For an official public production release, you want to attach author, date, and a release description message 'production launch'.",
        "task": "Create an annotated tag 'v1.0' with message 'production launch':",
        "valid": [
            'git tag -a v1.0 -m "production launch"',
            "git tag -a v1.0 -m 'production launch'",
            'git tag -a v1.0 -m"production launch"'
        ],
        "hint": "Use 'git tag' with the annotated flag (-a) and message flag (-m)",
        "why": "Annotated tags (-a) store complete cryptographic object data including tagger info and message."
    },
    {
        "concept": "Unstaging a file without discarding local edits",
        "situation": "You accidentally ran 'git add config.json'. You do NOT want config.json in the upcoming commit,\n  but you want to keep all the changes you wrote in the file on disk.",
        "task": "Unstage 'config.json' while preserving its changes on disk:",
        "valid": [
            "git restore --staged config.json",
            "git reset HEAD config.json",
            "git reset config.json"
        ],
        "hint": "Use 'git restore' with the flag that targets staged files: --staged",
        "why": "'git restore --staged' pulls the file back out of the staging index without altering your file on disk."
    },
    {
        "concept": "Discarding unwanted modifications in working directory",
        "situation": "You made experimental edits in 'style.css' that didn't work out.\n  You haven't staged it yet, and you want to discard your changes and revert 'style.css' back to the last commit.",
        "task": "Discard all uncommitted changes in 'style.css':",
        "valid": ["git restore style.css", "git checkout -- style.css"],
        "hint": "Use the restore command followed by the filename (without --staged)",
        "why": "'git restore <file>' discards uncommitted working tree modifications and resets the file to the last committed version."
    },
    {
        "concept": "Amending the latest commit without changing message",
        "situation": "You just made a commit, but realized you forgot to stage 'assets/logo.png'.\n  You staged it with 'git add assets/logo.png' and want to merge it into that latest commit without re-typing the message.",
        "task": "Amend the latest commit keeping its existing commit message:",
        "valid": ["git commit --amend --no-edit", "git commit --amend -C HEAD"],
        "hint": "Combine 'git commit' with the amend flag (--amend) and a flag to skip editing the message (--no-edit)",
        "why": "'--amend --no-edit' updates the last commit with new staged files while keeping the exact same commit message."
    },
    {
        "concept": "Cherry-picking a specific commit from another branch",
        "situation": "Branch 'experimental' has a bugfix in commit 'c4b1a8f' that you need on 'main' right now without merging the whole branch.",
        "task": "Apply commit 'c4b1a8f' onto your current branch:",
        "valid": ["git cherry-pick c4b1a8f"],
        "hint": "The command is named after picking fruit: git cherry-... followed by the commit SHA",
        "why": "'git cherry-pick' copies and applies a single specific commit SHA from any branch onto your current branch."
    },
    {
        "concept": "Recovering commits after an accidental reset",
        "situation": "A developer on your team ran 'git reset --hard HEAD~5' by mistake.\n  Five commits appear gone from git log. But Git almost never truly deletes\n  data — there's a hidden timeline you can check.",
        "task": "Show the full timeline of all HEAD movements including the 'lost' ones:",
        "valid": ["git reflog", "git reflog show"],
        "hint": "A 6-letter command short for 'reference log' — Git's flight recorder",
        "why": "git reflog records every movement of HEAD, including resets. Find the commit SHA and run 'git reset --hard <SHA>' to recover."
    }
]

def run_arena_level(level_name, challenges, level_color):
    clear_screen()
    print(f"{level_color}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║   🎯 PRACTICE ARENA: {level_name:<45}║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Color.RESET}\n")
    print(f"{Color.DIM}  Type 'hint' if you need a clue. Type '0' or 'menu' anytime to return to Main Menu.{Color.RESET}\n")

    score = 0
    total = len(challenges)

    for i, ch in enumerate(challenges, 1):
        clear_screen()
        print(f"{level_color}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
        print(f"║   🎯 PRACTICE ARENA: {level_name:<45}║")
        print(f"╚════════════════════════════════════════════════════════════════════╝{Color.RESET}")
        print(f"\n{level_color}{Color.BOLD}── Challenge {i}/{total}: {ch['concept']} ──────────────{Color.RESET}")

        situation_text = ch.get("situation") or ch.get("human_story", "")
        print(f"\n{Color.BOLD}Situation:{Color.RESET}\n  {situation_text}")
        print(f"\n{Color.YELLOW}{Color.BOLD}Your task:{Color.RESET} {ch['task']}")

        attempts = 0
        max_attempts = 2
        while attempts < max_attempts:
            user_cmd = input(f"\n{Color.DIM}[Type your command, 'hint', or '0' for Menu]{Color.RESET}\n{Color.BOLD}{Color.CYAN}$ {Color.RESET}").strip()

            if user_cmd.lower() in ["0", "menu", "home", "back", "exit", "q"]:
                print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
                time.sleep(0.5)
                return False

            if user_cmd.lower() == "hint":
                print(f"  {Color.YELLOW}💡 Clue:{Color.RESET} {ch['hint']}")
                continue

            if not user_cmd:
                continue

            # Normalize whitespace and quote style
            normalized = " ".join(user_cmd.split())
            alt_normalized = normalized.replace("'", '"')
            alt_valid = [v.replace("'", '"') for v in ch["valid"]]
            is_valid = normalized in ch["valid"] or alt_normalized in alt_valid

            if is_valid:
                points = 100 if attempts == 0 else 50
                score += points
                print(f"\n{Color.GREEN}{Color.BOLD}✅ Correct! (+{points} pts){Color.RESET}")
                print(f"  {Color.DIM}{ch['why']}{Color.RESET}\n")
                break
            else:
                attempts += 1
                if attempts < max_attempts:
                    print(f"\n{Color.RED}❌ Not quite.{Color.RESET}  💡 Clue: {ch['hint']}")
                else:
                    expected_answer = ch["valid"][0]
                    print(f"\n{Color.RED}❌ Out of attempts. The command was:{Color.RESET} {Color.BOLD}{expected_answer}{Color.RESET}")
                    print(f"  {Color.DIM}{ch['why']}{Color.RESET}\n")

        time.sleep(0.8)

    max_possible = total * 100
    print(f"\n{Color.BOLD}{Color.MAGENTA}═══════════════════════════════════════════════════")
    print(f"   {level_name} LEVEL FINISHED! Final Score: {score}/{max_possible}")
    if score >= max_possible * 0.8:
        print(f"   🏆 Rank: Champion! Your terminal muscle memory is exceptional!")
    elif score >= max_possible * 0.5:
        print(f"   ⭐ Rank: Solid Developer! Great progress, keep building the habit!")
    else:
        print(f"   🌱 Rank: Apprentice. Play again or check 'Git for Humans' to level up!")
    print(f"═══════════════════════════════════════════════════{Color.RESET}\n")
    
    print(f"  {Color.YELLOW}[1] 🔄 Play Another Difficulty Level{Color.RESET}")
    print(f"  {Color.CYAN}[0] 🏠 Return to Main Menu{Color.RESET}\n")
    nxt = input(f"{Color.BOLD}Choose [1 or 0]: {Color.RESET}").strip().lower()
    if nxt in ["1", "replay", "r"]:
        return True
    return False
    if score >= max_possible * 0.8:
        print(f"   🏆 Rank: Champion! Your terminal muscle memory is exceptional!")
    elif score >= max_possible * 0.5:
        print(f"   ⭐ Rank: Solid Developer! Great progress, keep building the habit!")
    else:
        print(f"   🌱 Rank: Apprentice. Play again or check 'Git for Humans' to level up!")
    print(f"═══════════════════════════════════════════════════{Color.RESET}\n")
    
    print(f"  {Color.YELLOW}[1] 🔄 Play Another Difficulty Level{Color.RESET}")
    print(f"  {Color.CYAN}[0] 🏠 Return to Main Menu{Color.RESET}\n")
    nxt = input(f"{Color.BOLD}Choose [1 or 0]: {Color.RESET}").strip().lower()
    if nxt in ["1", "replay", "r"]:
        return True
    return False

def mode_command_arena():
    while True:
        clear_screen()
        print(f"{Color.GREEN}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
        print("║        🎯 MODE 2: 'TYPE THE COMMAND' HANDS-ON PRACTICE ARENA       ║")
        print("╚════════════════════════════════════════════════════════════════════╝\n")
        print_slow("Reading won't build muscle memory — typing real commands will!", 0.012, Color.CYAN)
        print_slow("No matter your background, you'll learn Git step-by-step through real scenarios.\n", 0.012, Color.WHITE)
        
        print(f"{Color.BOLD}CHOOSE YOUR DIFFICULTY LEVEL:{Color.RESET}\n")
        print(f"  {Color.GREEN}[1] 🌱 LOW / EASY (Zero Git Knowledge / Absolute Beginner){Color.RESET}")
        print(f"      • Friendly gaming & real-life analogies for someone who has never touched Git.")
        print(f"      • Helpful on-screen hints displayed upfront. High success rate & confidence boost!\n")
        
        print(f"  {Color.YELLOW}[2] ⚔️ MEDIUM (Apprentice Developer / Everyday Workflow){Color.RESET}")
        print(f"      • Branching, pushing to GitHub, pulling teammate changes, staging files.")
        print(f"      • Smart hints available on demand or after your first attempt.\n")
        
        print(f"  {Color.RED}[3] 🔥 HIGH (Git Ninja / Emergency Survival){Color.RESET}")
        print(f"      • Disaster recovery: git revert, stashing, reflog time-machine, release tags.")
        print(f"      • Strict test of real-world terminal muscle memory under pressure.\n")
        
        print(f"  {Color.CYAN}[0] 🏠 Return to Main Menu{Color.RESET}\n")
        
        diff_choice = input(f"{Color.BOLD}Select Difficulty [1 / 2 / 3] or 0 for Main Menu: {Color.RESET}").strip().lower()
        if diff_choice in ["0", "menu", "home", "back", "q", "exit"]:
            print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
            time.sleep(0.5)
            return
        
        if diff_choice == "1":
            level_name = "LOW / EASY (BEGINNER)"
            challenges = CHALLENGES_LOW
            color = Color.GREEN
        elif diff_choice == "2":
            level_name = "MEDIUM (APPRENTICE)"
            challenges = CHALLENGES_MEDIUM
            color = Color.YELLOW
        elif diff_choice == "3":
            level_name = "HIGH (GIT NINJA)"
            challenges = CHALLENGES_HIGH
            color = Color.RED
        else:
            print(f"{Color.RED}Please choose 1, 2, 3 or 0!{Color.RESET}")
            time.sleep(1)
            continue
        
        should_continue = run_arena_level(level_name, challenges, color)
        if not should_continue:
            return

def main():
    while True:
        clear_screen()
        print(BANNER)
        print(f"{Color.BOLD}Welcome to the interactive Git arcade! Choose your adventure:{Color.RESET}\n")
        print(f"  {Color.YELLOW}[1]{Color.RESET} 🐣 'Git for Humans' (Story Mode + Quick Quiz)")
        print(f"  {Color.GREEN}[2]{Color.RESET} 🎯 'Type The Command' Practice Arena (Low, Medium & High Difficulty)")
        print(f"  {Color.CYAN}[3]{Color.RESET} 🎓 Survive the Tech Interview & Viva (Boss Battle)")
        print(f"  {Color.RED}[4]{Color.RESET} 🚨 'Oh No, Git!' Disaster Scenarios")
        print(f"  {Color.BLUE}[5]{Color.RESET} 📚 12-Step Practical Lab & Workflow Cheatbook")
        print(f"  {Color.MAGENTA}[6]{Color.RESET} ⚡ Show My Configured Git Aliases")
        print(f"  {Color.WHITE}[7]{Color.RESET} 🏃 Exit to Terminal")
        
        choice = input(f"\n{Color.BOLD}Enter your choice [1 - 7]: {Color.RESET}").strip()

        if choice == "1":
            mode_git_for_humans()
        elif choice == "2":
            mode_command_arena()
        elif choice == "3":
            mode_viva_gauntlet()
        elif choice == "4":
            mode_disaster_recovery()
        elif choice == "5":
            mode_vtu_cheatbook()
        elif choice == "6":
            clear_screen()
            print(f"\n{Color.YELLOW}{Color.BOLD}⚡ YOUR SUPERCHARGED GIT ALIASES:{Color.RESET}\n")
            print(f"  {Color.CYAN}git st{Color.RESET}    -> Instant status check")
            print(f"  {Color.CYAN}git lg{Color.RESET}    -> Clean, one-line commit log")
            print(f"  {Color.CYAN}git files{Color.RESET} -> View commits with file names and stats")
            print(f"  {Color.CYAN}git last{Color.RESET}  -> Deep inspection of the latest commit\n")
            input(f"{Color.DIM}Press Enter to return...{Color.RESET}")
        elif choice in ["7", "q", "exit"]:
            print(f"\n{Color.GREEN}Keep committing like a ninja! Bye Prajwal! 🚀{Color.RESET}\n")
            time.sleep(0.8)
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Color.YELLOW}Game exited. See you in the commits! 👋{Color.RESET}\n")
    except Exception as e:
        print(f"\n{Color.RED}Something went wrong: {e}{Color.RESET}\n")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")

