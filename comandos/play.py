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
    @commands.command()
    async def hola(self,ctx,args):
        if (args=='1'):
            await ctx.send('Okaeri '+str(ctx.author.nick)+ ' onii-chan',tts=True)
        else:
            await ctx.send('Okaeri '+str(ctx.author.nick)+ ' onii-chan')
            if not ctx.guild.voice_client:
                await ctx.author.voice.channel.connect()
            playAudioFromFile('archivos/sonidos/okaeri onii-chan.mp3', ctx.guild.voice_client)
    @commands.command()
    async def nice(self,ctx): 
        with open('archivos/img/nice.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/nice.gif')
            await ctx.send(file=img)
            if not ctx.guild.voice_client:
                await ctx.author.voice.channel.connect()
            playAudioFromFile('archivos/sonidos/Nice.mp3', ctx.guild.voice_client)
    @commands.command()
    async def ara(self,ctx): 
        with open('archivos/img/ara.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/araara.gif')
            await ctx.send(file=img)
            if not ctx.guild.voice_client:
                await ctx.author.voice.channel.connect()
            playAudioFromFile('archivos/sonidos/araara.mp3', ctx.guild.voice_client)
    @commands.command()
    async def pilarmen(self,ctx): 
        with open('archivos/img/pilarmen.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/pilarmen.gif')
            await ctx.send(file=img)
            if not ctx.guild.voice_client:
                await ctx.author.voice.channel.connect()
            playAudioFromFile('archivos/sonidos/Pillar MenS.mp3', ctx.guild.voice_client)
    @commands.command()
    async def pilarmenfull(self,ctx): 
        with open('archivos/img/pilarmen.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/pilarmen.gif')
            await ctx.send(file=img)
            if not ctx.guild.voice_client:
                await ctx.author.voice.channel.connect()
            playAudioFromFile('archivos/sonidos/Pillar Men.mp3', ctx.guild.voice_client)
    @commands.command()
    async def callate(self,ctx): 
        with open('archivos/img/silencio.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/silencio.gif')
            await ctx.send(file=img)
            if not ctx.guild.voice_client:
                await ctx.author.voice.channel.connect()
            playAudioFromFile('archivos/sonidos/silencio.mp3', ctx.guild.voice_client)
    @commands.command()
    async def nya(self,ctx): 
        with open('archivos/img/nyan.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/nyan.gif')
            await ctx.send(file=img)
            if not ctx.guild.voice_client:
                await ctx.author.voice.channel.connect()
            playAudioFromFile('archivos/sonidos/nya.mp3', ctx.guild.voice_client)
    @commands.command()
    async def tuturu(self,ctx): 
        with open('archivos/img/tuturu.png','rb') as fp:
            img = discord.File(fp,'archivos/img/tuturu.png')
            await ctx.send(file=img)
            if not ctx.guild.voice_client:
                await ctx.author.voice.channel.connect()
            playAudioFromFile('archivos/sonidos/Tuturu.mp3', ctx.guild.voice_client)
    @commands.command()
    async def baka(self,ctx): 
        with open('archivos/img/baka.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/baka.gif')
            await ctx.send(file=img)
            if not ctx.guild.voice_client:
                await ctx.author.voice.channel.connect()
            playAudioFromFile('archivos/sonidos/Baka.mp3', ctx.guild.voice_client)
    @commands.command()
    async def ohoho(self,ctx): 
        with open('archivos/img/ohoho.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/ohoho.gif')
            await ctx.send(file=img)
            if not ctx.guild.voice_client:
                await ctx.author.voice.channel.connect()
            playAudioFromFile('archivos/sonidos/ohoho.mp3', ctx.guild.voice_client)
    @commands.command()
    async def risamalvada(self,ctx): 
        with open('archivos/img/risamalvada.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/risamalvada.gif')
            await ctx.send(file=img)
            if not ctx.guild.voice_client:
                await ctx.author.voice.channel.connect()
            playAudioFromFile('archivos/sonidos/risamalvada.mp3', ctx.guild.voice_client)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(PlayCommands(bot))