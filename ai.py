#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════╗
║                    HCO MATRIX                      ║
║          AI Command-Line Assistant                 ║
║                                                    ║
║              Code by Azhar • HCO Team              ║
╚════════════════════════════════════════════════════╝

Copyright (c) 2026 Hackers Colony Tech
See LICENSE for terms.
"""

import os
import sys
import time
import subprocess
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openrouter/free"
YOUTUBE_URL = "https://youtube.com/@hackers_colony_tech?si=aojETEUcjhSIYUXB"

SYSTEM_PROMPT = (
    "You are HCO Matrix, a helpful command-line AI assistant. "
    "Give clear, practical and concise answers. "
    "For cybersecurity questions, focus on legal, authorized, defensive, "
    "and educational use."
)

# ANSI colors
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
MAGENTA = "\033[1;35m"
BLUE = "\033[1;34m"
WHITE = "\033[1;37m"


def clear():
    os.system("clear")


def banner():
    print(CYAN)
    print("╔════════════════════════════════════════════════════╗")
    print("║                    HCO MATRIX                      ║")
    print("║          AI Command-Line Assistant                 ║")
    print("║                                                    ║")
    print("║              Code by Azhar • HCO Team              ║")
    print("╚════════════════════════════════════════════════════╝")
    print(RESET)


def open_youtube():
    try:
        subprocess.run(
            ["am", "start", "-a", "android.intent.action.VIEW", YOUTUBE_URL],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except FileNotFoundError:
        print(f"\n{YELLOW}Open manually:{RESET}\n{YOUTUBE_URL}")


def startup_screen():
    clear()

    print(RED + BOLD)
    print("╔════════════════════════════════════════════════════╗")
    print("║                  HCO MATRIX                        ║")
    print("║                 TOOL STARTUP                       ║")
    print("╚════════════════════════════════════════════════════╝")
    print(RESET)

    print(f"{WHITE}⚠  Before using HCO Matrix, please support")
    print("   Hackers Colony Tech on YouTube.{RESET}\n")

    print(f"{MAGENTA}📺 You can like the channel, subscribe, and")
    print("   enable notifications if you enjoy the content.")
    print(f"   This is optional and is NOT technically verified.{RESET}\n")

    print(f"{CYAN}🔗 Channel:{RESET}")
    print(YOUTUBE_URL)
    print()

    print(f"{YELLOW}Opening YouTube in:{RESET}\n")

    for number in range(8, -1, -1):
        print(f"{BOLD}{YELLOW}                 {number}{RESET}", end="\r", flush=True)
        time.sleep(1)

    print("\n")
    print(f"{GREEN}📱 Opening Hackers Colony Tech...{RESET}")
    time.sleep(1)
    open_youtube()

    print()
    input(f"{CYAN}Press ENTER to continue to HCO Matrix...{RESET}")


def get_api_key():
    key = os.getenv("OPENROUTER_API_KEY")

    if not key:
        print(f"\n{RED}{BOLD}❌ API KEY NOT FOUND{RESET}\n")
        print("Set your OpenRouter key with:")
        print(f'{YELLOW}export OPENROUTER_API_KEY="YOUR_API_KEY"{RESET}\n')
        sys.exit(1)

    return key


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
        raise RuntimeError(
            f"API error ({response.status_code}): {data}"
        )

    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        raise RuntimeError("Unexpected response format from API.")


def assistant(api_key):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    while True:
        clear()
        banner()

        print(f"{GREEN}{BOLD}╭────────────────────────────────────────────╮")
        print("│              HCO MATRIX MENU               │")
        print("╰────────────────────────────────────────────╯" + RESET)

        print(f"""
{CYAN}[1]{RESET} 🤖 Ask AI
{CYAN}[2]{RESET} 🐧 Explain Linux / Termux Command
{CYAN}[3]{RESET} 💻 Code Assistant
{CYAN}[4]{RESET} 🛡️  Cybersecurity Learning
{CYAN}[5]{RESET} 💬 General Question
{CYAN}[6]{RESET} 🧹 Clear Conversation
{CYAN}[0]{RESET} 🚪 Exit
""")

        choice = input(f"{MAGENTA}HCO Matrix > {RESET}").strip()

        if choice == "0":
            print(f"\n{GREEN}Goodbye from HCO Matrix 👋{RESET}")
            return

        if choice == "6":
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            input(f"\n{GREEN}✓ Conversation cleared. Press ENTER...{RESET}")
            continue

        prompts = {
            "1": "Ask your question",
            "2": "Which Linux/Termux command do you want explained?",
            "3": "What code do you need help creating or debugging?",
            "4": "What cybersecurity topic do you want to learn about?",
            "5": "Ask your question",
        }

        if choice not in prompts:
            input(f"\n{RED}Invalid option. Press ENTER...{RESET}")
            continue

        print()
        question = input(
            f"{YELLOW}{prompts[choice]} > {RESET}"
        ).strip()

        if not question:
            continue

        messages.append({
            "role": "user",
            "content": question,
        })

        print(f"\n{YELLOW}⏳ HCO Matrix is thinking...{RESET}")

        try:
            answer = ask_ai(api_key, messages)
        except Exception as exc:
            messages.pop()
            input(f"\n{RED}❌ {exc}{RESET}\n\nPress ENTER...")
            continue

        messages.append({
            "role": "assistant",
            "content": answer,
        })

        clear()
        banner()

        print(f"{MAGENTA}{BOLD}🤖 HCO MATRIX RESPONSE{RESET}\n")
        print(f"{WHITE}{answer}{RESET}\n")

        input(f"{CYAN}Press ENTER to return to menu...{RESET}")


def main():
    startup_screen()
    api_key = get_api_key()
    assistant(api_key)


if __name__ == "__main__":
    main()
