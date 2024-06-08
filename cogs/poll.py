import discord
import requests
import json

from cogs.base_cog import BaseCog
from discord.ext import commands

class Poll(BaseCog):
  def __init__(self, bot):
    super().__init__(bot)

  @commands.command(name='test')
  async def meal_with_no_video(self, ctx):
    await ctx.send(f'{ctx.message.author.name} sent a message.')

  def text_search(self, query):
    url = 'https://places.googleapis.com/v1/places:searchText'

    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': self.bot.places_key,
        'X-Goog-FieldMask': 'places.displayName,places.googleMapsUri'
    }

    data = {
        'textQuery': query,
        'pageSize' : 5,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}")
    return json.loads(response.text)
  @commands.command(name='poll')
  async def poll(self, ctx, *args):
    query = ' '.join(args)
    results = self.text_search(query)['places']
async def setup(bot):
  await bot.add_cog(Poll(bot))