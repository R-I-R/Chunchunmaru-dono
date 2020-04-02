import discord
from discord.ext import commands
import sys, traceback

TOKEN = 'Njk0NjkxOTg2ODU0MTE3NDk2.XoPU5Q._QwabIi0FAtfb_ntoVylyHKdPNw'
bot = commands.Bot(command_prefix='uwu ')
bot.remove_command('help')
initial_extensions = ['comandos.play','comandos.text','comandos.age','comandos.memes']

if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))


bot.run(TOKEN)