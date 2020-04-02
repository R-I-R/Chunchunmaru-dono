import discord
from discord.ext import commands
from .shintarocommands import *
import random
TOKEN = 'Njk0NjkxOTg2ODU0MTE3NDk2.XoPU5Q._QwabIi0FAtfb_ntoVylyHKdPNw'
client = commands.Bot(command_prefix='uwu ')

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

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(pass_context=True)
async def hola(ctx,args):
    print(ctx.message.content)
    print(args)
    await ctx.message.channel.send('hola')
@client.command(pass_context=True)
async def text(ctx,args):
    if(args=="changemymind"):
        pass
    elif(args=="help"):
        helptext =":european_castle: **Sonidos del Age of Empires 2**. \n`age <Numero del sonido / Frase clave>`\n:speaking_head: **Frases**\n`loli`,`botqlo`,`wena`,`hola`,`nice`,`ara`,`yamero`,`nya`,`tuturu`,`baka`,`ohoho`,`risamalvada`\n:confetti_ball: **Diversión**\n`meme <pagina(Por ahora solo jaidefinichon)>`\n:notes: **Musica**\n`callate`,`avengers`,`pilarmen`,`pilarmenfull`\n:cool: **Misc**\n`dado`,`moneda`,`tiempo<ciudad>`,`sale`"
        await ctx.message.channel.send(helptext)
    elif(args=="loli"):
        await ctx.message.channel.send('Yoshi yoshi onichan.')
    elif(args=="botqlo"):
        await ctx.message.channel.send('K wea otaku qlo bastardo ijo la comemoco')
    elif(args=="moneda"):
        moneda = "cara" if(random.randint(0,1)==1) else "sello"
        await ctx.message.channel.send("Salio"+moneda)
    elif(args=="dado"):
        numero = str(random.randint(1,6))
        await ctx.message.channel.send("Salio"+numero)
    elif(args=="tiempo"):
        pass
    else:
        await ctx.message.channel.send('El comando no esta programado, te-he uwu')
@client.command(pass_context=True)
async def age(ctx,args):
    canal = ctx.message.channel
    voice_client= client.voice_client_in(canal)
    if(len(args[0])==2):
        voice_client.play("/archivos/age2sonidos/"+args[0]+".mp3")
    else:
        voice_client.play("/archivos/age2sonidos/"+palanum[args[0]]+".mp3")
    await voice_client.disconnect()
client.run(TOKEN)