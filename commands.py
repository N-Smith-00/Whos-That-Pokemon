import os
import discord
import asyncio
import random
import string
from pokemon import pokemon_dict as pokemon

async def game(client, channel, user):

    # Untested

    # send pic of pokemon
    name = list(pokemon)[random.randrange(0, len(pokemon))]
    with open('f{pokemon[name]}.png', 'rb') as fp:
        await channel.send(discord.File(fp, 'pokemon.png'))
    # wait for response
    try:
        msg = await client.wait_for('message', check=check, timeout=5.0)
    except(TimeoutError):
        await channel.send('you have run out of time')
        return 1
    # check answer
    if (msg.content != name):
        await channel.send(f'wrong answer, the correct answer is {name}')
        return 1
    else:
        await channel.send('correct')
        return (1 + game(client, channel, user))

def check(m, user, channel):
    return m.author == user and m.channel == channel