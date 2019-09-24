import discord
import os
import requests
import asyncio
from json import loads



client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print("ready")
    game = discord.Game("열심히")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "mochapoo"
    name = "모카똥"
    channel = client.get_channel(357188444872507396)
    a = 0
    while True:
        headers = {'Client-ID': '6vcpx7k4l6oiokev21orjk5mcmh2ej'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send("```" + name + " 님이 방송을 시작하였습니다.알로알로!!" + "```")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

