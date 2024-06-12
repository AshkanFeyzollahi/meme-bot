"""MemeBot

The discord.py bot that uses https://meme-api.com/ to generate
memes and send them to discord servers"""

import os
from dotenv import load_dotenv

import requests

import discord
from discord.ext import commands

description = """The discord.py bot that uses https://meme-api.com/ to generate
memes and send them to discord servers"""

intents = discord.Intents.default()

intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="?", description=description, intents=intents)

load_dotenv()

@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.command("meme")
async def send_meme(ctx: commands.Context) -> None:
    response = requests.get("https://meme-api.com/gimme")
    
    if response.status_code == 200:
        response = response.json()
        
        await ctx.send(response["title"])
        await ctx.send(response["url"])
        return
    
    await ctx.send(str(response))

bot.run(os.environ["BOT_TOKEN"])
