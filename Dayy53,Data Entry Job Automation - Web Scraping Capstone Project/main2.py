from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time

form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSdOhLBd_TmbtIKnfb3c3lZvKrRsgFUmkfWu1-Dthbr3O4YZaA/viewform?usp=sf_link'
property_link = "https://www.hepsiemlak.com/ankara-kiralik"


respond = requests.get(property_link)
soup = BeautifulSoup(respond.text, 'html.parser')

properties = soup.find_all(name='a', class_='card-link')
links = ['https://www.hepsiemlak.com' + i['href'] for i in properties]

prices = soup.find_all(name='span', class_='list-view-price')
prices_ = [float(xx.text.strip().split('\n')[0])*1000 for xx in prices]

properties = soup.find_all(name='span',class_='celly houseRoomCount')
properties_ = soup.find_all(name='span', class_='celly squareMeter list-view-size')
properties__ = [i.text.strip() for i in properties_]

full_properties = [properties__[i] + ' | ' + properties[i].text for i in range(0, len(properties))]

location = soup.find_all(name='div', class_='list-view-location')
location_ = [xx.text.strip().split('\n')[0] + xx.text.strip().split('\n')[2].strip() for xx in location]

drive = webdriver.Chrome('chromedriver.exe')

drive.get(form_link)
time.sleep(3)
        
for i in range(0, 24):
    answer_address = drive.find_element(By.XPATH,
                                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer_address.send_keys(location_[i])
        
    answer_price = drive.find_element(By.XPATH,
                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer_price.send_keys(prices_[i])
        
    answer_link = drive.find_element(By.XPATH,
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer_link.send_keys(links[i])
        
    send_button = drive.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    time.sleep(2)
    send_button.click()
    time.sleep(2)
    send_another = drive.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_another.click()
    time.sleep(1)
        
drive.quit()
