from selenium import webdriver
from selenium.webdriver.common.by import By
import time

twitter_email = "okbkagan@gmail.com"
twitter_pass = "experbilici1"
promised_down = 80
promised_up = 10

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Users\\061885\\Desktop\\Dayy50, Tinder Swipping Bot\\Development\\chromedriver.exe")
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go_button = self.driver.find_element(By.CLASS_NAME, 'start-text')
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.down, '--', self.up)

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/home')
        time.sleep(10)
        email_ = self.driver.find_element(By.NAME, 'text')
        email_.send_keys('okbkagan@gmail.com')
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(2)
        pass_ = self.driver.find_element(By.NAME, 'password')
        pass_.send_keys('experbilici1')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_button.click()
        time.sleep(5)
        tweet = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        tweet.send_keys(f'Download:{self.down}, Upload:{self.up}, i need get Download:{promised_down}, Upload:{promised_up}')
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()
        self.driver.quit()


a = InternetSpeedTwitterBot()
a.get_internet_speed()
print("we get internet")
a.tweet_at_provider()