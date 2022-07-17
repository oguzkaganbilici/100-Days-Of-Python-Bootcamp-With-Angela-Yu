import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP

MY_EMAIL = "delykurt@gmail.com"
MY_PASSWORD = "soscqgolxpzqprsb"

url = 'https://www.amazon.com.tr/Keycaps-Tu%C5%9Flar%C4%B1-Profil-Mekanik-Klavyesi/dp/B0989P4RSJ/ref=sr_1_33?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=18CFBU7TWH9AP&keywords=rk61&qid=1658053544&sprefix=rk61%2Caps%2C189&sr=8-33'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7'
}
respond = requests.get(url, headers=headers)
soup = BeautifulSoup(respond.text, 'lxml')

price = soup.find_all(name='span', class_="a-offscreen")
prices = [xx.getText() for xx in price]
our_price = float(prices[0].split('T')[0].replace(',','.'))

if our_price < 200:
    with SMTP('smtp.gmail.com', port=587) as mail:
        mail.starttls()
        mail.login(user=MY_EMAIL, password=MY_PASSWORD)
        mail.sendmail(from_addr=MY_EMAIL,to_addrs='oguzkaganbilici1@gmail.com',msg=f'Subject:Price Alert\nKeycaps price is {our_price}.It went down from 227,74TL. Go buy it as soon as possible!')
