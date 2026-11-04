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
{Color.YELLOW}{Color.BOLD}       🚀 Interactive Git Learning Arcade & Real-World Developer Simulator ⚡
{Color.RESET}"""

# ----------------- GAME DATA -----------------

VIVA_QUESTIONS = [
    {
        "q": "Senior Engineer / Examiner asks: 'What is the exact difference between git fetch and git pull?'",
        "options": [
            "A) git fetch is only for local branches; git pull is only for remote repositories.",
            "B) git fetch downloads remote changes without merging; git pull fetches AND merges them.",
            "C) git fetch overwrites local uncommitted changes; git pull preserves them.",
            "D) There is no difference; git fetch is deprecated syntax."
        ],
        "ans": "B",
        "tip": "Core Concept: git fetch is safe and doesn't touch your working tree. git pull = git fetch + git merge!",
        "praise": "Interviewer nods with approval: 'Clean, accurate answer. You understand remote tracking.'",
        "roast": "Interviewer takes notes: 'Remember: git fetch only inspects & downloads; git pull automatically merges!'"
    },
    {
        "q": "You made a commit with a critical bug directly on 'main' and ALREADY PUSHED IT to the team's remote GitHub repository. What is the safest way to undo it without breaking teammates' local clones?",
        "options": [
            "A) git reset --hard HEAD~1 followed by git push --force",
            "B) git revert <commit-id>",
            "C) git rm -r *",
            "D) git checkout -b rollback"
        ],
        "ans": "B",
        "tip": "Safety Rule: On public/shared branches, ALWAYS use 'git revert'. It creates a new inverse commit instead of rewriting history!",
        "praise": "Exactly right! You preserved shared history and prevented massive merge conflicts for your team.",
        "roast": "Careful! Force-pushing a hard reset rewrites shared history and corrupts your teammates' local branches. Use git revert!"
    },
    {
        "q": "You are half-way through coding a new feature when an urgent hotfix request comes in for 'main'. You don't want to commit incomplete, broken code. What command shelves your changes temporarily?",
        "options": [
            "A) git stash (or git stash save 'wip')",
            "B) git branch --temp",
            "C) git clean -fd",
            "D) git checkout -f main"
        ],
        "ans": "A",
        "tip": "Workspace Hygiene: 'git stash' safely tucks away dirty uncommitted changes onto a temporary stack so you can switch branches cleanly.",
        "praise": "Clean move! Your working tree is clean and your work is safely preserved in the stash stack.",
        "roast": "Watch out! 'git checkout -f' or 'git clean' can discard uncommitted work permanently. Always use 'git stash'!"
    },
    {
        "q": "How do you cherry-pick a range of commits from commit A up to commit B (inclusive of both A and B)?",
        "options": [
            "A) git cherry-pick A..B",
            "B) git cherry-pick A^..B",
            "C) git cherry-pick --range A B",
            "D) git cherry-pick A+B"
        ],
        "ans": "B",
        "tip": "Range Syntax: In Git revision ranges, A..B is exclusive of A (it means 'reachable from B but not A'). Adding the caret A^..B includes A as well!",
        "praise": "Spot on! That caret '^' is the secret handshake of Git professionals who understand revision ranges.",
        "roast": "Almost! In Git, 'A..B' skips commit A. You must write 'A^..B' to include commit A itself!"
    },
    {
        "q": "Your lead asks: 'What does this command do: git log --author=\"JohnDoe\" --since=\"2024-01-01\"'?",
        "options": [
            "A) Re-attributes all commits after Jan 1, 2024 to JohnDoe.",
            "B) Deletes commits by JohnDoe after Jan 1, 2024.",
            "C) Filters the commit history to display only commits authored by JohnDoe on or after Jan 1, 2024.",
            "D) Searches file contents in the codebase for the string 'JohnDoe'."
        ],
        "ans": "C",
        "tip": "Log Auditing: git log provides powerful investigation flags like --author, --since, --until, and --grep.",
        "praise": "Clean answer! You know how to audit Git history effectively.",
        "roast": "Incorrect! 'git log' is strictly a read-only inspection tool. It filters commits by author and date range."
    },
    {
        "q": "What is the key technical difference between a lightweight tag and an annotated tag in Git?",
        "options": [
            "A) Lightweight tags can only be created on branches named 'release'.",
            "B) Lightweight tags are simple pointers/bookmarks to a commit hash; annotated tags are full Git objects with author name, email, date, and message.",
            "C) Lightweight tags expire automatically after 30 days.",
            "D) Annotated tags can only be created by repository owners."
        ],
        "ans": "B",
        "tip": "Versioning Standards: Use annotated tags (git tag -a v1.0 -m '...') for public releases so release metadata is cryptographically preserved.",
        "praise": "Precise and accurate! Lightweight tags are quick bookmarks; annotated tags are official release records.",
        "roast": "Not quite! Lightweight tags are simple pointers (like a branch that doesn't move). Annotated tags store complete metadata."
    },
    {
        "q": "When running 'git merge feature-branch -m \"Integrate user authentication\"', what happens?",
        "options": [
            "A) It immediately deletes the feature branch after merging.",
            "B) It merges feature-branch into the currently checked-out branch, recording a merge commit with the specified message.",
            "C) It renames feature-branch to 'Integrate user authentication'.",
            "D) It only merges files that have no conflicts, ignoring the rest."
        ],
        "ans": "B",
        "tip": "Branch Integration: Merging combines branch histories. Providing '-m' sets a custom, human-readable merge commit message.",
        "praise": "Clean merge understanding! You understand branch integration.",
        "roast": "Incorrect! Merging combines branch histories into your current branch and attaches your custom commit message."
    }
]

DISASTER_SCENARIOS = [
    {
        "title": "🚨 Production Crash Hotfix",
        "story": "Commit 'prod981' introduced a fatal database query timeout directly on 'main'. The application is returning 500 errors to real users right now. The team needs to roll back the changes immediately without rewriting git history on the remote repository.",
        "prompt": "Which command safely creates a new commit that reverses the exact changes of 'prod981'?",
        "choices": [
            "git revert prod981 --no-edit",
            "git reset --hard HEAD~1",
            "git rm -rf .",
            "git checkout -b fix-branch"
        ],
        "ans_idx": 1,
        "reaction": "✅ Production restored! 'git revert' safely deployed the inverse commit without breaking teammates' branches."
    },
    {
        "title": "🔐 Accidental API Secret in Staging Area",
        "story": "You added a live production database password and OpenAI API key into a '.env' file. You ran 'git add .' and realized '.env' is sitting staged for the upcoming commit. It has NOT been committed yet.",
        "prompt": "How do you remove '.env' from the staging area WITHOUT deleting the file from your computer disk?",
        "choices": [
            "rm -f .env",
            "git restore --staged .env",
            "git push origin main",
            "git checkout -b secrets"
        ],
        "ans_idx": 2,
        "reaction": "✅ Secret safely unstaged! The file remains on your disk, and you can now add '.env' to your '.gitignore'."
    },
    {
        "title": "⚡ Accidental 'git reset --hard' Recovery",
        "story": "A developer accidentally typed 'git reset --hard HEAD~3' instead of soft reset. Three days of work have disappeared from 'git log' and the terminal shows a clean working tree. Heart rate: 180 BPM.",
        "prompt": "Which Git recovery tool logs every update to HEAD and lets you find the lost commit SHA?",
        "choices": [
            "git status",
            "git reflog",
            "git log -p",
            "git fsck --lost-found"
        ],
        "ans_idx": 2,
        "reaction": "✅ Commits rescued! 'git reflog' showed the exact commit SHA before the reset. You checked it out and saved the work!"
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
    print("║               🚨 MODE 2: 'OH NO, GIT!' DISASTER SIMULATOR          ║")
    print("╚════════════════════════════════════════════════════════════════════╝\n")
    print_slow("Real-world emergency situations. Can you fix them before production burns down?\n", 0.02)

    score = 0
    for i, scenario in enumerate(DISASTER_SCENARIOS, 1):
        print(f"\n{Color.BOLD}{Color.YELLOW}─── SCENARIO {i}: {scenario['title']} ───{Color.RESET}")
        print_slow(f"\n{scenario['story']}", 0.015, Color.WHITE)
        print_slow(f"{Color.CYAN}{scenario['prompt']}{Color.RESET}\n", 0.015)

        for idx, ch in enumerate(scenario["choices"], 1):
            print(f"  {Color.YELLOW}[{idx}] {ch}{Color.RESET}")

        while True:
            raw_input = input(f"\n{Color.BOLD}Select your tool [1 - 4] (or '0' for Menu): {Color.RESET}").strip().lower()
            if raw_input in ["0", "menu", "home", "q", "exit"]:
                print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
                time.sleep(0.5)
                return
            try:
                pick = int(raw_input)
                if 1 <= pick <= 4:
                    break
            except ValueError:
                pass
            print(f"{Color.RED}Enter a number from 1 to 4 (or '0' for Menu)!{Color.RESET}")

        if pick == scenario["ans_idx"]:
            score += 150
            print(f"\n{Color.GREEN}{Color.BOLD}{scenario['reaction']}{Color.RESET} (+150 pts)\n")
        else:
            print(f"\n{Color.RED}{Color.BOLD}💥 DISASTER ESCALATED! That wasn't the right fix!{Color.RESET}\n")
        time.sleep(1.5)

    print(f"{Color.CYAN}Disaster Simulation Complete! Score: {score}/450{Color.RESET}")
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
    print("║         🐣 'GIT FOR HUMANS': THE ANTI-BORING INTERACTIVE STORY      ║")
    print("╚════════════════════════════════════════════════════════════════════╝\n")
    print_slow("Welcome! If words like 'cryptographic hash tree' make you want to take a nap,", 0.02, Color.CYAN)
    print_slow("you are in the right place. Let's understand Git through real life and video games.\n", 0.02, Color.WHITE)

    # Act 1
    print(f"{Color.BOLD}─── ACT 1: THE TRAGEDY OF DESKTOP ICONS ───{Color.RESET}")
    print_slow("Imagine it is 2:00 AM. You are writing an important document (or recipe, or code).", 0.015)
    print_slow("You hit 'Save As' and your desktop looks like this:\n", 0.015)
    print(f"  📄 my_project.txt")
    print(f"  📄 my_project_v2.txt")
    print(f"  📄 my_project_final.txt")
    print(f"  📄 my_project_really_final_mom_swears.txt")
    print(f"  📄 my_project_USE_THIS_OR_DIE.txt\n")
    
    step1 = input(f"{Color.YELLOW}Hit [Enter] to see how Git fixes this madness (or '0' for Menu)...{Color.RESET}").strip().lower()
    if step1 in ["0", "menu", "home", "q", "exit"]:
        print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
        return

    # Act 2
    clear_screen()
    print(f"{Color.BOLD}─── ACT 2: THE VIDEO GAME SAVE SYSTEM ───{Color.RESET}\n")
    print_slow("Git is NOT rocket science. Git is literally just a SAVE SYSTEM from a video game! 🎮", 0.02, Color.GREEN)
    print_slow("""
  1. git init       -> You clicked 'New Game' in GTA / Elden Ring.
  2. git add        -> Putting loot into your Amazon shopping cart.
  3. git commit     -> Saving your game at a bonfire / checkpoint.
  4. git push       -> Cloud Save to PlayStation Plus / Steam (GitHub).
