import discord
import aiohttp

class PetMenuView(discord.ui.View):
    def __init__(self, pets_data, user_uuid, api_key):
        super().__init__()
        self.pets_data = pets_data
        self.current_index = 0
        self.user_uuid = user_uuid
        self.api_key = api_key

    @discord.ui.button(label="Previous", style=discord.ButtonStyle.secondary, emoji="⬅️")
    async def previous_pet(self, button, interaction):
        self.current_index = (self.current_index - 1) % len(self.pets_data)
        await interaction.response.edit_message(embed=self.create_pet_embed(), view=self)

    @discord.ui.button(label="Next", style=discord.ButtonStyle.secondary, emoji="➡️")
    async def next_pet(self, button, interaction):
        self.current_index = (self.current_index + 1) % len(self.pets_data)
        await interaction.response.edit_message(embed=self.create_pet_embed(), view=self)

    @discord.ui.button(label="Home", style=discord.ButtonStyle.secondary, emoji="🏠")
    await home(self, button, interaction)

    def create_pet_embed(self):
        pet = self.pets_data[self.current_index]
        embed = discord.Embed(title=f"{pet['type']} [{pet['tier']}]",
                              description=f"EXP: {pet['exp']}\nActive: {pet['active']}",
                              color=discord.Color.blurple())
        # Utilizing the provided URL format to display the pet image
        embed.set_thumbnail(url=f"https://mc-heads.net/head/{pet['uuid']}")
        return embed
