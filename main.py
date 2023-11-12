from fastapi import FastAPI
from crawler.crawler import Crawler
from dto.loginRequestDto import LoginRequestDto
from global_module.driverSetting import DriverSetting

app = FastAPI()
driverSetting = DriverSetting()
crawler = Crawler(driverSetting)

@app.get("/login")
def login(loginRequestDto: LoginRequestDto):
    userId = loginRequestDto.userId
    userPw = loginRequestDto.userPw

    crawler.login(userId, userPw)
    crawler.quit()
