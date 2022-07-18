from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Users\\061885\\Desktop\\Development\\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

clicked_cookie = driver.find_element(By.ID, "cookie")
cursor = driver.find_element(By.ID,"buyCursor").text.split("-")[1]

while(1):
    clicked_cookie.click()
    print(cursor.text)