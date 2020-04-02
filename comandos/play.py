import discord
from discord.ext import commands
from comandos.voice import playAudioFromFile
palanum = {
	'si':'01',
	'no':'02',
	'damealimento':'03',
	'damemadera':'04',
	'dameoro':'05',
	'damepiedra':'06',
	'ahh':'07',
	'todossaluden':'08',
	'oooh':'09',
	'devuelta':'10',
	'hahaha':'11',
	'soyasaltado':'12',
	'laculpa':'13',
	'comienzajugar':'14',
	'nomeapuntes':'15',
	'enemigovista':'16',
	'estupendorey':'17',
	'unmonje':'18',
	'llevamosmuchotiempo':'19',
	'miabuelita':'20',
	'bonitaciudad':'21',
	'nometoques':'22',
	'grupodecaza':'23',
	'malditasea':'24',
	'hieremesipuedes':'25',
	'nolamaravilla':'26',
	'hasjugado2horas':'27',
	'deberiasvercomoquedo':'28',
	'roggan':'29',
	'wololo':'30',
	'atacaalenemigo':'31',
	'dejadecrearaldeanos':'32',
	'creamasaldeanos':'33',
	'construyeunaarmada':'34',
	'dejadecontruirarmada':'35',
	'esperamiseñal':'36',
	'contruyeunamaravilla':'37',
	'dameloquetesobre':'38',
	'ally':'39',
	'enemy':'40',
	'neutral':'41',
	'enqueedad':'42'
}
class PlayCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def age(self, ctx, args):
        if(len(args)==2):
            await playAudioFromFile('archivos/age2sonidos/'+ args +'.mp3')
        elif(len(args)==1):
            await playAudioFromFile('archivos/age2sonidos/0'+ args +'.mp3')
        else:
            await playAudioFromFile('archivos/age2sonidos/'+ palanum[args] +'.mp3')
    @commands.command()
    async def hola(self,ctx,args):
        if (args=='1'):
            await ctx.send('Okaeri '+str(ctx.author.nick)+ ' onii-chan',tts=True)
        else:
            await ctx.send('Okaeri '+str(ctx.author.nick)+ ' onii-chan')
            await playAudioFromFile('archivos/sonidos/okaeri onii-chan.mp3')
    @commands.command()
    async def nice(self,ctx): 
        with open('archivos/img/nice.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/nice.gif')
            await ctx.send(file=img)
            await playAudioFromFile('archivos/sonidos/Nice.mp3')
    @commands.command()
    async def ara(self,ctx): 
        with open('archivos/img/ara.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/araara.gif')
            await ctx.send(file=img)
            await playAudioFromFile('archivos/sonidos/araara.mp3')
    @commands.command()
    async def pilarmen(self,ctx): 
        with open('archivos/img/pilarmen.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/pilarmen.gif')
            await ctx.send(file=img)
            await playAudioFromFile('archivos/sonidos/Pillar MenS.mp3')
    @commands.command()
    async def pilarmenfull(self,ctx): 
        with open('archivos/img/pilarmen.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/pilarmen.gif')
            await ctx.send(file=img)
            await playAudioFromFile('archivos/sonidos/Pillar Men.mp3')
    @commands.command()
    async def callate(self,ctx): 
        with open('archivos/img/silencio.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/silencio.gif')
            await ctx.send(file=img)
            await playAudioFromFile('archivos/sonidos/silencio.mp3')
    @commands.command()
    async def nya(self,ctx): 
        with open('archivos/img/nyan.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/nyan.gif')
            await ctx.send(file=img)
            await playAudioFromFile('archivos/sonidos/nya.mp3')
    @commands.command()
    async def tuturu(self,ctx): 
        with open('archivos/img/tuturu.png','rb') as fp:
            img = discord.File(fp,'archivos/img/tuturu.png')
            await ctx.send(file=img)
            await playAudioFromFile('archivos/sonidos/Tuturu.mp3')
    @commands.command()
    async def baka(self,ctx): 
        with open('archivos/img/baka.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/baka.gif')
            await ctx.send(file=img)
            await playAudioFromFile('archivos/sonidos/Baka.mp3')
    @commands.command()
    async def ohoho(self,ctx): 
        with open('archivos/img/ohoho.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/ohoho.gif')
            await ctx.send(file=img)
            await playAudioFromFile('archivos/sonidos/ohoho.mp3')
    @commands.command()
    async def risamalvada(self,ctx): 
        with open('archivos/img/risamalvada.gif','rb') as fp:
            img = discord.File(fp,'archivos/img/risamalvada.gif')
            await ctx.send(file=img)
            await playAudioFromFile('archivos/sonidos/risamalvada.mp3')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(PlayCommands(bot))