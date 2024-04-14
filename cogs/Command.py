import disnake
from disnake.ext import commands
from utils.config import DESCRIPTION
from utils.view.Action import ActionButton
class GroupCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description=DESCRIPTION)
    async def group(self, interaction: disnake.AppCommandInteraction):
        embed = disnake.Embed(description="> Если вы с друзьями ищите место для приятного\n"
                                          "> времяпрепровождения, то создайте приватную ветку для\n"
                                          "> общения без ограничений.")
        await interaction.response.send_message(embed=embed, view=ActionButton())

def setup(bot):
    bot.add_cog(GroupCommand(bot))