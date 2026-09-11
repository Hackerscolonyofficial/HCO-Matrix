#!/usr/bin/env python3

import os
import sys
import time
import subprocess
import getpass
import requests


# ============================================================
# HCO MATRIX CONFIG
# ============================================================

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openrouter/free"

YOUTUBE_URL = (
    "https://youtube.com/@hackers_colony_tech"
    "?si=aojETEUcjhSIYUXB"
)


# ============================================================
# COLORS
# ============================================================

RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"


# ============================================================
# AI SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = (
    "You are HCO Matrix, a helpful command-line AI assistant. "
    "Give clear, practical and concise answers. "
    "For cybersecurity questions, focus on legal, authorized, "
    "defensive, and educational use."
)


# ============================================================
# CLEAR SCREEN
# ============================================================

def clear():
    os.system("clear")


# ============================================================
# HCO LOGO
# ============================================================

def hco_logo():

    print(f"{CYAN}{BOLD}")

    print("██╗  ██╗ ██████╗ ██████╗ ")
    print("██║  ██║██╔════╝██╔═══██╗")
    print("███████║██║     ██║   ██║")
    print("██╔══██║██║     ██║   ██║")
    print("██║  ██║╚██████╗╚██████╔╝")
    print("╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ")

    print(f"{YELLOW}          M A T R I X{RESET}")

    print()

    print(
        f"{MAGENTA}{BOLD}"
        "      Code by Azhar (A-Z-H-A-R)"
        f"{RESET}"
    )

    print(
        f"{GREEN}{BOLD}"
        "             [ HCO Team ]"
        f"{RESET}"
    )

    print()


# ============================================================
# SMALL BANNER
# ============================================================

def small_banner():

    print(f"{CYAN}{BOLD}")

    print(
        "╔══════════════════════════════════════════════════════════╗"
    )

    print(
        "║                       HCO MATRIX                         ║"
    )

    print(
        "║             AI Command-Line Assistant                    ║"
    )

    print(
        "╚══════════════════════════════════════════════════════════╝"
    )

    print(f"{RESET}")


# ============================================================
# OPEN YOUTUBE
# ============================================================

def open_youtube():

    commands = [

        # Termux
        [
            "termux-open-url",
            YOUTUBE_URL
        ],

        # Android
        [
            "am",
            "start",
            "-a",
            "android.intent.action.VIEW",
            YOUTUBE_URL
        ],

        # Linux
        [
            "xdg-open",
            YOUTUBE_URL
        ],
    ]

    for command in commands:

        try:

            result = subprocess.run(
                command,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            if result.returncode == 0:
                return True

        except FileNotFoundError:
            continue

        except Exception:
            continue

    return False


# ============================================================
# STARTUP LOCK SCREEN
# ============================================================

def startup_screen():

    clear()

    print(f"{RED}{BOLD}")

    print(
        "╔══════════════════════════════════════════════════════════╗"
    )

    print(
        "║                                                          ║"
    )

    print(
        "║                    🔒 TOOL LOCKED 🔒                    ║"
    )

    print(
        "║                                                          ║"
    )

    print(
        "╚══════════════════════════════════════════════════════════╝"
    )

    print(f"{RESET}")

    print()

    print(
        f"{WHITE}"
        "To use HCO Matrix, you will be redirected to the\n"
        "Hackers Colony Tech YouTube channel."
        f"{RESET}"
    )

    print()

    print(f"{YELLOW}{BOLD}")
    print("📺 HACKERS COLONY TECH")
    print()
    print("👍 Like the content")
    print("🔔 Subscribe / enable the bell if you enjoy the content")
    print("↩️  Then come back to this terminal")
    print(f"{RESET}")

    print()

    print(f"{CYAN}{BOLD}🔗 Channel:{RESET}")
    print(YOUTUBE_URL)

    print()

    print(
        f"{MAGENTA}{BOLD}"
        "⚡ Opening Hackers Colony Tech automatically..."
        f"{RESET}"
    )

    print()

    print(f"{BLUE}{BOLD}Opening YouTube in:{RESET}")

    print()

    # 8 → 0 countdown
    for number in range(8, -1, -1):

        print(
            f"\r{YELLOW}{BOLD}"
            f"                    {number}"
            f"{RESET}",
            end="",
            flush=True
        )

        time.sleep(1)

    print()
    print()

    print(
        f"{GREEN}{BOLD}"
        "📱 Opening Hackers Colony Tech..."
        f"{RESET}"
    )

    time.sleep(1)

    opened = open_youtube()

    if not opened:

        print()

        print(
            f"{YELLOW}"
            "⚠️ Automatic YouTube opening is unavailable."
            f"{RESET}"
        )

        print()

        print(
            f"{WHITE}"
            "Please open the channel manually:"
            f"{RESET}"
        )

        print(YOUTUBE_URL)

    print()

    input(
        f"{CYAN}{BOLD}"
        "↩️  Come back here and press ENTER to unlock HCO Matrix..."
        f"{RESET}"
    )


# ============================================================
# API KEY INPUT
# ============================================================

def get_api_key():

    clear()

    print(f"{GREEN}{BOLD}")

    print(
        "╔══════════════════════════════════════════════════════════╗"
    )

    print(
        "║                  🔐 API KEY SETUP                        ║"
    )

    print(
        "╚══════════════════════════════════════════════════════════╝"
    )

    print(f"{RESET}")

    print()

    print(
        f"{WHITE}"
        "HCO Matrix uses your own OpenRouter API key.\n"
        "Your API key is entered locally and is not included\n"
        "inside the GitHub source code."
        f"{RESET}"
    )

    print()

    print(
        f"{YELLOW}"
        "🔑 Enter your OpenRouter API key below."
        f"{RESET}"
    )

    print()

    while True:

        try:

            key = getpass.getpass(
                f"{CYAN}{BOLD}"
                "OpenRouter API Key > "
                f"{RESET}"
            ).strip()

        except (KeyboardInterrupt, EOFError):

            print()

            print(
                f"{RED}"
                "❌ Cancelled."
                f"{RESET}"
            )

            sys.exit(1)

        if key:

            return key

        print()

        print(
            f"{RED}"
            "❌ API key cannot be empty."
            f"{RESET}"
        )

        print()


# ============================================================
# AI REQUEST
# ============================================================

def ask_ai(api_key, messages):

    response = requests.post(

        API_URL,

        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/",
            "X-Title": "HCO Matrix",
        },

        json={
            "model": MODEL,
            "messages": messages,
        },

        timeout=90,
    )

    try:

        data = response.json()

    except ValueError:

        raise RuntimeError(
            f"HTTP {response.status_code}: Invalid API response"
        )

    if response.status_code != 200:

        error = data.get("error", data)

        raise RuntimeError(
            f"API error ({response.status_code}): {error}"
        )

    try:

        return data["choices"][0]["message"]["content"]

    except (KeyError, IndexError, TypeError):

        raise RuntimeError(
            "Unexpected response format from OpenRouter."
        )


