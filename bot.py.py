import os
import discord
from discord.ext import commands
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def collected(ctx):

    farmers_role = discord.utils.get(ctx.author.roles, name="Farmers Club")

    if farmers_role:
        await ctx.send(
            f"{ctx.author.mention}, Farmers Club timer started! I'll remind you in 1.5 hours."
        )

        await asyncio.sleep(5400)  # 1.5 hours

        await ctx.send(
            f"{ctx.author.mention}, you can collect again!"
        )

    else:
        await ctx.send(
            f"{ctx.author.mention}, timer started! I'll remind you in 2 hours."
        )

        await asyncio.sleep(7200)  # 2 hours

        await ctx.send(
            f"{ctx.author.mention}, you can collect again!"
        )

bot.run(TOKEN)