import os
import discord
import asyncio
from flask import Flask
from dotenv import load_dotenv
import commands

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
        await channel.send('starting game')
        await asyncio.sleep(0.5)
        score = commands.game(client, channel, user)
        await channel.send(f'Game over, your final score is {score}')
        #check leaderboard

@app.route("/")
def main():
    client.run(os.getenv('TOKEN'))
    return "Who's That Pokemon (WIP)"