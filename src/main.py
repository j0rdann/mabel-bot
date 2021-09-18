import os
import discord
from dotenv import load_dotenv
# Installing packages

load_dotenv()
# Initialise the shell environment

TOKEN =  os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER') # Make this into a list of different servers mabel is in????
client = discord.Client()
# Discord client variables, Change to AWS Secrets Manager

petActions = ["snort", "exists in pain", "attempts to breathe", "leaves a stain"] # Select actions from this list when mabel is given a pat
stainedActions = ["shits in your bath", "steals your chair"] # Select actions from this list when mabel is given a pat by a stained member
# List of mabel actions

@client.event
async def on_message(message):
    print("Message: " + message.content) # Change to logging storage when deployed

@client.event
async def on_ready():
    for servers in client.guilds:
        if servers.name == SERVER:
            print(f'{client.user} has connected to the discord server {servers.name}!') # Change to logging storage when deployed

client.run(TOKEN)