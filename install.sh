#!/data/data/com.termux/files/usr/bin/bash

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

CYAN='\033[1;36m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
RED='\033[1;31m'
BOLD='\033[1m'
RESET='\033[0m'


# ============================================================
# HCO MATRIX INSTALLER
# ============================================================

clear

echo -e "${CYAN}${BOLD}"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║                      HCO MATRIX                          ║"
echo "║                 INSTALLATION SYSTEM                      ║"
echo "╚══════════════════════════════════════════════════════════╝"

echo -e "${RESET}"

echo


# ============================================================
# TERMUX DETECTION
# ============================================================

if command -v pkg >/dev/null 2>&1; then

    echo -e "${GREEN}📱 Termux detected${RESET}"

    echo -e "${YELLOW}📦 Installing Python...${RESET}"

    pkg update -y

    pkg install -y python


# ============================================================
# LINUX
# ============================================================

else

    echo -e "${GREEN}🐧 Linux detected${RESET}"

    echo -e "${YELLOW}📦 Installing Python...${RESET}"

    if command -v apt-get >/dev/null 2>&1; then

        if [ "$(id -u)" -eq 0 ]; then

            apt-get update

            apt-get install -y \
                python3 \
                python3-pip

        elif command -v sudo >/dev/null 2>&1; then

            sudo apt-get update

            sudo apt-get install -y \
                python3 \
                python3-pip

        else

            echo -e "${RED}"
            echo "❌ sudo is required to install Python."
            echo -e "${RESET}"

            exit 1

        fi

    else

        echo -e "${RED}"
        echo "❌ apt-get not found."
        echo "Please install Python 3 and pip manually."
        echo -e "${RESET}"

        exit 1

    fi

fi


# ============================================================
# PYTHON DEPENDENCIES
# ============================================================

echo

echo -e "${YELLOW}${BOLD}"
echo "📦 Installing Python dependencies..."
echo -e "${RESET}"

python3 -m pip install \
    -r "$PROJECT_DIR/requirements.txt"


# ============================================================
# FILE PERMISSION
# ============================================================

chmod +x "$PROJECT_DIR/HCO-Matrix.py"


# ============================================================
# INSTALLATION COMPLETE
# ============================================================

echo

echo -e "${GREEN}${BOLD}"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║              ✅ INSTALLATION COMPLETE                    ║"
echo "║                                                          ║"
echo "║              🚀 STARTING HCO MATRIX...                  ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"

echo -e "${RESET}"

sleep 2


# ============================================================
# AUTOMATICALLY START HCO MATRIX
# ============================================================

exec python3 "$PROJECT_DIR/HCO-Matrix.py"
