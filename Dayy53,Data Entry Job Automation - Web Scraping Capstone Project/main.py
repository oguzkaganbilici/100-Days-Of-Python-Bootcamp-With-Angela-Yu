from selenium import webdriver
from selenium.webdriver.common.by import By
import time

form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSdOhLBd_TmbtIKnfb3c3lZvKrRsgFUmkfWu1-Dthbr3O4YZaA/viewform?usp=sf_link'
property_link = "https://www.hepsiemlak.com/ankara-kiralik"

drive = webdriver.Chrome('chromedriver.exe')
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

drive.get(form_link)
time.sleep(3)

for i in range(0, 24):
    answer_address = drive.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer_address.send_keys(address_[i])

    answer_price = drive.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer_price.send_keys(prices__[i])

    answer_link = drive.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer_link.send_keys(links_[i])

    send_button = drive.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    send_button.click()
    time.sleep(2)
    send_another = drive.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_another.click()
    time.sleep(1)

drive.quit()
