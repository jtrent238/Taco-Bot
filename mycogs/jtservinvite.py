import discord
from discord.ext import commands

try: # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True
except:
	soupAvailable = False
import aiohttp


class jtrent238:
    """Get an invite link to jtrent238's Discord Server"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def inviteme(self):
        """Get an invite to jtrent238's server!"""

        #Your code will go here
        await self.bot.say("Here is a link to jtrent238's Discord Server: https://discord.gg/g4S5cMg")


def setup(bot):
	if soupAvailable:
		bot.add_cog(jtrent238(bot))
	else:
		raise RuntimeError("You need to run `pip3 install beautifulsoup4`")
