from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
url = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101165590&keywords=Python%20Developer&location=Birle%C5%9Fik%20Krall%C4%B1k"
driver = webdriver.Chrome("C:\\Users\\061885\\Desktop\\Dayy49,Automating Job Applications on LinkedIn\Development\\chromedriver.exe")
driver.get(url)
login_button = driver.find_element(By.CLASS_NAME,'nav__button-secondary')
login_button.click()
time.sleep(3)
username = driver.find_element(By.ID, "username")
username.send_keys("oguzkaganbilici1@gmail.com")
password = driver.find_element(By.ID,"password")
password.send_keys("experasus1")

login_button2 = driver.find_element(By.CLASS_NAME, "btn__primary--large")
login_button2.click()
time.sleep(10)

jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for i in jobs:
    i.click()
    time.sleep(5)
    try:
        apply_button = driver.find_element(By.CLASS_NAME, 'jobs-s-apply')
        if apply_button:
            apply_button.click()
            next_button = driver.find_element(By.CSS_SELECTOR,"button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
            while next_button:
                next_button.click()



"""

while next_button:
    next_button.click()
"""