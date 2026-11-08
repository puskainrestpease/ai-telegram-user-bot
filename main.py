import asyncio
import os

import ollama
from telethon import TelegramClient, events


API_ID = int(os.getenv("TG_API_ID", "0"))
API_HASH = os.getenv("TG_API_HASH", "")
SESSION_NAME = os.getenv("TG_SESSION_NAME", "telegram_ai_session")
MODEL_NAME = os.getenv("OLLAMA_MODEL", "cogito8b:latest")

if API_ID <= 0 or not API_HASH:
    raise SystemExit("Set TG_API_ID and TG_API_HASH environment variables before starting the client.")

PROMPT_AI = ""

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
ai_users = {}


@client.on(events.NewMessage(incoming=True, func=lambda event: event.is_private))
async def handle_message(event):
    sender_id = event.sender_id
    message = event.message.message

    if message == "/channi":
        ai_users[sender_id] = not ai_users.get(sender_id, False)
        state = "enabled" if ai_users[sender_id] else "disabled"
        await event.reply(f"AI replies {state}.")
        return

    if not ai_users.get(sender_id, False) or not message:
        return

    try:
        response = ollama.generate(
            model=MODEL_NAME,
            prompt=f"{PROMPT_AI}\n\nMessage: {message}",
        )
        await event.reply(response["response"])
    except Exception as exc:
        print(f"Failed to generate a response: {type(exc).__name__}: {exc}")
        await event.reply("The AI service is temporarily unavailable.")


async def main():
    await client.start()
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
