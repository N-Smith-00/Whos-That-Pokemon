import os
import discord
from flask import Flask
import commands
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    channel = message.channel
    user = message.author

    if message.content.startswith('!pstart'):
        commands.game(channel, user)

@app.route("/")
def main():
    client.run(os.getenv('TOKEN'))
    return "Who' That Pokemon (WIP)"