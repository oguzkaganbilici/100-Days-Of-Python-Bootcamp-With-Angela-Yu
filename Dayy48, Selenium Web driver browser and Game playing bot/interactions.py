from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
"""chrome_driver_path = "C:\\Users\\061885\\Desktop\\Development\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
#articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
articles = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
print(articles.text)
articles.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Oğuz Kağan")
search.send_keys(Keys.ENTER)"""

chrome_driver_path = "C:\\Users\\061885\\Desktop\\Development\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.NAME,"fName")
name.send_keys("Oghuz Khan")
surname = driver.find_element(By.NAME,"lName")
surname.send_keys("Bilici")
e_mail = driver.find_element(By.NAME,"email")
e_mail.send_keys("delykurt@gmail.com")
button = driver.find_element(By.CSS_SELECTOR, "form button")
button.send_keys(Keys.ENTER)


"""
chrome_driver_path = "C:\\Users\\061885\\Desktop\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
"""
driver.get('https://www.amazon.com.tr/Keycaps-Tu%C5%9Flar%C4%B1-Profil-Mekanik-Klavyesi/dp/B0989P4RSJ/ref=sr_1_33?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=18CFBU7TWH9AP&keywords=rk61&qid=1658053544&sprefix=rk61%2Caps%2C189&sr=8-33') #to opens browser
#price = driver.find_element(By.CLASS_NAME, "a-price-whole")
#price = driver.find_element(By.ID,"corePriceDisplay_desktop_feature_div")
#price = driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]')
print(price.text)
"""
last_news = {

}

driver.get("https://www.python.org/")
for i in range(1,5):
    menu = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]')
    xx = menu.text.split("\n")
    last_news[i-1]={"date":xx[0], "name":xx[1]}

print(last_news)
driver.quit() #to close all pages
#driver.close()

"""