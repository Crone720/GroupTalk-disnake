import disnake
class ChangeNameModal(disnake.ui.Modal):
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
            title=f"Переименование Группы",
            custom_id="id3",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        name = inter.text_values["name"]
        channel = inter.guild.get_channel(self.channel)
        await channel.edit(name=name)
        await inter.response.send_message(f"Вы переименовали группу в `{name}`", ephemeral=True)