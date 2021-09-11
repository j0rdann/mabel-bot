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

@client.event
async def on_ready():
    print(client.guilds)
    for servers in client.guilds:
        if servers.name == SERVER:
            print(f'{client.user} has connected to the discord server {servers.name}!')

client.run(TOKEN)