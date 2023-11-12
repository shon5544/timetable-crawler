from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

class DriverSetting:
    def __init__(self):
        self.options = ChromeOptions()

        # headless 옵션 설정
        self.options.add_argument('headless')
        self.options.add_argument('no-sandbox')

        # 브라우저 윈도우 사이즈
        self.options.add_argument('window-size=1920x1080')

        # 사람처럼 보이게 하는 옵션들
        self.options.add_argument('disable-gpu')   # 가속 사용 x
        self.options.add_argument('lang=ko_KR')    # 가짜 플러그인 탑재
        self.options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

        # ChromeService 설정
        self.service = ChromeService(executable_path='./chromedriver/chromedriver.exe')

        # 드라이버 위치 경로 입력
        self.driver = webdriver.Chrome(service=self.service, options=self.options)