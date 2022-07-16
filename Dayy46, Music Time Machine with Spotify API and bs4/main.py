import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "15f082f3fe1b470f97e38ff9332aad9d"
CLIENT_SECRET = "3739ba70e2a047489934616011ef0dd5"

date = input("Which year do you want to travel to? (YY-MM-DD): ")
songs_url = f"https://www.billboard.com/charts/hot-100/{date}/"

respond = requests.get(songs_url)
soup = BeautifulSoup(respond.text, "html.parser")

song = soup.select(selector="li ul h3")
songs = [xx.getText().strip() for xx in song]
with open("songs.txt", "w") as file:
    for i in song:
        file.write(i.getText().strip())
        file.write("\n")

    file.write("sdfasdfasdf\n")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope="playlist-modify-public",
        redirect_uri="https://example.com/callback/",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

songs_uri = []
for i in songs:
    #print(sp.search(q=f"track:{i} year:2000", type="track", limit=1)["tracks"]["items"][0]["uri"])
    try:
        songs_uri.append(sp.search(q=f"track:{i} year:{date.split('-')[0]}", type="track", limit=1)["tracks"]["items"][0]["uri"])
    except:
        print("This song is not avaible in Spotify: ",i)

playlist = sp.user_playlist_create(user=user_id, name=f"Hit songs from {date}",
                                   description="This playlist was created by python-spotif api project. It takes hit songs from www.billboard.com")


sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri, position=None)
