#!/usr/bin/env python3
"""
🎮 JUST LEARNING GIT - THE INTERACTIVE TERMINAL GAME
Author: Prajwal D. Chonnad
Repository: prajwalchonnad/just-learning-git-

An interactive, laugh-out-loud Git learning adventure and VTU BCS358C lab exam survival trainer.
"""

import sys
import time
import random
import os

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

def print_slow(text, delay=0.015, color=""):
    """Prints text with a subtle typing effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Color.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

BANNER = f"""
{Color.RED}       __           __     __                               __             _______ __  
{Color.YELLOW}      |__.--.--.---.|  |_  |  .-----.---.-.----.-----.--.--.--|  .-----       |   _   |__.  |_
{Color.GREEN}      |  |  |  |__ --|   _| |  |  -__|  _  |   _|     |  |  |  _  |  _  |      |.  |   |  |   _|
{Color.CYAN}     ___ |_____|_____|____| |__|_____|___._|__| |__|__|___  |___._|___  |      |.  |   |__|____|
{Color.BLUE}    |_____|                                            |_____|     |_____|      |:  1   /        
{Color.MAGENTA}                                                                                |::.. . /  THE GAME
{Color.WHITE}                                                                                `------'   
{Color.BOLD}                     🚀 The Official VTU Lab & Comedy Survival Simulator 🍝
{Color.RESET}"""

# ----------------- GAME DATA -----------------

VIVA_QUESTIONS = [
    {
        "q": "External Examiner walks in: 'Student, what is the exact difference between git fetch and git pull?'",
        "options": [
            "A) They are identical; Linus Torvalds just liked having two names for fun.",
            "B) git fetch downloads remote changes without merging; git pull fetches AND merges them.",
            "C) git fetch is for GitHub, git pull is for GitLab.",
            "D) git pull only works if you yell at your keyboard in Italian."
        ],
        "ans": "B",
        "tip": "VTU Exp 5: git fetch is safe and doesn't touch your working tree. git pull = fetch + merge!",
        "praise": "Examiner nods slowly and sips canteen chai: 'Good. Full marks.'",
        "roast": "Examiner stares with intense disappointment. 'Next time, attend the 8 AM lecture.'"
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
        "tip": "VTU Exp 12: git revert creates a NEW commit that inverses past changes without breaking shared remote history!",
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
        "tip": "VTU Exp 3: git stash temporarily shelves uncommitted modifications so you can switch branches cleanly!",
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
        "tip": "VTU Exp 8: In git, A..B excludes A. The caret ^ (A^..B) makes it include commit A as well!",
        "praise": "Spot on! That caret '^' is the trickiest question on the VTU syllabus.",
        "roast": "Remember the caret! 'A^..B' includes commit A, while 'A..B' skips commit A."
    },
    {
        "q": "Examiner points to your screen: 'What does this command do: git log --author=\"JohnDoe\" --since=\"2024-01-01\"'?",
        "options": [
            "A) Deletes all commits by JohnDoe after 2024",
            "B) Changes the author of all commits to JohnDoe",
            "C) Filters the commit history to display only commits by JohnDoe since Jan 1, 2024",
            "D) Sends an angry email to JohnDoe"
        ],
        "ans": "C",
        "tip": "VTU Exp 10: git log supports powerful filters like --author, --since, and --until.",
        "praise": "Textbook definition! You're dominating this viva.",
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
        "tip": "VTU Exp 7: git tag v1.0 is lightweight. git tag -a v1.0 -m 'Release' is annotated.",
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
        "tip": "VTU Exp 6: Merging brings histories together and allows an explicit custom commit message.",
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
        "story": "Your teammate accidentally staged an '.env' file containing API keys into the Git staging area. It hasn't been committed yet!",
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

VTU_EXPERIMENTS = [
    ("Exp 01", "Setting Up and Basic Commands", "git init\necho 'Hello' > file.txt\ngit add file.txt\ngit commit -m 'Initial commit'"),
    ("Exp 02", "Creating and Managing Branches", "git checkout -b feature-branch\n# make changes\ngit checkout master\ngit merge feature-branch"),
    ("Exp 03", "Stashing Changes", "git stash save 'WIP'\ngit checkout master\n# do urgent work\ngit checkout feature-branch\ngit stash apply"),
    ("Exp 04", "Cloning a Remote Repository", "git clone https://github.com/user/repo.git"),
    ("Exp 05", "Fetch and Rebase", "git checkout main\ngit fetch origin\ngit rebase origin/main"),
    ("Exp 06", "Merge with Custom Commit Message", "git checkout master\ngit merge feature-branch -m 'Custom merge message'"),
    ("Exp 07", "Git Tags and Releases", "git tag v1.0\n# or annotated:\ngit tag -a v1.0 -m 'Release v1.0'"),
    ("Exp 08", "Cherry-Picking a Range of Commits", "git cherry-pick start_commit^..end_commit"),
    ("Exp 09", "Inspecting a Specific Commit", "git show <commit-id>\n# or summary only:\ngit log -n 1 <commit-id>"),
    ("Exp 10", "Filtering by Author and Date Range", "git log --author='JohnDoe' --since='2023-01-01' --until='2023-12-31'"),
    ("Exp 11", "Display Last 5 Commits", "git log -n 5 --oneline"),
    ("Exp 12", "Undoing Changes via Revert", "git revert <commit-id> --no-edit")
]

# ----------------- GAME MODES -----------------

def mode_viva_gauntlet():
    clear_screen()
    print(f"{Color.CYAN}{Color.BOLD}╔════════════════════════════════════════════════════════════════════╗")
    print("║          🎓 MODE 1: SURVIVE THE VTU VIVA-VOCE EXAMINER             ║")
    print("╚════════════════════════════════════════════════════════════════════╝\n")
    print_slow("An external examiner walks into the lab with a pen, a clipboard, and zero patience.", 0.02, Color.YELLOW)
    print_slow("Answer the questions correctly to earn your engineering marks. You have 3 lives (☕ Coffee Cups).\n", 0.02)
    
    score = 0
    lives = 3
    questions = list(VIVA_QUESTIONS)
    random.shuffle(questions)

    for i, item in enumerate(questions[:5], 1):
        print(f"\n{Color.BOLD}{Color.WHITE}─── ROUND {i}/5 | Lives: {'☕ ' * lives} | Score: {score} ───{Color.RESET}")
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
                print_slow(f"\n{Color.RED}{Color.BOLD}💀 OUT OF LIVES! The examiner sent you to the supplementary exam!{Color.RESET}", 0.03)
                break
        
        print(f"{Color.DIM}💡 Tip: {item['tip']}{Color.RESET}")
        time.sleep(1.5)

    print(f"\n{Color.BOLD}{Color.MAGENTA}═══════════════════════════════════════════════════")
    print(f"   VIVA FINISHED! Final Score: {score}/500")
    if score >= 400:
        print(f"   🏆 Grade: S-Rank! You are the Lab Topper!")
    elif score >= 200:
        print(f"   ⭐ Grade: B-Rank! You passed with dignity!")
    else:
        print(f"   🧄 Grade: Burnt Garlic Rookie. Time to re-read the lab manual!")
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
    print("║       📚 MODE 3: VTU BCS358C 12-IN-1 INTERACTIVE CHEATBOOK         ║")
    print("╚════════════════════════════════════════════════════════════════════╝\n")
    print("Select an experiment number to view the exact exam code & solution:\n")

    for idx, (exp_code, name, _) in enumerate(VTU_EXPERIMENTS, 1):
        print(f"  {Color.YELLOW}[{idx:2d}] {exp_code}: {name}{Color.RESET}")

    print(f"\n  {Color.CYAN}[ 0] Return to Main Menu{Color.RESET}")

    while True:
        try:
            choice = int(input(f"\n{Color.BOLD}Enter Experiment [1 - 12] or 0 to exit: {Color.RESET}").strip())
            if choice == 0:
                return
            if 1 <= choice <= 12:
                exp_code, name, code = VTU_EXPERIMENTS[choice - 1]
                print(f"\n{Color.GREEN}{Color.BOLD}═════════════════════════════════════════════════════")
                print(f"📖 {exp_code}: {name}")
                print(f"═════════════════════════════════════════════════════{Color.RESET}")
                print(f"{Color.WHITE}{code}{Color.RESET}")
                print(f"{Color.GREEN}═════════════════════════════════════════════════════{Color.RESET}")
        except ValueError:
            pass

def main():
    while True:
        clear_screen()
        print(BANNER)
        print(f"{Color.BOLD}Welcome to the interactive Git arcade! Choose your adventure:{Color.RESET}\n")
        print(f"  {Color.CYAN}[1]{Color.RESET} 🎓 Survive the VTU Viva-Voce (Boss Battle)")
        print(f"  {Color.RED}[2]{Color.RESET} 🚨 'Oh No, Git!' Disaster Scenarios")
        print(f"  {Color.GREEN}[3]{Color.RESET} 📚 12-in-1 VTU BCS358C Lab Cheatbook")
        print(f"  {Color.YELLOW}[4]{Color.RESET} ⚡ Show My Configured Git Aliases")
        print(f"  {Color.MAGENTA}[5]{Color.RESET} 🏃 Exit to Terminal")
        
        choice = input(f"\n{Color.BOLD}Enter your choice [1 - 5]: {Color.RESET}").strip()

        if choice == "1":
            mode_viva_gauntlet()
        elif choice == "2":
            mode_disaster_recovery()
        elif choice == "3":
            mode_vtu_cheatbook()
        elif choice == "4":
            clear_screen()
            print(f"\n{Color.YELLOW}{Color.BOLD}⚡ YOUR SUPERCHARGED GIT ALIASES:{Color.RESET}\n")
            print(f"  {Color.CYAN}git st{Color.RESET}    -> Instant status check")
            print(f"  {Color.CYAN}git lg{Color.RESET}    -> Clean, one-line commit log")
            print(f"  {Color.CYAN}git files{Color.RESET} -> View commits with file names and stats")
            print(f"  {Color.CYAN}git last{Color.RESET}  -> Deep inspection of the latest commit\n")
            input(f"{Color.DIM}Press Enter to return...{Color.RESET}")
        elif choice in ["5", "q", "exit"]:
            print(f"\n{Color.GREEN}Keep committing like a ninja! Bye Prajwal! 🚀{Color.RESET}\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Color.YELLOW}Game exited. See you in the commits! 👋{Color.RESET}\n")
