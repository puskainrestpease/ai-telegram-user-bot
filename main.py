from telethon import TelegramClient, events
import ollama
import asyncio

# https://core.telegram.org/api
API_ID = 123142124124
API_HASH = 'sigma'
SESSION_NAME = 'zalupa'

PROMPT_AI = """

"""

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
ai_users = {}

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handle_message(event):
    sender_id = event.sender_id
    
    if event.message.message == '/channi':
        ai_users[sender_id] = not ai_users.get(sender_id, False)
        action = "on" if ai_users[sender_id] else "off"
        await event.reply(f"ai mode {action}!")
        return
    
    if ai_users.get(sender_id, False) and event.message.message:
        try:
            response = ollama.generate(
                model='cogito8b:latest',
                prompt=f"{PROMPT_AI}\n\nСообщение: {event.message.message}",
            )
            await asyncio.sleep(1)
            await event.reply(response['response'])
        except:
            await event.reply("something gone wrong")

async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
    