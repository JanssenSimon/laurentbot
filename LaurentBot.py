#!/usr/bin/env python3

import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
import random

bot=commands.Bot(command_prefix="#")

@bot.event
async def on_ready():
    print("I'm ready to go!")

#list of channel codes for the channels the bot should listen in
botChannels = [469621935609872395, 699351427364945930, 699352021144174602]

#if a message is sent, check that it respects requirements and reply maybe
@bot.event
async def on_message(message):
    if message.channel.id in botChannels:
        if message.author != bot.user:
            if " " not in message.content and "http" not in message.content:
                if random.randint(0,10) == 10:
                    await message.channel.send(message.content + "aroo")

#run the bot using the bot key
bot.run("***********************************************")
