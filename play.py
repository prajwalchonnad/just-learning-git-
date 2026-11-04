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

    for i, item in enumerate(questions[:5], 1):
        print(f"\n{Color.BOLD}{Color.WHITE}─── QUESTION {i}/5 | Lives: {'☕ ' * lives} | Score: {score} ───{Color.RESET}")
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
        time.sleep(1.5)

    print(f"\n{Color.BOLD}{Color.MAGENTA}═══════════════════════════════════════════════════")
    print(f"   CHALLENGE FINISHED! Final Score: {score}/500")
    if score >= 400:
        print(f"   🏆 Rank: Git Master! Ready for senior engineering!")
    elif score >= 200:
        print(f"   ⭐ Rank: Solid Developer! You survived with confidence!")
    else:
        print(f"   🧄 Rank: Burnt Garlic Rookie. Time to play again!")
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
    for i, scenario in enumerate(DISASTER_SCENARIOS, 1):
        clear_screen()
        print(f"{Color.RED}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
        print("║           🚨 MODE: REAL-WORLD GIT PROBLEM SOLVER                   ║")
        print(f"╚════════════════════════════════════════════════════════════════════╝\n")
        print(f"{Color.BOLD}{Color.YELLOW}── SCENARIO {i}/3 ──────────────────────────────────────────────────{Color.RESET}")
        print(f"\n{Color.BOLD}{Color.WHITE}{scenario['title']}{Color.RESET}\n")
        print_slow(scenario['story'], 0.013, Color.WHITE)
        print(f"\n{Color.CYAN}{Color.BOLD}What do you do?{Color.RESET}\n  {scenario['prompt']}\n")

        for idx, ch in enumerate(scenario["choices"], 1):
            print(f"  {Color.YELLOW}[{idx}]{Color.RESET} {ch}")

        while True:
            raw_pick = input(f"\n{Color.BOLD}Your answer [1 - 4] (or '0' for Menu): {Color.RESET}").strip().lower()
            if raw_pick in ["0", "menu", "home", "q", "exit"]:
                print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
                time.sleep(0.5)
                return
            try:
                pick = int(raw_pick)
                if 1 <= pick <= 4:
                    break
            except ValueError:
                pass
            print(f"{Color.RED}Enter a number from 1 to 4 (or '0' for Menu).{Color.RESET}")

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

    print(f"\n{Color.BOLD}{Color.MAGENTA}═══════════════════════════════════════════════════")
    print(f"   Problem Solver Complete! Score: {score}/450")
    if score >= 400:
        print(f"   ✅ Excellent! You handle real Git emergencies with confidence.")
    elif score >= 200:
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

def mode_git_for_humans():
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
    print("║              🐣 GIT FOR HUMANS — START HERE                        ║")
    print("╚════════════════════════════════════════════════════════════════════╝\n")
    print_slow("Never used Git before? Perfect. This takes 5 minutes.", 0.015, Color.CYAN)
    print_slow("No jargon. Just real situations and what Git does for you.\n", 0.015, Color.WHITE)

    # --- ACT 1: The problem Git solves ---
    print(f"{Color.BOLD}── PART 1: Why Does Git Exist? ──────────────────────────────────────{Color.RESET}\n")
    print_slow("You've probably done this before:", 0.015)
    print(f"""
  📄 report.docx
  📄 report_v2.docx
  📄 report_FINAL.docx
  📄 report_FINAL_actual.docx
  📄 report_USE_THIS_ONE.docx
""")
    print_slow("That is manual version control. It works, but it is a disaster to manage.", 0.015)
    print_slow("Git solves this. Instead of saving copies, Git tracks every change inside one folder.\n", 0.015, Color.GREEN)

    s = input(f"{Color.DIM}[Enter to continue, '0' to go back to menu]{Color.RESET} ").strip().lower()
    if s in ["0", "menu", "q"]: return

    # --- ACT 2: What Git actually is ---
    clear_screen()
    print(f"{Color.BOLD}── PART 2: What Git Actually Does ───────────────────────────────────{Color.RESET}\n")
    print_slow("Git keeps a timeline of snapshots of your project.", 0.015, Color.CYAN)
    print_slow("Every time you save a checkpoint, Git remembers exactly what changed and when.\n", 0.015)

    print(f"""  {Color.GREEN}git init{Color.RESET}      →  Tell Git to start tracking this folder.
  {Color.GREEN}git add .{Color.RESET}     →  Select the files you want to include in the next snapshot.
  {Color.GREEN}git commit{Color.RESET}    →  Save the snapshot with a short note describing what changed.
  {Color.GREEN}git push{Color.RESET}      →  Upload your snapshots to GitHub so they are backed up online.
  {Color.GREEN}git pull{Color.RESET}      →  Download snapshots from GitHub (e.g. from a teammate).
""")
    print_slow("That's the core. Everything else in Git builds on these five commands.", 0.015, Color.WHITE)

    s = input(f"\n{Color.DIM}[Enter to continue, '0' to go back to menu]{Color.RESET} ").strip().lower()
    if s in ["0", "menu", "q"]: return

    # --- ACT 3: Branching — real scenario ---
    clear_screen()
    print(f"{Color.BOLD}── PART 3: Working Without Breaking Things (Branches) ──────────────{Color.RESET}\n")
    print_slow("Here's a real situation:", 0.015)
    print_slow("Your app is working. You want to add a new login feature.", 0.015)
    print_slow("But what if the new code breaks the existing app while you're writing it?\n", 0.015, Color.RED)

    print_slow("The answer: create a branch.", 0.015, Color.GREEN)
    print(f"""
  {Color.CYAN}git checkout -b login-feature{Color.RESET}

  → This creates a separate working copy of your project called 'login-feature'.
  → You build and test on this branch. The main app stays untouched.
  → When the feature is ready and tested, you merge it into main.
  → If you decide to scrap it, delete the branch. Main was never affected.
""")
    print_slow("This is how professional teams work on features safely.", 0.015, Color.WHITE)

    s = input(f"{Color.DIM}[Enter to continue, '0' to go back to menu]{Color.RESET} ").strip().lower()
    if s in ["0", "menu", "q"]: return

    # --- ACT 4: Interactive decision ---
    clear_screen()
    print(f"{Color.BOLD}── PART 4: Quick Check — What Would You Do? ─────────────────────────{Color.RESET}\n")
    print_slow("You just found a critical bug on the main branch.", 0.015)
    print_slow("You were in the middle of building a new feature. You haven't committed yet.\n", 0.015)
    print(f"  {Color.YELLOW}[1]{Color.RESET} Run 'git stash' to save your in-progress work, switch to main, fix the bug.")
    print(f"  {Color.YELLOW}[2]{Color.RESET} Commit the half-finished feature code and push it to main to fix later.")
    print(f"  {Color.YELLOW}[3]{Color.RESET} Manually copy your files to the Desktop and switch branches.")
    print(f"  {Color.CYAN}[0]{Color.RESET} Back to Menu\n")

    ans = input(f"{Color.BOLD}Your answer [1 / 2 / 3]: {Color.RESET}").strip()
    if ans in ["0", "menu", "q"]:
        return
    elif ans == "1":
        print(f"\n{Color.GREEN}{Color.BOLD}✅ Exactly right.{Color.RESET}")
        print("  'git stash' saves your unfinished work without committing it.")
        print("  You get a clean workspace, fix the bug on main, then run 'git stash pop' to get your work back.")
    elif ans == "2":
        print(f"\n{Color.RED}❌ Not ideal.{Color.RESET}")
        print("  Pushing half-finished code to main can break things for your whole team.")
        print("  'git stash' is the right tool here — it saves your work temporarily without committing.")
    else:
        print(f"\n{Color.RED}❌ Manual file copying is what Git is designed to replace.{Color.RESET}")
        print("  Use 'git stash'. It saves your changes, cleans the workspace, and restores everything when you're done.")

    time.sleep(1.5)

    # --- ACT 5: Checkpoint Quiz ---
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}── PART 5: Quick Quiz — 3 Questions ─────────────────────────────────{Color.RESET}\n")
    print_slow("Answer these to confirm you've got the basics.\n", 0.015)

    quiz = [
        {
            "q": "1. You edited a file and want Git to include it in the next snapshot. What command do you run?",
            "opts": ["A) git commit", "B) git add <filename>", "C) git push"],
            "ans": "B",
            "explain": "'git add' stages the file — it tells Git 'include this in my next commit'. Without it, the file change is ignored."
        },
        {
            "q": "2. Your teammate pushed new code to GitHub. How do you get their changes on your machine?",
            "opts": ["A) git push", "B) git init", "C) git pull"],
            "ans": "C",
            "explain": "'git pull' downloads and merges changes from the remote repository into your local copy."
        },
        {
            "q": "3. You want to try a new feature without risking the working code. What do you create?",
            "opts": ["A) A new folder called 'backup'", "B) A new branch", "C) A new repository"],
            "ans": "B",
            "explain": "A branch is a safe, isolated copy of your project. Work on it freely — the main branch is untouched until you merge."
        }
    ]

    h_score = 0
    for item in quiz:
        print(f"{Color.CYAN}{Color.BOLD}{item['q']}{Color.RESET}")
        for opt in item["opts"]:
            print(f"  {opt}")
        choice = input(f"{Color.BOLD}  Your answer [A/B/C] (or '0' for Menu): {Color.RESET}").strip().upper()
        if choice in ["0", "MENU", "Q", "EXIT"]:
            print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
            return
        if choice == item["ans"]:
            h_score += 1
            print(f"{Color.GREEN}  ✅ Correct! {item['explain']}{Color.RESET}\n")
        else:
            print(f"{Color.RED}  ❌ Not quite. {item['explain']}{Color.RESET}\n")
        time.sleep(0.8)

    print(f"{Color.BOLD}{Color.MAGENTA}═══════════════════════════════════════════════════")
    print(f"   You scored {h_score}/3.")
    if h_score == 3:
        print("   ✅ You've got the fundamentals. Try Mode 2 to practice typing commands!")
    elif h_score >= 1:
        print("   👍 Good start. Re-read the parts you missed, then try the Practice Arena.")
    else:
        print("   📖 No worries — go through GIT_FOR_HUMANS.md and come back. You'll get it.")
    print(f"═══════════════════════════════════════════════════{Color.RESET}\n")
    input(f"{Color.DIM}Press Enter to return to the main menu...{Color.RESET}")

