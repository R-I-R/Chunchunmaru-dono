import discord
from discord.ext import commands
import random

class TextCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def help(self,ctx):
        helptext =":european_castle: **Sonidos del Age of Empires 2**. \n`age <Numero del sonido / Frase clave>`\n:speaking_head: **Frases**\n`loli`,`botqlo`,`wena`,`hola`,`nice`,`ara`,`yamero`,`nya`,`tuturu`,`baka`,`ohoho`,`risamalvada`\n:confetti_ball: **Diversión**\n`meme <pagina(Por ahora solo jaidefinichon)>`\n:notes: **Musica**\n`callate`,`avengers`,`pilarmen`,`pilarmenfull`\n:cool: **Misc**\n`dado`,`moneda`,`tiempo<ciudad>`,`sale`"
        await ctx.send(helptext)
    @commands.command()
    async def loli(self,ctx):
        await ctx.send('Yoshi yoshi onichan.')
    @commands.command()
    async def moneda(self,ctx):
        moneda = "cara" if(random.randint(0,1)==1) else "sello"
        await ctx.send("Salio "+moneda)
    @commands.command()
    async def botqlo(self,ctx):
        await ctx.send('K wea otaku qlo bastardo ijo la comemoco')
    @commands.command()
    async def hola(self,ctx,args):
        if (args=='1'):
            await ctx.send('Okaeri '+str(ctx.author.nick)+ ' onii-chan',tts=True)
        else:
            await ctx.send('Okaeri '+str(ctx.author.nick)+ ' onii-chan')
    @commands.command()
    async def wena(self,ctx):
        await ctx.send('Chupala '+str(ctx.author)+ ' onii-chan',tts=True)
    @commands.command()
    async def nice(self,ctx): 
        with open('archivos/img/nice.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/nice.gif')
            await ctx.send(file=img)
    @commands.command()
    async def ara(self,ctx): 
        with open('archivos/img/ara.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/ara.gif')
            await ctx.send(file=img)
    @commands.command()
    async def pilarmen(self,ctx): 
        with open('archivos/img/pilarmen.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/pilarmen.gif')
            await ctx.send(file=img)
    @commands.command()
    async def pilarmenfull(self,ctx): 
        with open('archivos/img/pilarmen.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/pilarmen.gif')
            await ctx.send(file=img)
    @commands.command()
    async def callate(self,ctx): 
        with open('archivos/img/silencio.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/silencio.gif')
            await ctx.send(file=img)
    @commands.command()
    async def nya(self,ctx): 
        with open('archivos/img/nyan.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/nyan.gif')
            await ctx.send(file=img)
    @commands.command()
    async def tuturu(self,ctx): 
        with open('archivos/img/tuturu.png','rb') as fp:
            img = discord.File(fp,'archivos/img/tuturu.png')
            await ctx.send(file=img)
    @commands.command()
    async def baka(self,ctx): 
        with open('archivos/img/baka.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/baka.gif')
            await ctx.send(file=img)
    @commands.command()
    async def ohoho(self,ctx): 
        with open('archivos/img/ohoho.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/ohoho.gif')
            await ctx.send(file=img)
    @commands.command()
    async def risamalvada(self,ctx): 
        with open('archivos/img/risamalvada.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/risamalvada.gif')
            await ctx.send(file=img)
    @commands.command()
    async def dado(self,ctx):
        numero = str(random.randint(1,6))
        await ctx.send("Salio "+numero)
    @commands.command()
    async def changemymind(self,ctx):
        pass
    @commands.command()
    async def tiempo(self,ctx):
        pass
    

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(TextCog(bot))