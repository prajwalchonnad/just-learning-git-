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

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Auto-launch into a dedicated spacious window on Windows
if sys.platform == "win32" and "--new-window" not in sys.argv and "--no-window" not in sys.argv:
    script_path = os.path.abspath(__file__)
    cmd = f'start "JUST LEARNING GIT - Arcade" cmd /c "mode con: cols=108 lines=40 && python \\"{script_path}\\" --new-window"'
    os.system(cmd)
    print("\n\033[92m[*] Launching 'JUST LEARNING GIT' in a new dedicated arcade window! Ready!\033[0m\n")
    sys.exit(0)

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
{Color.YELLOW}{Color.BOLD}            🚀 The Universal Git Learning Arcade & Developer Survival Simulator 🍝
{Color.RESET}"""

# ----------------- GAME DATA -----------------

VIVA_QUESTIONS = [
    {
        "q": "Senior Engineer / Examiner asks: 'What is the exact difference between git fetch and git pull?'",
        "options": [
            "A) They are identical; Linus Torvalds just liked having two names for fun.",
            "B) git fetch downloads remote changes without merging; git pull fetches AND merges them.",
            "C) git fetch is for GitHub, git pull is for GitLab.",
            "D) git pull only works if you yell at your keyboard in Italian."
        ],
        "ans": "B",
        "tip": "Core Concept: git fetch is safe and doesn't touch your working tree. git pull = fetch + merge!",
        "praise": "Interviewer nods with respect: 'Clean, accurate answer. You know your Git.'",
        "roast": "Interviewer writes a red mark in their notepad. 'Time to brush up on remote syncing!'"
    },
    {
        "q": "You made a disastrous commit with bugs directly on 'main' and ALREADY PUSHED IT to GitHub. What command safely undoes it?",
        "options": [
            "A) git reset --hard HEAD~1 (The nuclear option)",
            "B) git revert <commit-id>",
            "C) Delete your GitHub account and move to the Himalayas",
            "D) Turn off your laptop and pretend the power went out"
        ],
        "ans": "B",
        "tip": "Safety First: git revert creates a NEW commit that inverses past changes without breaking shared remote history!",
        "praise": "You saved the team's shared history! Nonna smiles upon you.",
        "roast": "If you ran git reset --hard on a pushed branch, your teammates' git trees are now on fire."
    },
    {
        "q": "You are half-way through writing code on a feature, but an emergency bug arrives on 'main'. You don't want to commit messy half-done code. What do you run?",
        "options": [
            "A) git stash save 'work in progress'",
            "B) git delete --quick",
            "C) Copy-paste your files to Desktop/backup_final_v2_really_final/",
            "D) git checkout -f main and throw away all progress"
        ],
        "ans": "A",
        "tip": "Pro-tip: git stash temporarily shelves uncommitted modifications so you can switch branches cleanly!",
        "praise": "Clean move! Your digital junk drawer saved your afternoon.",
        "roast": "Never use Desktop folders as a version control system! That's what git stash was born for."
    },
    {
        "q": "How do you cherry-pick a range of commits from commit A up to commit B (inclusive)?",
        "options": [
            "A) git cherry-pick A..B",
            "B) git cherry-pick A^..B",
            "C) git cherry-pick --all A B",
            "D) git grab A through B please"
        ],
        "ans": "B",
        "tip": "Range Syntax: In Git, A..B excludes A. The caret ^ (A^..B) makes it include commit A as well!",
        "praise": "Spot on! That caret '^' is the secret handshake of senior Git pros.",
        "roast": "Remember the caret! 'A^..B' includes commit A, while 'A..B' skips commit A."
    },
    {
        "q": "Your lead points to your terminal: 'What does this command do: git log --author=\"JohnDoe\" --since=\"2024-01-01\"'?",
        "options": [
            "A) Deletes all commits by JohnDoe after 2024",
            "B) Changes the author of all commits to JohnDoe",
            "C) Filters the commit history to display only commits by JohnDoe since Jan 1, 2024",
            "D) Sends an angry email to JohnDoe"
        ],
        "ans": "C",
        "tip": "Log Power: git log supports powerful filters like --author, --since, and --until.",
        "praise": "Textbook definition! You're dominating this interview.",
        "roast": "Nope! It filters history. JohnDoe didn't receive any angry emails."
    },
    {
        "q": "What is the difference between a lightweight tag and an annotated tag in Git?",
        "options": [
            "A) Lightweight tags have fewer calories.",
            "B) Lightweight tags are just pointers/bookmarks to a commit; annotated tags store full author, date, and message metadata.",
            "C) Annotated tags can only be created on Sundays.",
            "D) There is no difference, it's a marketing gimmick."
        ],
        "ans": "B",
        "tip": "Versioning: git tag v1.0 is lightweight. git tag -a v1.0 -m 'Release' is annotated.",
        "praise": "Exactly right. Always use annotated tags for formal public software releases!",
        "roast": "Not quite! Lightweight tags are simple bookmarks (SHA pointers). Annotated tags have full metadata."
    },
    {
        "q": "What happens when you run 'git merge feature-branch -m \"Custom message\"'?",
        "options": [
            "A) It deletes the feature branch immediately.",
            "B) It integrates feature-branch into the current branch with a custom merge commit message.",
            "C) It converts all code to Python.",
            "D) It opens Microsoft Word."
        ],
        "ans": "B",
        "tip": "Branch Integration: Merging brings histories together and allows an explicit custom commit message.",
        "praise": "Clean merge! Alternate timelines united peacefully.",
        "roast": "No Word documents involved here! It merges branches and attaches your custom message."
    }
]

DISASTER_SCENARIOS = [
    {
        "title": "🍝 Disaster at the Italian Trattoria",
        "story": "Matteo caught someone snapping dry spaghetti in half before putting it into the boiling pot! The perpetrator panicked and committed 'spaghetti_halved.py' to main.",
        "prompt": "You need to undo this tragic commit (ID: 'pastas1n') safely without rewriting history for the rest of the kitchen. What do you run?",
        "choices": [
            "git revert pastas1n --no-edit",
            "git reset --hard HEAD~1",
            "git rm -rf .",
            "git blame matteo"
        ],
        "ans_idx": 1,
        "reaction": "✅ Matteo smiles. The universe is restored to order. Al dente achieved."
    },
    {
        "title": "💣 The Accidental Secret Leak",
        "story": "Your teammate accidentally staged an '.env' file containing secret API keys into the Git staging area. It hasn't been committed yet!",
        "prompt": "How do you unstage '.env' without losing the file on disk?",
        "choices": [
            "rm -f .env",
            "git restore --staged .env",
            "git push origin main",
            "git checkout -b secrets"
        ],
        "ans_idx": 2,
        "reaction": "✅ Secret saved from staging! Add it to .gitignore immediately."
    },
    {
        "title": "⚡ The Accidental Hard Reset Catastrophe",
        "story": "You ran 'git reset --hard' by accident and now your latest 3 commits seem completely gone. Your heart rate is 180 BPM.",
        "prompt": "Which miraculous Git safety net tool lets you find and recover the lost commit SHA?",
        "choices": [
            "git panic",
            "git reflog",
            "git undo-everything",
            "git restart-computer"
        ],
        "ans_idx": 2,
        "reaction": "✅ git reflog records every single movement of HEAD! You recovered the lost SHA like a magician."
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
            choice = input(f"\n{Color.BOLD}Your Answer [A / B / C / D]: {Color.RESET}").strip().upper()
            if choice in ["A", "B", "C", "D"]:
                break
            print(f"{Color.RED}Please type A, B, C, or D!{Color.RESET}")

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
            try:
                pick = int(input(f"\n{Color.BOLD}Select your tool [1 - 4]: {Color.RESET}").strip())
                if 1 <= pick <= 4:
                    break
            except ValueError:
                pass
            print(f"{Color.RED}Enter a number from 1 to 4!{Color.RESET}")

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
    
    input(f"{Color.YELLOW}Hit [Enter] to see how Git fixes this madness...{Color.RESET}")

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

    input(f"{Color.YELLOW}Hit [Enter] to play the 'Save & Catastrophe' simulation...{Color.RESET}")

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
    
    ans = input(f"\n{Color.BOLD}Your choice [1 or 2]: {Color.RESET}").strip()
    if ans == "1":
        print(f"\n{Color.GREEN}{Color.BOLD}🎉 EXACTLY! That is 'git branch' and 'git merge'. You only merge if it tastes good!{Color.RESET}\n")
    else:
        print(f"\n{Color.YELLOW}Ordering food is tempting, but with Git, Timeline A was 100% safe all along!{Color.RESET}\n")

    print_slow(f"{Color.CYAN}Summary: You don't need to be a computer genius to use Git.", 0.02)
    print_slow("You just need to know: Checkpoints (commit), Parallel Timelines (branch), and Cloud Saves (push).", 0.02)
    print_slow(f"Congratulations! You now understand 90% of Git concepts! 🚀{Color.RESET}\n", 0.02)
    input(f"{Color.DIM}Press Enter to return to the main menu...{Color.RESET}")

def main():
    while True:
        clear_screen()
        print(BANNER)
        print(f"{Color.BOLD}Welcome to the interactive Git arcade! Choose your adventure:{Color.RESET}\n")
        print(f"  {Color.YELLOW}[1]{Color.RESET} 🐣 'Git for Humans' (Story Mode: Explain Like I'm 5 & Find Git Boring)")
        print(f"  {Color.CYAN}[2]{Color.RESET} 🎓 Survive the Tech Interview & Viva (Boss Battle)")
        print(f"  {Color.RED}[3]{Color.RESET} 🚨 'Oh No, Git!' Disaster Scenarios")
        print(f"  {Color.GREEN}[4]{Color.RESET} 📚 12-Step Practical Lab & Workflow Cheatbook")
        print(f"  {Color.BLUE}[5]{Color.RESET} ⚡ Show My Configured Git Aliases")
        print(f"  {Color.MAGENTA}[6]{Color.RESET} 🏃 Exit to Terminal")
        
        choice = input(f"\n{Color.BOLD}Enter your choice [1 - 6]: {Color.RESET}").strip()

        if choice == "1":
            mode_git_for_humans()
        elif choice == "2":
            mode_viva_gauntlet()
        elif choice == "3":
            mode_disaster_recovery()
        elif choice == "4":
            mode_vtu_cheatbook()
        elif choice == "5":
            clear_screen()
            print(f"\n{Color.YELLOW}{Color.BOLD}⚡ YOUR SUPERCHARGED GIT ALIASES:{Color.RESET}\n")
            print(f"  {Color.CYAN}git st{Color.RESET}    -> Instant status check")
            print(f"  {Color.CYAN}git lg{Color.RESET}    -> Clean, one-line commit log")
            print(f"  {Color.CYAN}git files{Color.RESET} -> View commits with file names and stats")
            print(f"  {Color.CYAN}git last{Color.RESET}  -> Deep inspection of the latest commit\n")
            input(f"{Color.DIM}Press Enter to return...{Color.RESET}")
        elif choice in ["6", "q", "exit"]:
            print(f"\n{Color.GREEN}Keep committing like a ninja! Bye Prajwal! 🚀{Color.RESET}\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Color.YELLOW}Game exited. See you in the commits! 👋{Color.RESET}\n")

