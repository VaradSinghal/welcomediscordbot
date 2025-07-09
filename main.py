import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1390971640040525956)
    if channel:
        await channel.send(f"🎉 Welcome to the server, {member.mention}!")
    else:
        print("❌ Channel not found.")


token = os.getenv("TOKEN")
if token is None:
    raise ValueError("TOKEN environment variable not set")
bot.run(token)
