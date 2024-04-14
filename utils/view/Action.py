from typing import Optional
import disnake
from utils.db import *
from utils.view.JoinGroupModal import JoinGroupModal
from utils.view.CreateGroupModal import CreateGroupModal
class ActionButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Создать группу", custom_id="create_group")
    async def create_group(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        b = await get_thread(interaction.author.id)
        embed = disnake.Embed(title="Создание Группы", description=f"У вас уже есть группа <#{b}>")
        if b:
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.response.send_modal(modal=CreateGroupModal(interaction.channel_id))

    @disnake.ui.button(label="Присоединиться", custom_id="join_group")
    async def join_group(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_modal(modal=JoinGroupModal())