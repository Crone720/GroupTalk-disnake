import disnake
from disnake.ext import commands
from utils.config import TOKEN

bot = commands.Bot(
    command_prefix="group/", 
    intents=disnake.Intents.all(), 
    help_command=None,
    reload=True
)

@bot.event
async def on_ready():
    print(f'Бот запустился')

bot.load_extensions("cogs")
bot.run(TOKEN)