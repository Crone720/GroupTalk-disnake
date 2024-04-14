import disnake, random, string, datetime
from utils.db import add_thread
from utils.view.ActionSecond import ActionSecondButton
class CreateGroupModal(disnake.ui.Modal):
    def __init__(self, channel):
        self.channel = channel
        components = [
            disnake.ui.TextInput(
                label="Введите Название",
                placeholder="<3",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                max_length=25,
            )
        ]
        super().__init__(
            title=f"Создание Группы",
            custom_id="id3",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        name = inter.text_values["name"]
        channel = inter.guild.get_channel(self.channel)
        category = inter.guild.get_channel(channel.category_id)
        nchannel = await inter.guild.create_text_channel(name, category=category)
        await nchannel.set_permissions(inter.guild.default_role, view_channel=False)
        await nchannel.set_permissions(inter.author, view_channel=True)
        embed = disnake.Embed(title="Создание Группы", description=f"{inter.author.mention}, Вы успешно **создали** группу {nchannel.mention}\n"
                                                                    "Пожалуйста **не** нарушайте **правила** Discord и TOS")
        await inter.send(embed=embed, ephemeral=True)
        embed = disnake.Embed(title="Группа", description="Чтобы управлять комнатой выберите **кнопку** ниже.")
        await nchannel.send(embed=embed, view=ActionSecondButton())
        length = random.randint(5, 8)
        characters = string.ascii_letters + string.digits[1:]
        code = ''.join(random.choice(characters) for _ in range(length))
        await add_thread(inter.author.id, code, nchannel.id, int(datetime.datetime.now().timestamp()))