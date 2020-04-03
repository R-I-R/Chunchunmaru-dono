import discord
from discord.ext import commands
import sys, traceback
from credentials import Credential

TOKEN = Credential.discord
bot = commands.Bot(command_prefix='uwu ')
bot.remove_command('help')
initial_extensions = ['comandos.play',
					'comandos.text',
					'comandos.api',
					'comandos.voice']


if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))


bot.run(TOKEN)