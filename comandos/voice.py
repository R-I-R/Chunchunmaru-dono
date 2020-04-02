import discord
from discord.ext import commands

async def playAudioFromFile(source, ctx, priority=False):
	if ctx.author.voice == None: return

	if not ctx.guild.voice_client:
		await ctx.author.voice.channel.connect()

	if not ctx.guild.voice_client.is_playing() or priority:
		audio = discord.FFmpegPCMAudio(source)
		ctx.guild.voice_client.play(audio)

class VoiceCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def join(self, ctx):
		await ctx.author.voice.channel.connect()
		await ctx.send('I\'m In')
		
	@commands.command()
	async def sale(self, ctx):
		if ctx.guild.voice_client:
			await ctx.send('Adios')
			await ctx.guild.voice_client.disconnect()
		else:
			await ctx.send('ni si quiera estoy adentro aweonao')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
	bot.add_cog(VoiceCommands(bot))