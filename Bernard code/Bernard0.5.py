import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game



Client = discord.client
client = commands.Bot(command_prefix = 'b!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='deviancy'))
    print('Model AP700 is ready.') 


@client.event
async def on_message(message):
    if message.content == 'b!ping':
        await client.send_message(message.channel,'pong')
    if message.content == 'b!loki':
        em = discord.Embed(description='AP700 hugged you!')
        em.set_image(url='https://cdn.discordapp.com/attachments/466028163944677398/497056508262088706/244a0b6c27003dc395ff5212044b5e96.gif')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('b!random'):
        randomlist = ["hello", "goodbye"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('b!hug <@USER_ID>'):
        randomlist = ['https://cdn.discordapp.com/attachments/466028163944677398/497056392222343171/13321653494973.gif',
                      'https://cdn.discordapp.com/attachments/466028163944677398/497056354507292673/UzjV.gif',
                      'https://cdn.discordapp.com/attachments/466028163944677398/497056508262088706/244a0b6c27003dc395ff5212044b5e96.gif']
        em = discord.Embed(description =  'Bernard hugged <@USER_ID>',)
        em.set_image(url='%s' %(random.choice(randomlist),))
        await client.send_message(message.channel, embed=em)
        
client.run('NDk3MDY0Mzk3MzE1ODk5Mzk1.Dp-C0A.RJlPmSgp6ZvvCKkgVn2ZwC4SWFE')
