import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, activity= disnake.Game('Minecraft', status = disnake.Status.streaming))
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    print(f'{message.author.name} ({message.author.id}): {message.content}')
    await message.channel.send(f'{message.content}')

    await bot.process_commands(message)

bot.run('')
