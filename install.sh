#!/usr/bin/env bash
set -e

echo "🟢 HCO Matrix Installer"
echo "======================="

if command -v pkg >/dev/null 2>&1; then
    echo "📱 Termux detected"
    pkg update -y
    pkg install python -y
else
    echo "🐧 Linux detected"
    if command -v apt >/dev/null 2>&1; then
        sudo apt update
        sudo apt install python3 python3-pip -y
    else
        echo "Please install Python 3 and pip manually."
    fi
fi

PYTHON_BIN="python3"
command -v python3 >/dev/null 2>&1 || PYTHON_BIN="python"

"$PYTHON_BIN" -m pip install -r requirements.txt

echo
echo "✅ HCO Matrix installation complete!"
echo
echo 'Set your API key:'
echo 'export OPENROUTER_API_KEY="YOUR_API_KEY"'
echo
echo 'Then run:'
echo "$PYTHON_BIN ai.py"
