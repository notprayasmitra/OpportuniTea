import discord
from discord.ext import commands
import config

# Setup permissions
intents = discord.Intents.default()
intents.message_content = True  # Allows reading/sending messages

# Initialize the bot with a command prefix (e.g., >ping)
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in successfully as {bot.user.name} (ID: {bot.user.id})")
    print("------")

@bot.command()
async def ping(ctx):
    """A simple test command to ensure the bot is responsive."""
    await ctx.send("Pong!")

# Run the bot using the token from config.py
bot.run(config.BOT_TOKEN)