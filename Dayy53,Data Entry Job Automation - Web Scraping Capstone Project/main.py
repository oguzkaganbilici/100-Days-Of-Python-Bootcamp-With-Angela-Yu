from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSdOhLBd_TmbtIKnfb3c3lZvKrRsgFUmkfWu1-Dthbr3O4YZaA/viewform?usp=sf_link'
property_link = "https://www.hepsiemlak.com/ankara-kiralik"

drive = webdriver.Chrome('C:\\Users\\061885\\Desktop\\Dayy49,Automating Job Applications on LinkedIn\\Development\\chromedriver.exe')
drive.get(property_link)
links = drive.find_elements(By.CLASS_NAME, 'list-view-content')
links_ = []
for i in links:
    links_.append(i.find_element(By.CSS_SELECTOR, 'a').get_attribute("href"))
prices = drive.find_elements(By.CLASS_NAME, 'list-view-price')
prices_ = []
prices__ = []
for i in prices:
    prices_.append(i.text.split("\n"))

address = drive.find_elements(By.CLASS_NAME, 'list-view-location')
address_ = []
for i in address:
    address_.append(i.text.split("\n"))

for i in prices_:
    prices__.append(i[0])

print(len(prices__))


drive.get(form_link)
time.sleep(5)
answer_address = drive.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
answer_address.send_keys(address_[0])
answer_price = drive.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
answer_price.send_keys(prices[0])
answer_link = drive.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
answer_link.send_keys(links_[0])
