import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "!ping":
        await message.channel.send("Pong 🏓")

# Start web server
keep_alive()

TOKEN = os.environ.get("TOKEN")
client.run(TOKEN)
