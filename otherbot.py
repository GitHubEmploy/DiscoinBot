import discord
from discord.ext import commands
import time
import random
#---CONFIG---

token = "NDU2NTA2OTE5MjEzODU4ODIw.X6mQgg.jvnsxMMqOkiZtWLTr9e1oCpQ2go" # https://www.youtube.com/watch?v=tI1lzqzLQCs
prefix = "!" # This defines the selfbot prefix. You can customize it however you like, but you should probably keep it tiny.

#--- BOT ---

print("Logging into Discord...")

client = discord.Client()
count = 0
@client.event
async def on_message(message):
    global count
    if message.content.startswith('-start'):
        while True:
            count = count + 1
            await message.channel.send('pls beg')
            time.sleep(int(random.randrange(0, 5, 1)))
            await message.channel.send('pls hunt')
            time.sleep(int(random.randrange(0, 30, 1)))
            if count >= int(random.randrange(0, 70, 1)):
                await message.channel.send('pls hourly')
                count = 0
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(client.guilds)
    print('------')

client.run(token, bot=False)
