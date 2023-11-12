from selenium import webdriver
from selenium.webdriver.common.by import By
from domain.loginService import LoginService

## 상위 모듈 참조
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from globalModule.driverSetting import DriverSetting

import time

class Crawler:
    def __init__(self, driverSetting: DriverSetting) -> None:
        self.driver = driverSetting.driver
    
        self.loginService = LoginService(self.driver)
    
    def takeScreenShotForTest(self, filename: str) -> None:
        self.driver.save_screenshot(filename)

    def login(self, userId: str, userPw: str) -> None:
        self.loginService.gotoLoginpage()

        self.loginService.enterId(userId)
        self.loginService.enterPw(userPw)

        self.loginService.clickLoginBtn()

        self.takeScreenShotForTest("screenshot.png")

    
    def quit(self) -> None:
        self.driver.quit()
    

crawler = Crawler()

userId, userPw = map(str, input().split())

crawler.login(userId, userPw)

crawler.quit()