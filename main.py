import discord
import dotenv
import os

from base.bot import PPBot

def run():
  dotenv.load_dotenv()
  DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
  PLACES_KEY = os.getenv('PLACES_KEY')

  intents = discord.Intents.default()
  intents.message_content = True

  bot = PPBot(command_prefix='!', intents=intents, places_key=PLACES_KEY, discord_token=DISCORD_TOKEN)
  bot.initialize()

  bot.run(DISCORD_TOKEN,log_handler=None)

if __name__ == "__main__":
  run()



