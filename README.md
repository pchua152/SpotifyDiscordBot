## Spotify-Discord Bot

# About the project
This project is a Python program that interacts with the Spotify Web API to perform actions that are relevant for users who are listening to music. 
The program can perform the following features:
  * Display the current song playing
  * Skip the current song or play the previous track
  * Set the volume of the player
  * Pause/Play
  * View what is next in the queue
  * Fast forward any amount of seconds ahead
  * Put player on repeat, shuffle, or repeat one
The program is also integrated with a Discord bot that allows you to use these commands within Discord.

# Requirements
In order to use this program, you will need:
  * A Spotify Account (Free users can still use this app, but should be aware some features are limited due to the Web API limitations)
  * [A Spotify Developer Account](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)
  * Spotipy and discord.py have to be installed for the program to work.
      - pip install spotipy discord.py

# Installation
In the Spotify Developer Dashboard, create a web app to use the API. The app will create a client_id and client_secret. Replace the variables with these names in spotifyapi.py file with the corresponding values. This allows the API to function using your account. Also, to have the bot return a message when it becomes online, replace channel_id in the spotify_bot.py with the desired channel ID which can be found by right clicking a channel -> copy channel ID. If not, this field is optional so you can remove channel_id references.

python spotify_bot.py runs runs the bot and all commands as well as descriptions are available by starting a message with /
 
