import discord

from cogs.base_cog import BaseCog
from discord.ext import commands

class Poll(BaseCog):
  def __init__(self, bot):
    super().__init__(bot)

  @commands.command(name='test')
  async def meal_with_no_video(self, ctx):
    await ctx.send(f'{ctx.message.author.name} sent a message.')

async def setup(bot):
  await bot.add_cog(Poll(bot))