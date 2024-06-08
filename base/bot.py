import asyncio
import discord
import os

from database import Database
from discord.ext import commands
from base.formatted_logger import get_formatted_logger

class PPBot(commands.Bot):
  logging = get_formatted_logger()

  def __init__(self, command_prefix='!', intents=discord.Intents.default(), places_key='', discord_token=''):
    super().__init__(command_prefix=command_prefix, intents=intents)
    self.places_key = places_key
    self.discord_token = discord_token
    #self.db = Database()

  async def load(self):
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py') and filename != 'base_cog.py':
        await self.load_extension(f'cogs.{filename[:-3]}')

  def initialize(self):
    asyncio.run(self.load())

  
