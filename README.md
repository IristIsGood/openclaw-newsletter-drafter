# Newsletter Drafter: Agentic OpenClaw Skill 🤖
An autonomous capability for the OpenClaw gateway that leverages GPT-5.4 to research, draft, and persist professional newsletters to the local file system.

## 🎯 Problem & Solution
* **Problem:** Traditional LLM workflows require manual "copy-pasting" between a browser and a text editor, creating a bottleneck in content production.
* **Solution:** A **Zero-UI Agentic Workflow**. By integrating directly with the OpenClaw gateway, the AI gains "agency"—the ability to execute code and manage files locally on your Mac without human intervention.

## 🏗️ Technical Architecture & OpenClaw Integration
Building an OpenClaw skill is a technical exercise in **Agentic Orchestration**. Unlike a standard chatbot, this project operates across three layers:

1. **The Gateway Layer:** OpenClaw runs a local Node.js server that acts as a secure proxy between your MacBook and OpenAI.
2. **The Skill Protocol:** The \`SKILL.md\` file serves as a **Functional Manifest**. It tells the OpenClaw interpreter how to map natural language triggers (intent) to specific Python binaries (action).
3. **The Execution Layer:** A Python-based runtime environment that handles:
    * **State Persistence:** Moving AI-generated data from volatile memory (LLM response) to non-volatile storage (your SSD).
    * **Absolute Path Resolution:** Using robust logic (\`os.path.abspath\`) to prevent path recursion bugs common in agentic sub-shells.

## ✨ Key Features
* **Autonomous Execution:** Triggered via natural language through the OpenClaw Dashboard.
* **GPT-5.4 Integration:** Optimized for high-reasoning models to ensure editorial quality.
* **Smart File I/O:** Automatically handles directory creation and date-stamped naming conventions.
* **Markdown Native:** Outputs formatted \`.md\` files ready for static site generators or email editors.

## 🛠️ Tech Stack
* **Framework:** OpenClaw (Local-First AI Agent Gateway)
* **Intelligence:** OpenAI API (GPT-5.4)
* **Runtime:** Python 3.11+ (Optimized for Apple Silicon/Zsh)
* **Environment:** macOS POSIX File System

## 🚀 Getting Started

### 1. Install OpenClaw
Ensure Node.js (v22+) is installed, then run:
\`\`\`bash
npm install -g openclaw@latest
openclaw onboard --openai-api-key "your-key"
\`\`\`

### 2. Install This Skill
Clone this repo into your OpenClaw workspace:
\`\`\`bash
mkdir -p ~/.openclaw/workspace/skills/newsletter-drafter
# (Move draft_newsletter.py and SKILL.md here)
\`\`\`

Test the script directly first — before wiring it to OpenClaw
python3 draft_newsletter.py "AI agents in 2026"copy
You should see a success message and a new .md file in your newsletters folder. Open it to check the output.

### 3. Run the Gateway
\`\`\`bash
openclaw gateway start
openclaw dashboard
\`\`\`
*Simply type "Draft a newsletter about SpaceX" in the dashboard chat.*

## 🔑 Key Technical Decisions
* **Challenge: The "Path Loop" Bug:** During development, sub-agents created redundant nested directories (e.g., \`/Users/irist/Users/irist/\`).
* **Technical Fix:** Implemented a robust path-resolution strategy using \`__file__\` introspection. This ensures the script is **environment-aware**, a critical requirement for tools executed by autonomous agents.

## 🛡️ Safety & Sandboxing
To ensure security on macOS, this skill is designed for **Local-First execution**. It does not require elevated (sudo) permissions and operates within the user-level \`~/.openclaw\` directory, adhering to the principle of least privilege.

## 🛡️ Screenshot 
<img width="1436" height="809" alt="Screenshot 2026-04-16 at 2 02 16 PM" src="https://github.com/user-attachments/assets/966c474c-1634-43fd-9d77-4e206031f7a4" />
<img width="1722" height="432" alt="image" src="https://github.com/user-attachments/assets/d2cc87d0-1b46-4735-b6e1-fc673c7f1c55" />


## 📝 License
MIT

## 👤 Developer
**Irist** – Exploring the frontier of Local AI Agents.
