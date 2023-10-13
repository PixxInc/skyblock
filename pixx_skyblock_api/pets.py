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
    async def home(self, button, interaction):

        main_menu_view = MyView()
        embed = discord.Embed(title="SkyBlock Functions Menu", description="Select an option below:")

        embed.add_field(name=":bar_chart: Player Profiles", value="Get SkyBlock player profiles.", inline=True)
        embed.add_field(name=":busts_in_silhouette: User Online Check", value="Check the online status of a specific player.", inline=True)
        embed.add_field(name=":department_store: Bazaar", value="Search for Bazaar prices.", inline=True)
        embed.add_field(name=":hammer: Auctions", value="View active auctions.", inline=True)
        embed.add_field(name=":classical_building: Elections and Mayors", value="Information about elections and mayors.", inline=True)
        embed.add_field(name="⚙️ More soon", value="Nothing here yet", inline=True)
        await interaction.response.send_message(embed=embed, view=main_menu_view)

    def create_pet_embed(self):
        pet = self.pets_data[self.current_index]
        embed = discord.Embed(title=f"{pet['type']} [{pet['tier']}]",
                              description=f"EXP: {pet['exp']}\nActive: {pet['active']}",
                              color=discord.Color.blurple())
        # Utilizing the provided URL format to display the pet image
        embed.set_thumbnail(url=f"https://mc-heads.net/head/{pet['uuid']}")
        return embed
