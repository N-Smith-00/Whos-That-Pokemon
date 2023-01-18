import os
import discord
import asyncio
import random
import string
from pokemon import pokemon_dict as pokemon

async def game(client, channel, user, timeout=10):

    # send pic of pokemon
    name = list(pokemon)[random.randrange(0, len(pokemon))]
    with open(f'pictures/{pokemon[name]}.png', 'rb') as fp:
        await channel.send(file=discord.File(fp, 'pokemon.png'))
    # wait for response
    try:
        def check(m):
            return m.author == user and m.channel == channel
        msg = await client.wait_for('message', check=check, timeout=timeout)
    except(asyncio.exceptions.TimeoutError):
        await channel.send('you have run out of time')
        return 0
    # check answer
    if (msg.content != name):
        await channel.send(f'wrong answer, the correct answer is {name}')
        return 0
    else:
        await channel.send('correct')
        await asyncio.sleep(0.5)
        return (1 + await game(client, channel, user, timeout*0.994))