# ----------------- COMMAND CHALLENGES BY DIFFICULTY -----------------

CHALLENGES_LOW = [
    {
        "concept": "Starting fresh — initializing a repository",
        "situation": "You just created a new folder called 'my-project' for your work.\n  Right now it is a plain folder. Git doesn't know about it yet.\n  You need to tell Git to start tracking this folder.",
        "task": "Run the command that initializes Git in the current folder:",
        "valid": ["git init", "git init ."],
        "easy_hint": "git init",
        "why": "This creates a hidden '.git' folder inside your project. That's where Git stores all your history."
    },
    {
        "concept": "Checking what has changed",
        "situation": "You edited a file called 'index.html'.\n  Before doing anything else, you want to see what files have changed,\n  which are staged, and which are untracked.",
        "task": "Run the command to see the current state of your working directory:",
        "valid": ["git status", "git st", "git status -s", "git status --short"],
        "easy_hint": "git status",
        "why": "git status is the most used Git command. Run it constantly — it always tells you what's going on."
    },
    {
        "concept": "Staging files before saving",
        "situation": "You edited two files today. You want to include all of them\n  in your next commit. Git doesn't save anything automatically —\n  you have to explicitly select what goes into the next snapshot.",
        "task": "Stage all changed files in the current directory:",
        "valid": ["git add .", "git add -A", "git add --all"],
        "easy_hint": "git add .",
        "why": "The dot '.' means 'everything here'. git add picks what goes into your next commit."
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
        "easy_hint": 'git commit -m "add homepage layout"',
        "why": "Every commit needs a message (-m flag). It describes what changed so you (and your team) can understand the history."
    },
    {
        "concept": "Viewing the commit history",
        "situation": "You've made a few commits over the past few days.\n  You want to see all of them — who made them, when, and what the message said.",
        "task": "Show the full commit history of this repository:",
        "valid": ["git log", "git lg", "git log --oneline", "git log -n 5"],
        "easy_hint": "git log",
        "why": "git log lists every commit in reverse order (newest first). Each has a unique ID, author, date, and message."
    }
]

