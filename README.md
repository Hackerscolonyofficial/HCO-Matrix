# 🟢 HCO Matrix

### AI Command-Line Assistant for Termux & Linux

> **"The quieter you become, the more you are able to hear."**

**Tool Name:** HCO Matrix  
**Code by:** Azhar • HCO Team  
**Channel:** Hackers Colony Tech

HCO Matrix is a colorful command-line AI assistant designed to run in
**Termux on Android** and on **Linux**.

It connects your terminal to an AI model through the OpenRouter API, allowing
you to ask questions, understand Linux/Termux commands, get coding help, and
learn cybersecurity concepts directly from the command line.

---

## ⚠️ Disclaimer

HCO Matrix is an educational technology project.

Use this tool and any AI-generated commands responsibly and only on systems,
networks, accounts, and devices that you own or have explicit permission to
test.

AI-generated information can be incorrect. Always review commands before
running them.

For cybersecurity use, keep your activity legal, authorized, defensive, and
educational.

---

## 🔐 API KEY SECURITY

**NEVER put your real API key inside `ai.py` or commit it to GitHub.**

HCO Matrix reads the API key from an environment variable:

```bash
OPENROUTER_API_KEY
```

Your API key stays on your machine and is not included in this repository.

If an API key is accidentally exposed, revoke it immediately and generate a
new one.

---

# 📱 Termux Installation

### 1️⃣ Update Termux

```bash
pkg update -y && pkg upgrade -y
```

### 2️⃣ Install Git and Python

```bash
pkg install git python -y
```

### 3️⃣ Clone HCO Matrix

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 4️⃣ Enter the directory

```bash
cd HCO-Matrix
```

### 5️⃣ Install the Python dependency

```bash
pip install -r requirements.txt
```

### 6️⃣ Add your API key 🔑

Create your own OpenRouter API key, then run:

```bash
export OPENROUTER_API_KEY="YOUR_API_KEY"
```

**Do not share your key with anyone.**

### 7️⃣ Run HCO Matrix 🚀

```bash
python ai.py
```

---

# 🐧 Linux Installation

### 1️⃣ Update packages

Ubuntu/Debian/Kali:

```bash
sudo apt update
```

### 2️⃣ Install Git and Python

Ubuntu/Debian/Kali:

```bash
sudo apt install git python3 python3-pip -y
```

### 3️⃣ Clone HCO Matrix

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 4️⃣ Enter the directory

```bash
cd HCO-Matrix
```

### 5️⃣ Install dependencies

```bash
python3 -m pip install -r requirements.txt --user
```

If your Linux distribution requires a virtual environment, use:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 6️⃣ Add your API key 🔑

```bash
export OPENROUTER_API_KEY="YOUR_API_KEY"
```

### 7️⃣ Start the tool 🚀

```bash
python3 ai.py
```

---

# 🎨 HCO Matrix Features

```text
[1] 🤖 Ask AI
[2] 🐧 Explain Linux / Termux Command
[3] 💻 Code Assistant
[4] 🛡️  Cybersecurity Learning
[5] 💬 General Question
[6] 🧹 Clear Conversation
[0] 🚪 Exit
```

### 🤖 Ask AI
Ask normal questions directly from the terminal.

### 🐧 Linux / Termux
Understand commands and their purpose.

### 💻 Code Assistant
Get coding explanations, examples, and debugging help.

### 🛡️ Cybersecurity Learning
Learn cybersecurity concepts for authorized and educational use.

### 💬 General Questions
Use HCO Matrix as a general command-line AI assistant.

---

# 📺 Hackers Colony Tech

On startup, HCO Matrix provides a voluntary support prompt and opens the
Hackers Colony Tech YouTube channel.

Users can like, subscribe, and enable notifications if they enjoy the content.
HCO Matrix does **not** technically verify these actions.

---

# 🧑‍💻 Credits

**Code by Azhar • HCO Team**

**Hackers Colony Tech**

---

# 📜 License

HCO Matrix is distributed under the **HCO Matrix Proprietary License**.

See [`LICENSE`](LICENSE) for the complete terms.

Public visibility of source code on GitHub cannot technically prevent copying.
The license states the permitted and prohibited uses. If the source must remain
private, use a private repository.

---

## ⭐ Support

If you find HCO Matrix useful, support **Hackers Colony Tech** on YouTube.

Keep learning. Keep building. Stay ethical. 🛡️
