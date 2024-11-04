import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv



load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = "http://localhost:3000"

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret= client_secret, 
                                                                              redirect_uri= redirect_uri, scope = "user-read-currently-playing user-modify-playback-state user-read-playback-state"))


def get_current_playing():
    artists = ""
    result =  spotify.current_user_playing_track()
    for s in result['item']['artists']:
        artists += s['name'] + ", "
    return result['item']['name'] + " by " + artists.rstrip(', ')

def skip_song():
    spotify.next_track()
    return "Song skipped."

def prev_song():
    spotify.previous_track()
    return "Previous track playing"
    


def set_volume(volume):
    try:
        if(volume > 100):
            volume = 100
        elif(volume < 0):
            volume = 0 
        spotify.volume(volume_percent=volume)
        return volume
    except TypeError:
        return "Volume must be a number"

def control(stop):
    try:
        if stop == True:
            spotify.pause_playback()
            return "Paused"
        else:
            spotify.start_playback()
            return "Resuming"
    except TypeError:
        return "Must be true or false"

def view_queue():
    q = spotify.queue()
    song_display = ""
    
    
    for item in q['queue']:
        s = item['artists']
        song_display += f"{item['name']} by {s[0]['name']}\n"
    return song_display
            


def skip(seconds):
    try:
        seconds *= 1000
        ## if the number of seconds is bigger than song length it skips
        spotify.seek_track(seconds)
        return seconds / 1000
    except:
        return "Value must be a positive number"

def toggle_mode(mode):
    match mode.lower():
        case "track":
            spotify.repeat("track")
            return "Track set on repeat"
        #Context - the repeat without 1
        case "context":
            spotify.repeat("context")
            return "Playlist set on repeat"
        case "shuffle": 
            spotify.shuffle(True)
            return "Playlist on shuffle"
        case _:
            return "Invalid command, please use 'Track, shuffle, or context' "



            
    