CHALLENGES_MEDIUM = [
    {
        "concept": "Creating and switching to a new branch",
        "situation": "You're on 'main' and want to start building a new 'search' feature.\n  You don't want to work directly on main — you need a separate branch\n  so the working code stays safe while you build.",
        "task": "Create a new branch called 'search-feature' and switch to it in one command:",
        "valid": ["git checkout -b search-feature", "git switch -c search-feature"],
        "hint": "git checkout -b search-feature",
        "why": "The -b flag creates the branch AND switches to it. Without -b, git checkout just switches to an existing branch."
    },
    {
        "concept": "Switching back to an existing branch",
        "situation": "You're on 'search-feature'. Your team lead just told you to\n  review something on the 'main' branch. You need to switch without losing anything.",
        "task": "Switch to the already-existing branch called 'main':",
        "valid": ["git checkout main", "git switch main"],
        "hint": "git checkout main",
        "why": "No -b flag here — that would try to create a new branch. Without -b, git checkout just switches to main."
    },
    {
        "concept": "Uploading your commits to GitHub",
        "situation": "You've made 3 commits locally on the 'main' branch.\n  None of them are on GitHub yet. You want to upload them so\n  they're backed up and visible to your team.",
        "task": "Push your local 'main' branch to the remote called 'origin':",
        "valid": ["git push origin main", "git push", "git push -u origin main"],
        "hint": "git push origin main",
        "why": "'origin' is the default name for your GitHub remote. 'main' is the branch you're pushing."
    },
    {
        "concept": "Downloading your teammate's new commits",
        "situation": "Your teammate pushed a bug fix to GitHub an hour ago.\n  Your local copy doesn't have it. You need to download\n  AND apply their latest commits to your machine.",
        "task": "Download and merge the latest commits from the remote repository:",
        "valid": ["git pull", "git pull origin main"],
        "hint": "git pull",
        "why": "git pull = git fetch + git merge. It downloads remote changes and applies them to your current branch."
    },
    {
        "concept": "Staging only one specific file",
        "situation": "You edited three files today: index.html, style.css, and app.js.\n  But only the index.html changes are ready. You want to commit just that file\n  and leave the other two for a separate commit.",
        "task": "Stage only the file 'index.html':",
        "valid": ["git add index.html"],
        "hint": "git add index.html",
        "why": "Specifying a filename instead of '.' gives you precise control over what goes into each commit."
    }
]

