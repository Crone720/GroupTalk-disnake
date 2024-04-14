import disnake
from utils.db import get_code_thread
class JoinGroupModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Введите Код Группы",
                placeholder="<3",
                custom_id="code",
                style=disnake.TextInputStyle.short,
                max_length=25,
            )
        ]
        super().__init__(
            title=f"Присоединение к Группе",
            custom_id="id31",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        code = inter.text_values["code"]
        b = await get_code_thread(code)
        if b:
            channel = inter.guild.get_channel(b)
            if inter.author in channel.members:
                embed = disnake.Embed(title="Присоединение к Группе", description=f"{inter.author.mention}, Вы уже находитесь в группе {channel.mention}")
                await inter.send(embed=embed, ephemeral=True)
            else:
                await channel.set_permissions(inter.author, view_channel=True)
                embed3 = disnake.Embed(title="Присоединение к Группе", description=f"{inter.author.mention}, Вы успешно **присоединились** к группе {channel.mention}")
                embed1 = disnake.Embed(title="Пиу Пиу Пиу", description=f"У нас пополнение в беседе. Новый участник: {inter.author.mention}")
                await inter.send(embed=embed3, ephemeral=True)
                await channel.send(embed=embed1)
        else:
            embed2 = disnake.Embed(title="Присоединение к Группе", description=f"{inter.author.mention}, Не найден код группы")
            await inter.send(embed=embed2, ephemeral=True)