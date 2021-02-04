import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# TODO: Issue #1 Create a description for the bot.
bot = commands.Bot(command_prefix="!", description="Bot description.")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='ping', help='Pings the bot.')
async def ping(ctx):
    await ctx.send("pong!")

bot.run(TOKEN)
