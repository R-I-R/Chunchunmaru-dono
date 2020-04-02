import discord
from discord.ext import commands
import requests
import json
class MemeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx,args):
        if (args=="dankmemes":)
            r = requests.get('https://meme-api.herokuapp.com/gimme/dankmemes/1')
            data = r.json()
            await ctx.send(data['memes'][0]['url'])

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(MemeCog(bot))