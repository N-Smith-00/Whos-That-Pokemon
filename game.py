import os
import discord
import asyncio

async def game(channel, user):
    await channel.send('starting game')
    await asyncio.sleep(0.5)
    