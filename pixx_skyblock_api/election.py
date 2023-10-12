import discord
import aiohttp
from PIL import Image
import requests
from io import BytesIO
import random


emotes={
    # Mayors
    "Aatrox": "<:Aatrox_Sprite:1161710871555346452>",
    "Cole": "<:Cole_Sprite:1161710879327408169>",
    "Derpy": "<:Derpy_Sprite:1161710857957421147>",
    "Diana": "<:Diana_Sprite:1161710876605284524>",
    "Diaz": "<:Diaz_Sprite:1161710874650751150>",
    "Finnegan": "<:Finnegan_Sprite:1161710841347985418>",
    "Foxy": "<:Foxy_Sprite:1161710865125474384>",
    "Marina": "<:Marina_Sprite:1161710862403371088>",
    "Paul": "<:Paul_Sprite:1161710860679512215>",
    "Scorpius": "<:Scorpius_Sprite:1161710843919081542>",
    "Villager": "<:Villager_Sprite:1161710853301751939>",
    # Other
    "Fairy soul": "<:fairy_soul:1161953288686678108>",
    "Coins": "<:Coins:1161952966442496080>",
    "XP": "<:experience_bottle:1161952849601773588>",
    # Rarity Emojis
    "Common": "<:common:1161956252973289542>",
    "Uncommon": "<:uncommon:1161956283356807229>",
    "Rare": "<:rare:1161956310238122034>",
    "Epic": "<:epic:1161956344652365874>",
    "Legendary": "<:legendary:1161956395336335460>",
    "Mythic": "<:mythic:1161956437623316492>",
    "Divine": "<:divine:1161956434838290473>",
    "Special": "<:special:1161956433332551700>",
}
#get
async def get_elections_data():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.hypixel.net/resources/skyblock/election") as response:
            data = await response.json()
            return data




#embed
async def create_elections_embed():
    data = await get_elections_data()
    if not data or "error" in data:
        return "Error fetching election data from the API."

    election = data.get("mayor", {}).get("election", {})
    candidates = election.get("candidates", [])

    embed = discord.Embed(title="SkyBlock Election Information", description=f"Year: {election.get('year')}")

    max_votes = 0  # Track the candidate with the most votes
    max_votes_candidate = None

    for candidate in candidates:
        mayor_name = candidate["name"]
        emote = emotes.get(mayor_name, "")
        
        embed.add_field(
            name=f"{emote} {mayor_name}",
            value=f"Votes: `{candidate['votes']}`",  # Wrap votes in code box
            inline=False
        )
        formatted_perks = format_perks(candidate['perks'])
        embed.add_field(
            name="Perks",
            value=formatted_perks,
            inline=False
        )

        if candidate['votes'] > max_votes:
            max_votes = candidate['votes']
            max_votes_candidate = f"{emote} 🏆 {mayor_name}"

        # Add a divider
        embed.add_field(name="\u200b", value="\u200b", inline=False)

    # Set the small image to the right of the embed
    embed.set_thumbnail(url="https://pixx.pics/wp-content/uploads/2023/10/Book_and_Quill.webp")

    return embed

def format_perks(perks):
    formatted_perks = ""
    for perk in perks:
        formatted_perks += f"{perk['name']}: {perk['description']}\n"
    return formatted_perks
