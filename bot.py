import discord
import asyncio
import os
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
USER_ID = 1452060173739757763

nicknames = ["夜", "影", "無", "☾", "黒"]

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Запущен как {bot.user}")

    await bot.wait_until_ready()

    while True:
        for guild in bot.guilds:
            try:
                member = await guild.fetch_member(USER_ID)
                for nick in nicknames:
                    await member.edit(nick=nick)
                    print(f"Ник сменён на {nick}")
                    await asyncio.sleep(300)  # 5 минут
            except Exception as e:
                print("Ошибка:", e)

bot.run(TOKEN)
