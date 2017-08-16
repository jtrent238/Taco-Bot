import discord
from discord.ext import commands

class jtrent238:
    """I will lick anyone! >.<"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lick(self, user : discord.Member):
        """I will lick anyone! >.<"""

        #Your code will go here
        await self.bot.say("You Lick " + user.mention + "!")

def setup(bot):
    bot.add_cog(jtrent238(bot))
