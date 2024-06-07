from discord.ext import commands
from base.formatted_logger import get_formatted_logger

class BaseCog(commands.Cog):
  logging = get_formatted_logger()

  def __init__(self, bot):
    self.bot = bot
    #self.cursor = bot.db.cursor
    