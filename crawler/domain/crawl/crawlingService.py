from selenium.webdriver.common.by import By
import time

## 상위 모듈 참조
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))).replace("\crawler", ""))

from global_module.driverSetting import DriverSetting

class CrawlingService:
    def __init__(self, driverSetting: DriverSetting):
        self.driver = driverSetting.driver

    def moveToTimeTablePage(self):
        academicManagementBtn = self.driver.find_element(By.CSS_SELECTOR, "#ddba4fb5fbc996006194d3c0c0aea5c4 > a")
        academicManagementBtn.click()
        self.driver.implicitly_wait(5)

        enrolmentBtn = self.driver.find_element(By.XPATH, '//*[@id="12cda160608ccd7b32af0ad5c6e5752c"]/a')
        enrolmentBtn.click()
        self.driver.implicitly_wait(5)

        print("good")


        personalTimeTableBtn = self.driver.find_element(By.XPATH, '//*[@id="1724938fdd5d98311a8647b31efd21fe"]/a')
        personalTimeTableBtn.click()
        self.driver.implicitly_wait(5)

        time.sleep(3)

        frameBorder = self.driver.find_element(By.XPATH, '//*[@id="contentAreaFrame"]')
        self.driver.switch_to.frame(frameBorder)

        frame = self.driver.find_element(By.XPATH, '//*[@id="isolatedWorkArea"]')
        self.driver.switch_to.frame(frame)

        semesterLBtn = self.driver.find_element(By.CSS_SELECTOR, "#WDA7")
        semesterLBtn.click()

        time.sleep(2)

        self.driver.save_screenshot("screenshot.png")

    def crawlTimeTable(self):
        monday = ["WDE5", "WDF4", "WD0103", "WD0112", "WD0121", "WD0130", "WD013F", "WD014E", "WD015D", "WD016C"]
        tuesday = ["WDE7", "WDF6", "WD0105", "WD0114", "WD0123", "WD0132", "WD0141", "WD0150", "WD015F", "WD016E"]
        wednesday = ["WDE9", "WDF8", "WD0107", "WD0115", "WD0125", "WD0134", "WD0143", "WD0152", "WD0161", "WD0170"]
        thursday = ["WDEB", "WDFA", "WD0109", "WD0118", "WD0127", "WD0136", "WD0145", "WD0153", "WD0163", "WD0172"]
        friday = ["WDED", "WDFC", "WD010B", "WD011A", "WD0129", "WD0138", "WD0147", "WD0156", "WD0165", "WD0174"]
        saturday = ["WDEF", "WDFE", "WD010D", "WD011C", "WD012B", "WD013A", "WD0149", "WD0158", "WD0167", "WD0176"]

        monValue = []
        tueValue = []
        wedValue = []
        thuValue = []
        friValue = []
        satValue = []
        
        self.getTimeTable(monday, monValue)
        self.getTimeTable(tuesday, tueValue)
        self.getTimeTable(wednesday, wedValue)
        self.getTimeTable(thursday, thuValue)
        self.getTimeTable(friday, friValue)
        self.getTimeTable(saturday, satValue)

        print(monValue)
        print()
        print(tueValue)
        print()
        print(wedValue)
        print()
        print(thuValue)
        print()
        print(friValue)
        print()
        print(satValue)
        print()

        response = {
            "monday": monValue,
            "tuesday": tueValue,
            "wednesday": wedValue,
            "thusday": thuValue,
            "friday": friValue,
            "saturday": satValue
        }

        return response

    def getTimeTable(self, dayList, dayValue):
        for i in dayList:
            myTime = self.driver.find_element(By.XPATH, f'//*[@id="{i}"]')
            text = myTime.text
            dayValue.append(text)
            if len(text) > 1:
                print(text)
            else:
                print("null")
            print()
