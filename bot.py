import discord
import asyncio
import os
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
USER_ID = 1300374418429575169

PREFIX = "🕷 "  # НЕВИДИМЫЙ символ, фиксит прыжки в списке
SUFFIX = " 🕷"

nicknames = [
    PREFIX + "Папа заходит в офис" + SUFFIX,
    PREFIX + "Шалавы в шоке" + SUFFIX,
    PREFIX + "Пока папа работал" + SUFFIX,
    PREFIX + "Летели логи" + SUFFIX,
    PREFIX + "Папе дайте потрогать" + SUFFIX,
    PREFIX + "Тити и жопу" + SUFFIX,
    PREFIX + "Папа заводит" + SUFFIX,
    PREFIX + "Моя цель разрушить" + SUFFIX,
    PREFIX + "Дропнул как трек" + SUFFIX,
    PREFIX + "Не буду пушить" + SUFFIX,
    PREFIX + "Она не лучше" + SUFFIX,
    PREFIX + "Улыбка до ушей" + SUFFIX,
    PREFIX + "Я воркаю один" + SUFFIX,
    PREFIX + "За минуту три лога" + SUFFIX,
    PREFIX + "Пальцы в крови" + SUFFIX,
    PREFIX + "Мне нужен профит" + SUFFIX,
    PREFIX + "Обход Vinted" + SUFFIX,
    PREFIX + "Папа чистит логи" + SUFFIX,
    PREFIX + "Сделал так много" + SUFFIX,
    PREFIX + "Подделал подписи" + SUFFIX,
    PREFIX + "По дороге" + SUFFIX,
    PREFIX + "Папа параноит" + SUFFIX,
    PREFIX + "Savage" + SUFFIX,
    PREFIX + "Во мне бокал вина" + SUFFIX,
    PREFIX + "Свэг от меня" + SUFFIX,
    PREFIX + "Деньги для себя" + SUFFIX,
    PREFIX + "У папы семья" + SUFFIX,
    PREFIX + "Папа 812" + SUFFIX,
    PREFIX + "Папа па папа" + SUFFIX,
    PREFIX + "Тити и жопу" + SUFFIX,
    PREFIX + "Вся эта кровь" + SUFFIX
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