CHALLENGES_HIGH = [
    {
        "concept": "Safely undoing a pushed commit",
        "situation": "You pushed commit 'a3f9c12' to main and teammates already pulled it.\n  It has a bug. You cannot use git reset because that would rewrite\n  history that your teammates already have.",
        "task": "Create a new commit that undoes commit 'a3f9c12' without rewriting history:",
        "valid": ["git revert a3f9c12", "git revert a3f9c12 --no-edit", "git revert --no-edit a3f9c12"],
        "hint": "git revert a3f9c12",
        "why": "git revert doesn't erase the bad commit — it creates a new one that undoes it. Safe for shared branches."
    },
    {
        "concept": "Saving unfinished work before switching branches",
        "situation": "You're halfway through writing new code on 'feature' branch.\n  An urgent bug was just reported on 'main'. You need to switch branches\n  but you can't commit unfinished code.",
        "task": "Temporarily save your uncommitted changes so the workspace is clean:",
        "valid": ["git stash", "git stash save", "git stash push"],
        "hint": "git stash",
        "why": "git stash shelves your in-progress changes. Your workspace is clean, you switch to main, fix the bug, then come back."
    },
    {
        "concept": "Restoring stashed work after fixing the bug",
        "situation": "You fixed the urgent bug on main. Now you're back on 'feature' branch.\n  Your unfinished code from before is still in the stash.\n  You want to get it back and remove it from the stash in one step.",
        "task": "Restore and remove the most recent stash entry:",
        "valid": ["git stash pop", "git stash apply"],
        "hint": "git stash pop",
        "why": "git stash pop applies the stashed changes back to your working directory and removes the stash entry."
    },
    {
        "concept": "Marking a release version",
        "situation": "Your team just finished testing v2.0 of the app.\n  You want to mark the current commit as an official release\n  so the team can always refer back to exactly this version.",
        "task": "Create a lightweight tag named 'v2.0' on the current commit:",
        "valid": ["git tag v2.0", "git tag -a v2.0 -m 'v2.0'", 'git tag -a v2.0 -m "v2.0"'],
        "hint": "git tag v2.0",
        "why": "Tags are permanent named pointers to specific commits. Use them for version releases so you can always find them."
    },
    {
        "concept": "Recovering commits after an accidental reset",
        "situation": "A developer on your team ran 'git reset --hard HEAD~5' by mistake.\n  Five commits appear gone from git log. But Git almost never truly deletes\n  data — there's a hidden timeline you can check.",
        "task": "Show the full timeline of all HEAD movements including the 'lost' ones:",
        "valid": ["git reflog", "git reflog show"],
        "hint": "git reflog",
        "why": "git reflog records every movement of HEAD, including resets. Find the commit SHA and run 'git reset --hard <SHA>' to recover."
    }
]

