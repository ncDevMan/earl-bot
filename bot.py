# bot.py
import os
import discord
from dotenv import load_dotenv
import json
from discord import Game
from discord.ext.commands import Bot
from imgurpython import ImgurClient
from random import randint
from time import sleep

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()


# CONFIG
BOT_PREFIX = (">")

client = Bot(command_prefix=BOT_PREFIX)

# From IMGUR
client_id = os.getenv('IMGUR_ID')
client_secret = os.getenv('IMGUR_SECRET')'




# getMemes Function()
# Hits IMGUR API and returns imgur link
# By- Nick Conn
def get_meme():

    
    subreddits = [
        'holdmybeer',
        'funny',
        'whitepeopletwitter',
        'holdmyfries',
        'MemeEconomy',
        'wholesomememes',
        'dankmemes',
        'Whatcouldgowrong',
        'RedneckGifs',
        'gifs'
    ]
    # Get Length of list
    subRedditLength = len(subreddits)
    subRedditKey = randint(0, subRedditLength-1)

    # Plug this into api for a random subreddit
    subReddit = subreddits[subRedditKey]
    
    # Connect to Client
    client = ImgurClient(client_id, client_secret)


    # https://github.com/Imgur/imgurpython
    items = client.subreddit_gallery(subReddit, sort='top', window='day', page=0)


    # Grab the length of the dictionary returned from IMGUR
    imgurLength = len(items)

    if imgurLength != 0:
        # Get random element
        key = randint(0, imgurLength)

        # Grab random meme link
        link = items[key].link

        return link
    else:
        return 'Please try again!'






# ------------------------------- Main -------------------------------

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('>hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send('Earl has arrived!')

    # Lets make a meme feature!
    if message.content.startswith('>meme'):
        
        meme = get_meme()
        msg = meme.format(message)
        await message.channel.send(msg)

        # IMGUR API nonsense
        sleep(2)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)