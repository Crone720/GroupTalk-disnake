from typing import Optional
import disnake
from utils.db import *
from utils.view.ChangeNameModal import ChangeNameModal
class ActionSecondButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Информация", custom_id="information_group")
    async def information_group(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        data = await get_thread_info(interaction.channel_id)

        embed = disnake.Embed(title="Информация о группе")
        for row in data:
            time = row[3]
            embed.add_field(name="Владелец Группы", value=f"<@{row[0]}>", inline=False)
            embed.add_field(name="Код Группы", value=f"`{row[1]}`", inline=False)
            embed.add_field(name="Создан", value=f"<t:{time}:R>", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @disnake.ui.button(label="Переименовать", custom_id="rename_group")
    async def rename_group(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        b = await get_owner_thread(interaction.channel_id)
        if b == interaction.author.id:
            await interaction.response.send_modal(modal=ChangeNameModal(interaction.channel_id))
        else:
            await interaction.response.send_message("Вы не владеете данной группой", ephemeral=True)

    @disnake.ui.button(label="Удалить группу", custom_id="delete_group")
    async def delete_group(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        b = await get_owner_thread(interaction.channel_id)
        if b == interaction.author.id:
            await del_thread(interaction.channel_id)
            await interaction.channel.delete()
        else:
            await interaction.response.send_message("Вы не владеете данной группой", ephemeral=True)

    @disnake.ui.button(label="Покинуть группу", custom_id="leave_group")
    async def leave_group(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        b = await get_owner_thread(interaction.channel_id)
        if b == interaction.author.id:
            await interaction.response.send_message("Вы не можете покинуть группу, так как вы её создавали", ephemeral=True)
        else:
            await interaction.channel.set_permissions(interaction.author, view_channel=False)
            embed1 = disnake.Embed(title="Пиу Пиу Пиу(", description=f"Из группы покинул участник: {interaction.author.mention}")
            await interaction.response.send_message(embed=embed1)