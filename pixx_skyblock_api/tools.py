import discord
import aiohttp
from PIL import Image
import requests
from io import BytesIO
import random


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
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                print(f"Error fetching skyblock profile: {response.status}")
                return None
            data = await response.json()
            return data

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
