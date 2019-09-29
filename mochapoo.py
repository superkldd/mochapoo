import discord
import os
import requests
import asyncio
import random
from discord.ext import commands
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
                await channel.send("```" + name + " 님이 방송을 시작하였습니다.알로알로!!\n 방송 주소 : twitch.tv/mochapoo" + "```")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)

@client.event
async def on_message(message):
    global msg
    if message.content.startswith('!안녕'):
        await message.channel.send("```알로알로!!!```")
    
    if message.content.startswith('!알로알로'):
        await message.channel.send("```알로알로!!!```")   
        
    if message.content.startswith('!에몽언니'):
        await message.channel.send("```에몽언니 트위치 주소 : twitch.tv/emongss/ ```") 
        
    if message.content.startswith('!쏘정언니'):
        await message.channel.send("```쏘정언니 트위치 주소 : twitch.tv/ssozung/ ```")
        
    if message.content.startswith('!은진언니'):
        await message.channel.send("```은진언니 트위치 주소 : twitch.tv/eunjin2/ ```")
     
    if message.content.startswith('!명령어'):
        file = open("명령어.txt")
        await message.channel.send("```" + file.read() + "```")
        file.close()
        
    if message.content.startswith("!골라"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice) - 1)
        choiceresult = choice[choicenumber]
        await message.channel.send("```" + choiceresult + "```")
        
    if message.content.startswith("!따라해"):
        memory = message.content[5:]
        memorychat = memory.split(" ")
        await message.channel.purge(limit=1)
        await message.channel.send(memory)
        
    if message.content.startswith("!팀나누기"):
        team = message.content[6:]
        peopleteam = team.split(" / ")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send("```" + person[i] + "->" + teamname[i] + "```\n" )
            
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

