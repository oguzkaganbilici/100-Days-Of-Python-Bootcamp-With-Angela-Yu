from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


target = "instagram"
username_ = "####"
pass_ = "######"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(
            "C:\\Users\\061885\\Desktop\\Dayy50, Tinder Swipping Bot\\Development\\chromedriver.exe")

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(username_)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(pass_)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{target}/")
        time.sleep(10)
        f_list = self.driver.find_elements(By.CLASS_NAME, '_ac2a')
        f_list[1].click()

    def follow(self):
        time.sleep(5)
        button_list = self.driver.find_elements(By.CLASS_NAME, '_acan._acap._acas')
        print("following list len: ", len(button_list))
        if len(button_list) == 0:
            print("following list len: ", len(button_list))
            pop_up_window = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "_aano")))
            #self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', pop_up_window)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', pop_up_window)
            time.sleep(1)
        for i in button_list:
            try:
                print("following...")
                self.driver.execute_script("arguments[0].click();", i)
            except:
                pass


xx = InstaFollower()
xx.login()
time.sleep(10)
xx.find_followers()
while(1):
    xx.follow()