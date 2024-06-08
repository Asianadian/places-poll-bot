import discord
import json
import requests

from cogs.base_cog import BaseCog
from discord.ext import commands

def format_poll_option(text):
  return (text if len(text) <= 55 else text[:52] + '...')

def format_embed_name(i, place):
  return f"{i+1}. {place['displayName']['text']} ({float(place['rating']):.1f})"

def format_embed_value(place):
  return f"{place['editorialSummary']['text']}\n[More...]({place['googleMapsUri']})"

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
        'X-Goog-FieldMask': 'places.displayName,places.googleMapsUri,places.rating,places.editorialSummary'
    }

    data = {
        'textQuery': query,
        'pageSize' : 5,
    }

    response = requests.post(url, headers=headers, json=data)

    return json.loads(response.text)
  
  async def show_links(self, ctx, places):
    embedVar = discord.Embed(title='Top Results:', color=0x00ff00)
    
    for i, place in enumerate(places):
      embedVar.add_field(name=format_embed_name(i, place), value=format_embed_value(place), inline=False)

    await ctx.send(embed=embedVar)
  
  async def create_poll(self, ctx, places):
    channel_id = ctx.channel.id
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

    headers = {
      'Content-Type': 'application/json',
      'Authorization': f'Bot {self.bot.discord_token}'
    }

    data = {
      'poll': {
         'question': {'text': 'Vote:'}
         ,
         'answers': [
            {
               'answer_id': index+1,
               'poll_media': {'text': format_poll_option(place['displayName']['text'])}
            }
            for index, place in enumerate(places)
          ]
      }
    }

    response = requests.post(url, headers=headers, json=data)
    
    return json.loads(response.text)

  @commands.command(name='poll')
  async def poll(self, ctx, *args):
    query = ' '.join(args)
    results = self.text_search(query)['places']

    await self.show_links(ctx, results)
    await self.create_poll(ctx, results)
    
async def setup(bot):
  await bot.add_cog(Poll(bot))