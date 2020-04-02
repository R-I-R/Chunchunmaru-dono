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
    async def wena(self,ctx):
        await ctx.send('Chupala '+str(ctx.author)+ ' onii-chan',tts=True)
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