from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.nba.com/stats"
driver = webdriver.Chrome("C:\\Users\\061885\\Desktop\\Dayy92, Professional Portfolio Project - Web Scraping - NBA players stats\\chromdriver.exe")
driver.get(URL)

all_divs = driver.find_elements(By.CLASS_NAME,"LeaderBoardCard_lbcWrapper__e4bCZ")

with open("all_player_datas.txt", "w") as f:
    for ii in range(0, 8):
        f.writelines(all_divs[ii].text + "\n")

