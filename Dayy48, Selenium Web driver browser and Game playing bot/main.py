from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def checkConsole():
    selector = 0
    money = int(driver.find_element(By.ID, "money").text)

    cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b')
    cursor_price = int(cursor.text.split("-")[1])

    grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
    grandma_price = int(grandma.text.split("-")[1])

    factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b')
    factory_price = int(factory.text.split("-")[1])

    mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b')
    mine_price = int(mine.text.split("-")[1].replace(",",""))

    shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b')
    shipment_price = int(shipment.text.split("-")[1].replace(",",""))

    alchemy = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
    alchemy_price = int(alchemy.text.split("-")[1].replace(",",""))

    portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b')
    portal_price = int(portal.text.split("-")[1].replace(",",""))

    timeMachine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')
    timeMachine_price = int(timeMachine.text.split("-")[1].replace(",",""))

    prices = [cursor_price,grandma_price,factory_price,mine_price,shipment_price,
              alchemy_price,portal_price,timeMachine_price]

    for i in range(len(prices)-1, -1, -1):
        if money > prices[i]:
            selector = i
            break

    if selector == 0:
        cursor.click()
    elif selector == 1:
        grandma.click()
    elif selector == 2:
        factory.click()
    elif selector == 3:
        mine.click()
    elif selector == 4:
        shipment.click()
    elif selector == 5:
        alchemy.click()
    elif selector == 6:
        portal.click()
    elif selector == 7:
        timeMachine.click()


chrome_driver_path = "C:\\Users\\061885\\Desktop\\Dayy48, Selenium Web driver browser and Game playing bot\\Development\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

while 1:
    cookie.click()
    checkConsole()
    time.sleep(2)
