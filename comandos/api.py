import discord
from discord.ext import commands
import requests
import json
class ApiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx,args):
        r = requests.get('https://meme-api.herokuapp.com/gimme/'+args+'/1')
        data = r.json()
        await ctx.send(data['memes'][0]['url'])
    @commands.command()
    async def tiempo(self, ctx,args):
        apiKey = '2f1e8bb2fbf1116d0a9ceebfbb022766';
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+args+'&units=metric&appid='+apiKey
        r = requests.get(url)
        data = r.json()
        msg ='Hay '+str(data['main']['temp'])+'°C en '+str(data['name'])+'!\nLa velocidad del viento es de '+str(data['wind']['speed'])+' kilometros por hora y la humedad es de '+str(data['main']['humidity'])+'%'
        await ctx.send(msg)
# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(ApiCog(bot))