""", 0.015)

    step2 = input(f"{Color.YELLOW}Hit [Enter] to play the 'Save & Catastrophe' simulation (or '0' for Menu)...{Color.RESET}").strip().lower()
    if step2 in ["0", "menu", "home", "q", "exit"]:
        print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
        return

    # Act 3: Interactive Decision
    clear_screen()
    print(f"{Color.BOLD}─── ACT 3: THE PARALLEL UNIVERSE (BRANCHING) ───{Color.RESET}\n")
    print_slow("You are cooking your famous biryani. It is perfect.", 0.015)
    print_slow("Suddenly, your roommate says: 'Bro, add dark chocolate and pineapples to it!' 🍍🍫", 0.015, Color.MAGENTA)
    print_slow("Do you ruin your main pot? NO! You create a PARALLEL UNIVERSE (git branch)!\n", 0.015)
    
    print(f"  Timeline A (main)       : Delicious Normal Biryani")
    print(f"  Timeline B (experiment) : Chocolate Pineapple Chaos\n")

    print_slow("You taste Timeline B... It tastes like pure regret.", 0.015, Color.RED)
    print_slow("What do you do with Git?\n", 0.015)
    print(f"  [1] Keep Timeline A and peacefully delete Timeline B. (Main pot was never touched!)")
    print(f"  [2] Throw away the entire kitchen and order Swiggy.")
    print(f"  [0] 🏠 Return to Main Menu")
    
    ans = input(f"\n{Color.BOLD}Your choice [1 or 2] (or '0' for Menu): {Color.RESET}").strip().lower()
    if ans in ["0", "menu", "home", "q", "exit"]:
        print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
        return
    if ans == "1":
        print(f"\n{Color.GREEN}{Color.BOLD}🎉 EXACTLY! That is 'git branch' and 'git merge'. You only merge if it tastes good!{Color.RESET}\n")
    else:
        print(f"\n{Color.YELLOW}Ordering food is tempting, but with Git, Timeline A was 100% safe all along!{Color.RESET}\n")

    # Act 4: Quick 3-Question Checkpoint Quiz
    clear_screen()
    print(f"{Color.YELLOW}{Color.BOLD}─── ACT 4: QUICK POP QUIZ (TEST YOUR HUMAN INTUITION) ───{Color.RESET}\n")
    print_slow("Reading is good, but answering proves you actually got it! 3 fast questions:\n", 0.015)

    human_quiz = [
        {
            "q": "1. What is 'git add' most similar to in real life?",
            "opts": ["A) Burning your laptop", "B) Putting items in your Amazon shopping cart before checkout", "C) Sending an email to Linus Torvalds"],
            "ans": "B",
            "explain": "git add stages files into the cart so you can commit (buy) them next!"
        },
        {
            "q": "2. In video games, what is a 'git commit'?",
            "opts": ["A) A bonfire / checkpoint where you save your game", "B) Dying to the final boss", "C) Quitting without saving"],
            "ans": "A",
            "explain": "git commit creates a permanent checkpoint you can always return to."
        },
        {
            "q": "3. Why do developers use 'git branch'?",
            "opts": ["A) Because they love botany", "B) To experiment in a safe parallel timeline without breaking the main project", "C) To delete all files"],
            "ans": "B",
            "explain": "Branches let you try risky ideas. If they fail, delete the branch. Main stays perfect!"
        }
    ]

    h_score = 0
    for item in human_quiz:
        print(f"{Color.CYAN}{Color.BOLD}{item['q']}{Color.RESET}")
        for opt in item["opts"]:
            print(f"  {opt}")
        choice = input(f"{Color.BOLD}Your answer [A/B/C] (or '0' for Menu): {Color.RESET}").strip().upper()
        if choice in ["0", "MENU", "HOME", "Q", "EXIT"]:
            print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
            return
        if choice == item["ans"]:
            h_score += 1
            print(f"{Color.GREEN}✅ Spot on! {item['explain']}{Color.RESET}\n")
        else:
            print(f"{Color.RED}❌ Not quite! {item['explain']}{Color.RESET}\n")
        time.sleep(1)

    print(f"{Color.MAGENTA}{Color.BOLD}🎉 You scored {h_score}/3 on the beginner checkpoint! You're ready for real terminal work!{Color.RESET}\n")
    input(f"{Color.DIM}Press Enter to return to the main menu...{Color.RESET}")

# ----------------- COMMAND CHALLENGES BY DIFFICULTY -----------------

CHALLENGES_LOW = [
    {
        "concept": "🌱 Step 1: Planting Your First Checkpoint Station",
        "human_story": "You just made a brand-new folder on your computer for a project.\n  Before Git can track anything, you need to turn this regular folder into a Git repository.",
        "analogy": "🎮 Like clicking 'New Game' or planting your very first campfire save point in Dark Souls.",
        "task": "Initialize a brand-new Git repository inside this folder:",
        "valid": ["git init", "git init ."],
        "easy_hint": "git init",
        "why": "This creates an invisible '.git' folder where Git stores all your snapshots."
    },
    {
        "concept": "👀 Step 2: Looking Inside Your Adventure Bag",
        "human_story": "You added or modified some files in your folder.\n  You want to ask Git: 'Hey, what files are changed, new, or waiting to be saved?'",
        "analogy": "🎒 Like peeking into your backpack to inspect what loot you're carrying before saving.",
        "task": "Check the status of all your working files:",
        "valid": ["git status", "git st", "git status -s", "git status --short"],
        "easy_hint": "git status (or shortcut: git st)",
        "why": "Never commit blindly! 'git status' is a developer's most-used daily command."
    },
    {
        "concept": "🛒 Step 3: Putting Items in the Shopping Cart",
        "human_story": "Git never saves your files automatically without your permission.\n  You must gather the files you want to include in the upcoming save point.",
        "analogy": "🛒 Like placing items into your Amazon shopping cart before hitting Checkout.",
        "task": "Stage (pack) ALL modified files in the current folder (use the dot '.'):",
        "valid": ["git add .", "git add -A", "git add --all"],
        "easy_hint": "git add .",
        "why": "The dot '.' means 'everything in this directory'. Now your files are staged!"
    },
    {
        "concept": "💾 Step 4: Sealing Your Save Point with a Note",
        "human_story": "Your files are staged in the cart! Now you want to permanently lock in the save point\n  with a short note describing what you accomplished.",
        "analogy": "📸 Like taking a snapshot and writing a caption on the back of the photo.",
        "task": "Commit your staged files with the message: 'first save':",
        "valid": [
            'git commit -m "first save"',
            "git commit -m 'first save'",
            'git commit -m"first save"',
            "git commit -m'first save'",
            "git commit -m first save"
        ],
        "easy_hint": 'git commit -m "first save"',
        "why": "The '-m' flag attaches a message. Unlabeled save points confuse future-you!"
    },
    {
        "concept": "📜 Step 5: Reading the History Book",
        "human_story": "You want to look back in time and view the chronological list of all checkpoints you made.",
        "analogy": "📖 Like opening your diary to see every past save point with its date and message.",
        "task": "View your project's commit history log:",
        "valid": ["git log", "git lg", "git log --oneline", "git log -n 5"],
        "easy_hint": "git log (or shortcut: git lg)",
        "why": "Lists each commit's unique SHA code, author, date, and description."
    }
]

CHALLENGES_MEDIUM = [
    {
        "concept": "🌿 Step 1: Branching into a Parallel Universe",
        "human_story": "You want to test a crazy new idea without risking breaking your working code on 'main'.",
        "analogy": "🌌 Creating an alternate timeline: if it works, merge it; if it fails, delete it with zero damage.",
        "task": "Create a new branch called 'feature' and switch to it in ONE command:",
        "valid": ["git checkout -b feature", "git switch -c feature"],
        "hint": "git checkout -b feature (or modern: git switch -c feature)",
        "why": "The '-b' flag means 'create a new branch and jump onto it immediately'."
    },
    {
        "concept": "🔀 Step 2: Teleporting Back to Home Base",
        "human_story": "You finished inspecting your experiment. Now you want to hop back to the existing 'main' branch.",
        "analogy": "🏠 Teleporting back to your home base timeline.",
        "task": "Switch back to the existing branch named 'main':",
        "valid": ["git checkout main", "git switch main"],
        "hint": "git checkout main (or: git switch main)",
        "why": "No '-b' here because 'main' already exists — you're just switching to it!"
    },
    {
        "concept": "☁️ Step 3: Backing Up Your Work to the Cloud",
        "human_story": "Your commits exist only on your laptop right now. If your laptop falls in pasta sauce, it's gone!\n  You want to upload your 'main' branch commits to the remote cloud server ('origin').",
        "analogy": "☁️ Cloud Save syncing your game progress to PlayStation Cloud or Steam.",
        "task": "Push your local 'main' branch commits to remote 'origin':",
        "valid": ["git push origin main", "git push", "git push -u origin main"],
        "hint": "git push origin main",
        "why": "'origin' is the nickname of your GitHub repo, and 'main' is the branch."
    },
    {
        "concept": "📥 Step 4: Downloading Teammate Updates",
        "human_story": "Your teammate Prajwal pushed changes to GitHub. You want to fetch AND combine their latest commits into your local folder.",
        "analogy": "📦 Downloading and applying the latest game patch.",
        "task": "Pull the latest commits from the remote repository:",
        "valid": ["git pull", "git pull origin main"],
        "hint": "git pull",
        "why": "'git pull' downloads (fetch) and combines (merge) remote changes in one step."
    },
    {
        "concept": "🎯 Step 5: Packing Only One Specific File",
        "human_story": "You edited 5 different files, but you only want to stage 'index.html' for this specific commit.",
        "analogy": "🛒 Putting only pasta into your shopping cart, leaving sauce for later.",
        "task": "Stage ONLY the file named 'index.html':",
        "valid": ["git add index.html"],
        "hint": "git add index.html",
        "why": "Instead of 'git add .', specifying a filename stages only that particular file."
    }
]

CHALLENGES_HIGH = [
    {
        "concept": "🛡️ Emergency 1: The Safe Public Undo",
        "human_story": "You pushed bad commit 'abc123' to GitHub. Teammates already pulled it! You cannot delete it without breaking their repos.",
        "analogy": "🩹 Publishing an official counter-transaction or correction note instead of rewriting history.",
        "task": "Safely undo commit 'abc123' by creating a public inverse commit:",
        "valid": ["git revert abc123", "git revert abc123 --no-edit", "git revert --no-edit abc123"],
        "hint": "git revert abc123",
        "why": "'git revert' creates a brand-new commit that undoes the changes cleanly and safely."
    },
    {
        "concept": "🧹 Emergency 2: The Digital Junk Drawer (Stash)",
        "human_story": "You're half-way through typing messy code, but an urgent bug arrives on 'main'. You don't want to commit half-baked code.",
        "analogy": "🧹 Sweeping your messy room under the rug temporarily so guests can walk in.",
        "task": "Temporarily shelve your dirty uncommitted changes with a stash:",
        "valid": ["git stash", "git stash save", "git stash push"],
        "hint": "git stash",
        "why": "Your working tree becomes 100% clean, letting you switch branches freely."
    },
    {
        "concept": "📦 Emergency 3: Pulling Work Back Out of the Drawer",
        "human_story": "You fixed the urgent bug! Now you're back on your branch and want your unfinished work back on your desk.",
        "analogy": "🧰 Pulling your tools back out of the toolbox onto your workbench.",
        "task": "Re-apply and remove your latest stashed changes in one step:",
        "valid": ["git stash pop", "git stash apply"],
        "hint": "git stash pop (or: git stash apply)",
        "why": "'pop' applies the stashed changes and deletes the stash item in one go."
    },
    {
        "concept": "🏷️ Milestone: Slapping an Official Release Sticker",
        "human_story": "Your software is ready for launch! You want to mark the current commit as official milestone 'v1.0'.",
        "analogy": "🏆 Pressing a permanent gold wax seal 'v1.0' onto the document.",
        "task": "Create a lightweight tag named 'v1.0':",
        "valid": ["git tag v1.0", "git tag -a v1.0 -m 'v1.0'", 'git tag -a v1.0 -m "v1.0"'],
        "hint": "git tag v1.0",
        "why": "Tags are permanent, human-friendly bookmarks used for version releases."
    },
    {
        "concept": "🕵️ The Black Box Flight Recorder (Reflog)",
        "human_story": "Someone ran 'git reset --hard' by accident! A commit seems completely gone from the log. You need the black box recorder.",
        "analogy": "📼 Rewinding the security camera footage to find where a dropped item fell.",
        "task": "View the reflog history of all HEAD movements:",
        "valid": ["git reflog", "git reflog show"],
        "hint": "git reflog",
        "why": "'git reflog' records every single movement of HEAD. In Git, almost nothing is truly lost!"
    }
]

def run_arena_level(level_name, challenges, level_color):
    clear_screen()
    print(f"{level_color}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║   🎯 PRACTICE ARENA: {level_name:<45}║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Color.RESET}\n")
    print(f"{Color.DIM}[Tip: Type 'menu' or '0' at any prompt to return to Main Menu. Type 'hint' for help!]{Color.RESET}\n")

    score = 0
    total = len(challenges)

    for i, ch in enumerate(challenges, 1):
        print(f"\n{level_color}{Color.BOLD}─── CHALLENGE {i}/{total}: {ch['concept']} ───{Color.RESET}")
        print(f"\n{Color.BOLD}📖 What's happening:{Color.RESET}\n  {ch['human_story']}")
        print(f"\n{Color.CYAN}{Color.BOLD}🎮 Human Analogy:{Color.RESET}\n  {ch['analogy']}")
        print(f"\n{Color.YELLOW}{Color.BOLD}🎯 Your Task:{Color.RESET}\n  {ch['task']}")
        
        # In Easy / Low mode: Give the hint right upfront!
        if "easy_hint" in ch:
            print(f"\n  {Color.GREEN}💡 Helpful Hint: Just type: {Color.BOLD}{ch['easy_hint']}{Color.RESET}")
        
        attempts = 0
        max_attempts = 2
        while attempts < max_attempts:
            prompt_str = f"\n{Color.DIM}[Type command, 'hint', or '0' / 'menu' to exit]{Color.RESET}\n{Color.BOLD}{Color.CYAN}$ {Color.RESET}"
            user_cmd = input(prompt_str).strip()
            
            # Check for home / main menu navigation
            if user_cmd.lower() in ["0", "menu", "home", "back", "exit", "q"]:
                print(f"\n{Color.YELLOW}🏠 Returning to Main Menu...{Color.RESET}\n")
                time.sleep(0.6)
                return False  # Do not replay, go to main menu
            
            # Check for explicit hint request
            if user_cmd.lower() == "hint":
                hint_text = ch.get("easy_hint") or ch.get("hint")
                print(f"  {Color.YELLOW}💡 Hint:{Color.RESET} {Color.BOLD}{hint_text}{Color.RESET}")
                continue
            
            if not user_cmd:
                continue
            
            # Normalize whitespace and quotes
            normalized = " ".join(user_cmd.split())
            
            # Match against valid solutions
            is_valid = normalized in ch["valid"]
            if not is_valid:
                # Check with quotes normalized (e.g. ' -> ")
                alt_normalized = normalized.replace("'", '"')
                alt_valid = [v.replace("'", '"') for v in ch["valid"]]
                is_valid = alt_normalized in alt_valid

            if is_valid:
                points = 100 if attempts == 0 else 50
                score += points
                print(f"\n{Color.GREEN}{Color.BOLD}✅ PERFECT! (+{points} pts){Color.RESET}")
                print(f"  {Color.GREEN}💡 Why this works:{Color.RESET} {ch['why']}\n")
                break
            else:
                attempts += 1
                hint_text = ch.get("easy_hint") or ch.get("hint")
                if attempts < max_attempts:
                    print(f"\n{Color.RED}❌ Close, but not quite!{Color.RESET}")
                    print(f"   {Color.YELLOW}💡 Try this:{Color.RESET} {Color.BOLD}{hint_text}{Color.RESET}")
                else:
                    print(f"\n{Color.RED}❌ Out of attempts! Expected command:{Color.RESET} {Color.BOLD}{hint_text}{Color.RESET}")
                    print(f"  {Color.DIM}💡 Why this works: {ch['why']}{Color.RESET}\n")
        
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

