import discord
from discord.ext import commands

try: # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True
except:
	soupAvailable = False
import aiohttp


class jtrent238:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tacoplease(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("This is a Work In Progress! When finished will get a random image of a taco or something.")


def setup(bot):
	if soupAvailable:
		bot.add_cog(jtrent238(bot))
	else:
		raise RuntimeError("You need to run `pip3 install beautifulsoup4`")
