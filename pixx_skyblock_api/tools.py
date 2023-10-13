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

async def convert_usename_to_uuid(username):
    url = f"https://playerdb.co/api/player/minecraft/{username}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                print(f"Error fetching UUID: {response.status}")
                return None
            data = await response.json()
            
            if 'data' in data and 'player' in data['data'] and 'id' in data['data']['player']:
                return data['data']['player']['id']
            else:
                return None

        

async def fetch_skyblock_profile_data(api_key, user_uuid):
    url = f"https://api.hypixel.net/skyblock/profiles?key={api_key}&uuid={user_uuid}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    print(f"Error fetching skyblock profile: {response.status}")
                    return None
                data = await response.json()
                return data
    except aiohttp.ClientError as e:
        print(f"HTTP Client Error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


async def convert_uuid_to_username(uuid):
    url = f"https://api.mojang.com/user/profiles/{uuid}/names"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(data[-1]['name'] if isinstance(data, list) and len(data) > 0 else "Unknown")
            return data[-1]['name'] if isinstance(data, list) and len(data) > 0 else "Unknown"

async def fetch_player_name(uuid):
    url = f"https://playerdb.co/api/player/minecraft/{uuid}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data['data']['player']['username']
            else:
                return None

async def get_dominant_color(image_url):
    # Fetch the image
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    

    image = image.resize((16, 16), 3)  
    

    result = image.convert('RGB').getcolors(256)
    max_occurence, most_present = 0, 0
    try:
        for c in result:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        dominant = most_present
        return dominant
    except TypeError:
        raise Exception("Too many colors in the image")
