from selenium import webdriver
from selenium.webdriver.common.by import By
import time

## 상위 모듈 참조
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from global_module.driverSetting import DriverSetting

class LoginService:
    def __init__(self, driverSetting: DriverSetting):
        self.driver = driverSetting.driver

    def gotoLoginpage(self):
        self.driver.get('https://saint.ssu.ac.kr/irj/portal')
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.CSS_SELECTOR, "#s_btnLogin").click()
        self.driver.implicitly_wait(3)

    def enterId(self, userId: str):
        idBar = self.driver.find_element(By.CSS_SELECTOR, "#userid")
        idBar.click()
        idBar.send_keys(userId)
        self.driver.implicitly_wait(1.5)
    
    def enterPw(self, userPw: str):
        pwBar = self.driver.find_element(By.CSS_SELECTOR, "#pwd")
        pwBar.click()
        pwBar.send_keys(userPw)
        self.driver.implicitly_wait(1.5)

    def clickLoginBtn(self):
        enterButton = self.driver.find_element(By.CSS_SELECTOR, "#sLogin > div > div.area_login > form > div > div:nth-child(2) > a")
        enterButton.click()
        time.sleep(3)