def run_arena_level(level_name, challenges, level_color):
    clear_screen()
    print(f"{level_color}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║   🎯 PRACTICE ARENA: {level_name:<45}║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Color.RESET}\n")
    print(f"{Color.DIM}  Type 'hint' for a hint. Type '0' or 'menu' anytime to go back to Main Menu.{Color.RESET}\n")

    score = 0
    total = len(challenges)

    for i, ch in enumerate(challenges, 1):
        clear_screen()
        print(f"{level_color}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
        print(f"║   🎯 PRACTICE ARENA: {level_name:<45}║")
        print(f"╚════════════════════════════════════════════════════════════════════╝{Color.RESET}")
        print(f"\n{level_color}{Color.BOLD}── Challenge {i}/{total}: {ch['concept']} ──────────────{Color.RESET}")

        # Print situation (supports both 'situation' key for new data and 'human_story' for legacy)
        situation_text = ch.get("situation") or ch.get("human_story", "")
        print(f"\n{Color.BOLD}Situation:{Color.RESET}\n  {situation_text}")
        print(f"\n{Color.YELLOW}{Color.BOLD}Your task:{Color.RESET} {ch['task']}")

        # In Easy / Low mode: Give the hint upfront
        if "easy_hint" in ch:
            print(f"\n  {Color.GREEN}💡 Hint: {Color.BOLD}{ch['easy_hint']}{Color.RESET}")

        attempts = 0
        max_attempts = 2
        while attempts < max_attempts:
            user_cmd = input(f"\n{Color.DIM}[Type your command, 'hint', or '0' to exit]{Color.RESET}\n{Color.BOLD}{Color.CYAN}$ {Color.RESET}").strip()

            if user_cmd.lower() in ["0", "menu", "home", "back", "exit", "q"]:
                print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
                time.sleep(0.5)
                return False

            if user_cmd.lower() == "hint":
                hint_text = ch.get("easy_hint") or ch.get("hint", "")
                print(f"  {Color.YELLOW}💡 Hint:{Color.RESET} {Color.BOLD}{hint_text}{Color.RESET}")
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
                hint_text = ch.get("easy_hint") or ch.get("hint", "")
                if attempts < max_attempts:
                    print(f"\n{Color.RED}❌ Not quite.{Color.RESET}  Hint: {Color.BOLD}{hint_text}{Color.RESET}")
                else:
                    print(f"\n{Color.RED}❌ The answer was:{Color.RESET} {Color.BOLD}{hint_text}{Color.RESET}")
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

