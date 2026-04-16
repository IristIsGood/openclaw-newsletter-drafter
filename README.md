# openclaw-newsletter-drafter🤖

An autonomous OpenClaw skill that leverages GPT-5.4 to research, draft, and format professional newsletters directly into your local workspace.

## 🎯 Problem & Solution
* **Problem:** Content creation is time-consuming, and manually switching between an LLM and a text editor to save and format files disrupts the creative flow.
* **Solution:** A zero-click agentic workflow. You tell OpenClaw what to write about, and the script handles the API call, professional formatting, and local file management instantly.

## ✨ Key Features
* **GPT-5.4 Powered:** Uses the latest OpenAI models for high-quality, professional prose.
* **Smart Formatting:** Automatically generates catchy headlines and structured Markdown.
* **Local File Vault:** Organizes drafts by date and topic in a dedicated \`newsletters/\` directory.
* **OpenClaw Integrated:** Designed to be triggered by natural language commands through the OpenClaw gateway.

## 🏗️ Architecture
* **Runtime:** Python 3.11+
* **AI Orchestration:** OpenAI SDK (Chat Completions API).
* **Integration:** OpenClaw Skill Protocol (via \`SKILL.md\` triggers).
* **File System:** Local POSIX-compliant file I/O for macOS.

## 🛠️ Tech Stack
* **Language:** Python | **AI:** OpenAI GPT-5.4 | **OS:** macOS (optimized) | **Agent Framework:** OpenClaw

## 🚀 Getting Started
### Prerequisites
* macOS (MacBook Air/Pro)
* Python 3.10+ & \`pip\`
* An OpenAI API Key

### Installation
1. **Clone & Navigate:**
   \`\`\`bash
   mkdir -p ~/newsletter-drafter && cd ~/newsletter-drafter
   \`\`\`
2. **Set up Environment:**
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate
   pip install openai
   export OPENAI_API_KEY='your-key-here'
   \`\`\`
3. **Configure OpenClaw:**
   Place the \`SKILL.md\` in \`~/.openclaw/workspace/skills/newsletter-drafter/\` to allow natural language triggers.

## 🔑 Key Technical Decisions & Learning
* **Challenge: Path Recursion on macOS.**
    * *Problem:* Initial scripts created redundant \`/Users/irist/Users/irist/\` directories.
    * *Solution:* Implemented \`os.path.abspath(__file__)\` to ensure the script always identifies its location relative to its own directory.

## 🗺️ Roadmap
* [ ] Add support for DALL-E 3 image generation.
* [ ] Integration with Mailchimp/SendGrid API.
* [ ] Multi-model support (toggle between GPT-4o and GPT-5.4).

## 📝 License
MIT License

## 👤 About the Developer
**Irist**
