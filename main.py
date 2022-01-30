import os
import discord
TOKEN = os.environ.get('DS-BOT-TKN')
PREFIX = "'"
INTENTS = discord.Intents.default()
client = discord.Client(commands_prefix=PREFIX, intents=INTENTS)


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')


client.run(TOKEN)