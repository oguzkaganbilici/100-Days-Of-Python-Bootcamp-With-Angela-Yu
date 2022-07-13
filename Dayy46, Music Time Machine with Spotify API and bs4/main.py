from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID="15f082f3fe1b470f97e38ff9332aad9d"
SPOTIPY_CLIENT_SECRET="37363338f766462187824e31154c81c2"
SP_URL = "http://example.com"

date = input("Which year do you want to travel to?: YY-MM-DD ")
url = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
respond = BeautifulSoup(url.text, "html.parser")

#songs = respond.find_all(name="h3", id="title-of-a-story",class_="c-title a-no-trucate")
songs = respond.select(selector="li.o-chart-results-list__item h3")
with open("songs.txt", "w") as file:
    for i in songs:
        file.write(i.getText().strip())
        file.write("\n")

"""sp = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                                 redirect_uri=SP_URL, scope="playlist-modify-private")

#access_token = sp.get_access_token()
acc_tok = {"access_token": "BQB3sMVOBsHPFxq1MUhdIZDbKgxz-p56XCBE9YgGpXB2GoYqqIa9XBEGZI_xB8MkwvNd6wMjHpq5wD0veuqPFykgDz76TuKjn1x7MO1SxFhaXGOTM1TcXD-Xdc6J7PaQJGaKzCT-OVSlt-4Ako79QbZxheimrGPROXYLgfVGp_bH1vGZjIQ9thP7FuFLwxTpXcHkEXkIIIoRJbDjVNZj",
           "token_type": "Bearer",
           "expires_in": 3600,
           "refresh_token": "AQAQtLE0JE_dEW8EZz5uKKed-uJfhxpt0lawxEho2s_8YZxXC4bB5PKZ48su9wO7JVexvtIMxi8GxpMWOANaVyevr_e9_zzsz3PbwFpgi64LZ6un4p__RZYoeHNyzFU23YY",
           "scope": "playlist-modify-private",
           "expires_at": 1657714461}

spoti = spotipy.Spotify(acc_tok["access_token"])
print(spoti.current_user())



"""