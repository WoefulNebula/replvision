import disnake
from disnake.ext import commands
from disnake.enums import ButtonStyle

class row_buttons(disnake.ui.View):
	def __init__(self, author):
		self.author = author
		self.value = -1
		super().__init__(timeout=None)
		
	@disnake.ui.button(label="Rock", style=ButtonStyle.red)
	async def rock(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
		if self.author == interaction.author.id:
			await interaction.response.send_message("You have chosen rock", ephemeral=True)
			self.value = 0
			self.stop()

	@disnake.ui.button(label="Paper", style=ButtonStyle.green)
	async def paper(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
		if self.author == interaction.author.id:
			await interaction.response.send_message("You have chosen paper", ephemeral=True)
			self.value = 1
			self.stop()

	@disnake.ui.button(label="Scissors", style=ButtonStyle.blurple)
	async def scissors(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
		if self.author == interaction.author.id:
			await interaction.response.send_message("You have chosen scissors", ephemeral=True)
			self.value = 2
			self.stop()
		