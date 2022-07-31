import requests
from bs4 import BeautifulSoup
from ele

form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSdOhLBd_TmbtIKnfb3c3lZvKrRsgFUmkfWu1-Dthbr3O4YZaA/viewform?usp=sf_link'
zillow_link = 'https://www.zillow.com/san-jose-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.2767031220703%2C%22east%22%3A-121.47332787792968%2C%22south%22%3A37.08960415669598%2C%22north%22%3A37.52761076383666%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",

    "Accept-Language": "en-US,en;q=0.9"
}
respond = requests.get(zillow_link, headers=headers)
soup = BeautifulSoup(respond.text, 'html.parser')
links = soup.find_all(name="a", class_="list-card-link")
prices = soup.find_all(name='div', class_='list-card-price')
adress = soup.find_all(name='address', class_='list-card-addr')
print(len(links))
print(len(prices))
print(len(adress))