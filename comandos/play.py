import discord
from discord.ext import commands
from comandos.voice import playAudioFromFile

class PlayCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url):
        if not ctx.guild.voice_client:
            await ctx.author.voice.channel.connect()

        playAudioFromFile('archivos/sonidos/Nice.mp3', ctx.guild.voice_client)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(PlayCommands(bot))