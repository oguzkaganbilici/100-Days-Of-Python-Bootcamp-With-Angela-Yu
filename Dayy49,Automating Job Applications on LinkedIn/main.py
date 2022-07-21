from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
url = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101165590&keywords=C%2B%2B%20Developer&location=Birle%C5%9Fik%20Krall%C4%B1k"
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
    print("basvuru secildi")
    time.sleep(3)
    try:
        apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
        apply_button.click()
        print("basvur tiklandi")
        time.sleep(1)
        next_flag = True
        while next_flag:
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, "button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
                print("next bulundu")
                next_button.click()
                time.sleep(1)
                try:
                    radio_error = driver.find_element(By.CLASS_NAME, "fb-radio")
                    close = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
                    close.click()
                    time.sleep(1)
                    dont_save = driver.find_element(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")
                    dont_save.click()
                    time.sleep(1)
                except:
                    try:
                        select_error = driver.find_element(By.CLASS_NAME, "fb-dropdown")
                        close = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                        close.click()
                        time.sleep(1)
                        dont_save = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
                        dont_save.click()
                        time.sleep(1)
                    except:
                        pass
            except:
                print("next bulunamadı")
                next_flag = False

    except NoSuchElementException:
        pass


""" 


        while flag:
            print("next buton bulundu")
            time.sleep(2)
            if next_button:
                next_button.click()
            else:
                flag = False
    else:
        i.click()
        time.sleep(3)



print("basvuruya tıkladı")
        time.sleep(5)
        try:
            
            
            
            while next_button:
                next_button.click()
                print("next butonuna tikladi")
                errors = driver.find_element(By.CLASS_NAME, "fb-radio-buttons")
"""