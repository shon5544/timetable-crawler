from .domain.loginService import LoginService

## 상위 모듈 참조
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from global_module.driverSetting import DriverSetting

class Crawler:
    def __init__(self, driverSetting: DriverSetting) -> None:
        self.driver = driverSetting.driver
    
        self.loginService = LoginService(driverSetting)
    
    def takeScreenShotForTest(self, filename: str) -> None:
        self.driver.save_screenshot(filename)

    def login(self, userId: str, userPw: str) -> None:
        self.loginService.gotoLoginpage()

        print(f"login 진입: {userId}")

        self.loginService.enterId(userId)
        self.loginService.enterPw(userPw)

        self.loginService.clickLoginBtn()

        self.takeScreenShotForTest("screenshot.png")

        print("스크린샷 완료.")

    
    def quit(self) -> None:
        self.driver.quit()