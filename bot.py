import discord
import asyncio
import os
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
USER_ID = 1300374418429575169

PREFIX = "🕷 "  # НЕВИДИМЫЙ символ, фиксит прыжки в списке

nicknames = [
    PREFIX + "Папа заходит в офис",
    PREFIX + "Шалавы в шоке",
    PREFIX + "Пока папа работал",
    PREFIX + "Летели логи",
    PREFIX + "Папе дайте потрогать",
    PREFIX + "Тити и жопу",
    PREFIX + "Папа заводит",
    PREFIX + "Моя цель разрушить",
    PREFIX + "Дропнул как трек",
    PREFIX + "Не буду пушить",
    PREFIX + "Она не лучше",
    PREFIX + "Улыбка до ушей",
    PREFIX + "Я воркаю один",
    PREFIX + "За минуту три лога",
    PREFIX + "Пальцы в крови",
    PREFIX + "Мне нужен профит",
    PREFIX + "Обход Vinted",
    PREFIX + "Папа чистит логи",
    PREFIX + "Сделал так много",
    PREFIX + "Подделал подписи",
    PREFIX + "По дороге",
    PREFIX + "Папа параноит",
    PREFIX + "Savage",
    PREFIX + "Во мне бокал вина",
    PREFIX + "Свэг от меня",
    PREFIX + "Деньги для себя",
    PREFIX + "У папы семья",
    PREFIX + "Папа 812",
    PREFIX + "Папа па папа",
    PREFIX + "Тити и жопу",
    PREFIX + "Вся эта кровь"
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








