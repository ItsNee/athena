# import discord

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as', self.user)

#     async def on_message(self, message):
#         # don't respond to ourselves
#         if message.author == self.user:
#             return

#         if message.content == 'pang':
#             await message.channel.send('pung')

# client = MyClient()
# client.run('')

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('NzYzMDMyOTkwMTMyNzMxOTM0.X3xz2Q.6Km1w2m-SWnQMoQr9Lve1Qr88gY')