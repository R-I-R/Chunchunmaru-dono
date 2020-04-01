import discord
from discord.ext import commands

TOKEN = 'Njk0NjkxOTg2ODU0MTE3NDk2.XoPU5Q._QwabIi0FAtfb_ntoVylyHKdPNw'
client = commands.Bot(command_prefix='uwu ')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(pass_context=True)
async def hola(ctx,args):
    print(ctx.message.content)
    print(args)
    await ctx.message.channel.send('hola')

client.run(TOKEN)