import discord
import asyncio
import os
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
USER_ID = 1452060173739757763

nicknames = [
    "Папа заходит в офис",
    "Шалавы в шоке",
    "Пока папа работал",
    "Летели логи",
    "Папе дайте потрогать",
    "Тити и жопу",
    "Папа заводит",
    "Моя цель разрушить",
    "Дропнул как трек",
    "Не буду пушить",
    "Она не лучше",
    "Улыбка до ушей",
    "Я воркаю один",
    "За минуту три лога",
    "Пальцы в крови",
    "Мне нужен профит",
    "Обход Vinted",
    "Папа чистит логи",
    "Сделал так много",
    "Подделал подписи",
    "По дороге",
    "Папа параноит",
    "Savage",
    "Во мне бокал вина",
    "Свэг от меня",
    "Деньги для себя",
    "У папы семья",
    "Папа 812",
    "Папа па папа",
    "Тити и жопу",
    "Вся эта кровь"
]

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
                    await asyncio.sleep(0.77)  # 5 минут
            except Exception as e:
                print("Ошибка:", e)

bot.run(TOKEN)

