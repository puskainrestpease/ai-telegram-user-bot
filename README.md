# Telegram AI User Bot

A Telegram user-account automation prototype built with Telethon and Ollama. When enabled in a private conversation, the client sends incoming text messages to a local Ollama model and replies with the generated response.

## Requirements

- Python 3.8 or newer
- Telegram API credentials from https://my.telegram.org
- Ollama installed and running
- The model configured through OLLAMA_MODEL

## Installation

```bash
git clone https://github.com/puskainrestpease/ai-telegram-user-bot.git
cd ai-telegram-user-bot
python -m venv .venv
```

Activate the virtual environment, then install dependencies:

```bash
# Windows
.venv\\Scripts\\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

## Configuration

Set the following environment variables before running the client.

PowerShell:

```powershell
$env:TG_API_ID = "your_api_id"
$env:TG_API_HASH = "your_api_hash"
$env:TG_SESSION_NAME = "telegram_ai_session"
$env:OLLAMA_MODEL = "cogito8b:latest"
```

Linux / macOS:

```bash
export TG_API_ID="your_api_id"
export TG_API_HASH="your_api_hash"
export TG_SESSION_NAME="telegram_ai_session"
export OLLAMA_MODEL="cogito8b:latest"
```

Pull the selected Ollama model:

```bash
ollama pull cogito8b:latest
```

## Run

```bash
python main.py
```

Send `/channi` in a private chat to toggle AI replies for that conversation.

## Security

This project uses a Telegram user session, not a Bot API token. Treat the generated session file as an authentication credential. Keep it out of version control and revoke the session from Telegram settings if it is exposed.

## Limitations

The current implementation keeps the enabled-user state in memory and is intended as a small prototype rather than a production service.
