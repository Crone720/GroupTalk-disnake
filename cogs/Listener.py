from utils.db import create_db
from disnake.ext import commands
from utils.view.Action import ActionButton 
from utils.view.ActionSecond import ActionSecondButton
class GroupListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False
    @commands.Cog.listener()
    async def on_ready(self):
        if self.persistent_views_added:
            return
        
        await create_db()
        self.bot.add_view(ActionButton())
        self.bot.add_view(ActionSecondButton())
def setup(bot):
    bot.add_cog(GroupListener(bot))