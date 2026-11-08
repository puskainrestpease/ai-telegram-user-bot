# Telegram AI User Bot

A Telegram user-account automation prototype built with Telethon and Ollama. When enabled for a private conversation, the client sends incoming text messages to a locally available Ollama model and replies with the generated response.

## Requirements

- Python 3.8 or newer
- Telegram API credentials from [my.telegram.org](https://my.telegram.org)
- Ollama installed and running
- A model downloaded in Ollama

## Installation

```bash
git clone https://github.com/puskainrestpease/ai-telegram-user-bot.git
cd ai-telegram-user-bot

python -m venv .venv

# Windows
.venv\\Scripts\\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

## Configuration

Set the Telegram API ID and API hash in `main.py` before starting the client. Do not publish these credentials or the generated Telethon session file.

Pull the model configured in `main.py`:

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
