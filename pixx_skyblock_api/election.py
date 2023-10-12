import discord
import aiohttp
from PIL import Image
import requests
from io import BytesIO
import random

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
