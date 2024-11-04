import os
import discord
from discord import app_commands

from spotifyapi import *
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents = discord.Intents.default())
tree = app_commands.CommandTree(client)

channelid = os.getenv('channelid')


@client.event
async def on_ready():

    
    await tree.sync()
    await client.get_channel(int(channelid)).send("Hello, bot is online now")
    
    print(f'{client.user} is now online!')




@tree.command(name = "current", description= "Displays current song")
async def current_command(phrase: discord.Interaction):
    await phrase.response.send_message((get_current_playing()))

@tree.command(name = "skip", description = "Skips current song")
async def skip_command(phrase:discord.Interaction):
    await phrase.response.send_message(skip_song())
    
@tree.command(name = "previous", description = "Skips current song")
async def skip_command(phrase:discord.Interaction):
    await phrase.response.send_message(prev_song())

@tree.command(name = "volume", description= "Set volume")
@app_commands.describe(target_volume = "The volume to set Spotify to")
async def volume_command(phrase: discord.Interaction, target_volume: int):
    await phrase.response.send_message(f"Volume set to {set_volume(target_volume)}")


@tree.command(name = "pause", description = "Pause")
async def pause_command(phrase: discord.Interaction):
    await phrase.response.send_message(control(True))

@tree.command(name = "play", description= "Resume")
async def play_command(phrase: discord.Interaction):
    await phrase.response.send_message(control(False))

@tree.command(name = "seek",  description = "skips x amount of seconds")
@app_commands.describe(seconds=  "Amount of seconds wanted to skip")
async def skip_command(phrase: discord.Interaction, seconds: int):
    await phrase.response.send_message(f"Skipped {skip(seconds)} seconds")

#For toggle have it take what they want (repeat, context, shuffle)
@tree.command(name = "toggle", description= "Toggle between repeating or shuffling your playlist")
@app_commands.describe(mode = "The mode to play the playlist")
async def toggle_command(phrase: discord.Interaction, mode: str):
    await phrase.response.send_message(toggle_mode(mode))

    
@tree.command(name = "queue", description = "View your queue")
async def queue_command(phrase:discord.Interaction):
    await phrase.response.send_message(view_queue())

    
    
    
client.run(os.getenv('token'))
