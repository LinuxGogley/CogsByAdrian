import discord
from redbot.core import commands
from random import choice as randchoice
import os


class Insult:

    """Airenkun's Insult Cog"""
    def __init__(self, bot):
        fo = open("insults.json","r")
        self.bot = bot
        self.insults = fo.open
        fo.close

    @commands.command(pass_context=True, no_pm=True)
    async def insult(self, ctx, user : discord.Member=None):
        """Insult the user"""

        msg = ' '
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = " How original. No one else had thought of trying to get the bot to insult itself. I applaud your creativity. Yawn. Perhaps this is why you don't have friends. You don't add anything new to any conversation. You are more of a bot than me, predictable answers, and absolutely dull to have an actual conversation with."
                await self.bot.say(user.mention + msg)
            else:
                await self.bot.say(user.mention + msg + randchoice(self.insults))
        else:
            await self.bot.say(ctx.message.author.mention + msg + randchoice(self.insults))

