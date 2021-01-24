import discord
import dotenv
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!')

initial_extensions = (
    'cogs.make_scene'

)

if __name__ == '__main__':

    for extension in initial_extensions:
        bot.load_extension(extension)


bot.run(token)

