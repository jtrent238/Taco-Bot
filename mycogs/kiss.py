import discord
from discord.ext import commands

class jtrent238:
    """Kiss Someone!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kiss(self, user : discord.Member):
        """Kiss Someone"""

        #Your code will go here
        await self.bot.say("You Kiss " + user.mention + " <3")

def setup(bot):
    bot.add_cog(jtrent238(bot))
