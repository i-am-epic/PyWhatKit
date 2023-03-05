import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import pprint

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="2a11bcf59a0d42b9ac76a6164ca69301",
                                                           client_secret="c9d64682ede34421926d3bd159c9472d",redirect_uri="https://web.whatsapp.com/#",
                                               scope="user-library-read"))

#results = sp.current_user_playing_track()

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = 'BQBZWLwp9nIfVTbWtIcsC5AzCSdQvJm7gi0kmod0jfYMTG_flv8BXDnE3DQMnmaSsIdXyQWC8-67JuIS3HSdR6wHlRSraSxa-xUpFfqd7tw5lujwqZxhol8tn2jY9YDxG9t43fMZr-2BfrJY2JsJ6MfCO86gAe-7JMbm9GlrpGpoR1W2_bXYSYZ9cL9RdK5TOHxvdhf2K7zScA'



def get_current_play(access_token):
    response = requests.get(SPOTIFY_GET_CURRENT_TRACK_URL,headers={"Authorization":f"Bearer {access_token}"
                                                               
                                                               })
    res_json = response.json()
    #print(res_json)
    track_id = res_json['item']['id']
    track_name = res_json['item']['name']

    artists = res_json['item']['artists']
    artists_name = ", ".join([artist['name'] for artist in artists])
    link = res_json['item']['external_urls']['spotify']


    current_track_info = {"id" : track_id,
                          "name" : track_name,
                          "artist"  : artists_name,
                          "link"  :link}
    
    return current_track_info

def main():
    current_track_info = get_current_play(SPOTIFY_ACCESS_TOKEN)
    print(current_track_info)
    return current_track_info


if __name__ == "__main__":
    main()
    
