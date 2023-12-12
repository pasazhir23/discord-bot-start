import disnake
from disnake.ext import commands

# Создание объекта бота
bot = commands.Bot(command_prefix='!')

# Обработчик события запуска бота
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Обработчик события нового сообщения
@bot.event
async def on_message(message):
    # Игнорирование сообщений от ботов, чтобы избежать зацикливания
    if message.author.bot:
        return

    # Вывод информации о сообщении в консоль
    print(f'{message.author.name} ({message.author.id}): {message.content}')
    await message.channel.send(f'{message.content}')

    # Не забываем обработку команд, чтобы они продолжали работать
    await bot.process_commands(message)

bot.run('ODAyMjgyMjM1NDM1OTQxOTM5.GyEP1g.RkloSDXL45dXYiDUUSTjf7b9i3e7MxxsZdJW5M')