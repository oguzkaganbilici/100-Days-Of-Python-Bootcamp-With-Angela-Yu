import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

respond = requests.get(URL)
respond = BeautifulSoup(respond.content, "html.parser")

movie = respond.find_all(name="h3", class_="title")
movies = [xx.getText() for xx in movie]

with open("top100.txt", "w") as file:
    for i in movies[::-1]:
        file.write(i)
        file.write("\n")