# ============================================================
# MAIN MENU
# ============================================================

def show_menu():

    print(f"{BLUE}{BOLD}")

    print(
        "╭────────────────────────────────────────────────────────╮"
    )

    print(
        "│                  ⚡ HCO MATRIX MENU ⚡                  │"
    )

    print(
        "╰────────────────────────────────────────────────────────╯"
    )

    print(f"{RESET}")

    print(f"{CYAN}[1]{RESET} 🤖 Ask AI")

    print(
        f"{GREEN}[2]{RESET} 🐧 Explain Linux / Termux Command"
    )

    print(
        f"{MAGENTA}[3]{RESET} 💻 Code Assistant"
    )

    print(
        f"{RED}[4]{RESET} 🛡️  Cybersecurity Learning"
    )

    print(
        f"{YELLOW}[5]{RESET} 💬 General Question"
    )

    print(
        f"{BLUE}[6]{RESET} 🧹 Clear Conversation"
    )

    print(
        f"{RED}[0]{RESET} 🚪 Exit"
    )

    print()


# ============================================================
# ASSISTANT
# ============================================================

def assistant(api_key):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    prompts = {

        "1":
        "Ask your question",

        "2":
        "Which Linux/Termux command do you want explained?",

        "3":
        "What code do you need help creating or debugging?",

        "4":
        "What cybersecurity topic do you want to learn about?",

        "5":
        "Ask your question",
    }

    while True:

        clear()

        small_banner()

        show_menu()

        try:

            choice = input(
                f"{MAGENTA}{BOLD}"
                "HCO Matrix > "
                f"{RESET}"
            ).strip()

        except (KeyboardInterrupt, EOFError):

            print()

            print(
                f"{GREEN}{BOLD}"
                "Goodbye from HCO Matrix 👋"
                f"{RESET}"
            )

            return

        if choice == "0":

            print()

            print(
                f"{GREEN}{BOLD}"
                "👋 Goodbye from HCO Matrix!"
                f"{RESET}"
            )

            return

        if choice == "6":

            messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                }
            ]

            input(
                f"\n{GREEN}"
                "✓ Conversation cleared. Press ENTER..."
                f"{RESET}"
            )

            continue

        if choice not in prompts:

            input(
                f"\n{RED}"
                "❌ Invalid option. Press ENTER..."
                f"{RESET}"
            )

            continue

        print()

        question = input(
            f"{YELLOW}{BOLD}"
            f"{prompts[choice]} > "
            f"{RESET}"
        ).strip()

        if not question:
            continue

        messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        print()

        print(
            f"{CYAN}{BOLD}"
            "⏳ HCO Matrix is thinking..."
            f"{RESET}"
        )

        try:

            answer = ask_ai(
                api_key,
                messages
            )

        except Exception as error:

            messages.pop()

            input(
                f"\n{RED}"
                f"❌ {error}"
                f"{RESET}\n\n"
                "Press ENTER..."
            )

            continue

        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        clear()

        small_banner()

        print(
            f"{GREEN}{BOLD}"
            "╭────────────────────────────────────────────────────────╮"
        )

        print(
            "│                  🤖 HCO RESPONSE 🤖                   │"
        )

        print(
            "╰────────────────────────────────────────────────────────╯"
            f"{RESET}"
        )

        print()

        print(
            f"{WHITE}"
            f"{answer}"
            f"{RESET}"
        )

        print()

        input(
            f"{CYAN}"
            "Press ENTER to return to HCO Matrix menu..."
            f"{RESET}"
        )


# ============================================================
# MAIN
# ============================================================

def main():

    startup_screen()

    api_key = get_api_key()

    clear()

    print(
        f"{GREEN}{BOLD}"
        "╔══════════════════════════════════════════════════════════╗"
    )

    print(
        "║             🔓 HCO MATRIX UNLOCKED 🔓                   ║"
    )

    print(
        "╚══════════════════════════════════════════════════════════╝"
        f"{RESET}"
    )

    print()

    hco_logo()

    print(
        f"{CYAN}{BOLD}"
        "🚀 Starting HCO Matrix..."
        f"{RESET}"
    )

    time.sleep(2)

    assistant(api_key)


if __name__ == "__main__":
    main()
