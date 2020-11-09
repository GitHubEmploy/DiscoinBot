import discord
from discord.ext import commands
import time
import random
#---CONFIG---

token = "NTM1OTcyNzA0NDAzMTkzODg4.X6jIMw.XDvpXQ9XY7va7Lq-QjhBe3P_nxk" # https://www.youtube.com/watch?v=tI1lzqzLQCs
prefix = "!" # This defines the selfbot prefix. You can customize it however you like, but you should probably keep it tiny.

#--- BOT ---



print("Logging into Discord...")

client = discord.Client()

@client.event
async def on_message(message):

    if message.content.startswith('-start'):
        while True:
            count = count + 1
            await message.channel.send('pls beg')
            time.sleep(int(random.randrange(0, 150, 1)))
            if count == int(random.randrange(0, 97, 1)):
                await message.channel.send('pls hourly')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token, bot=False)
