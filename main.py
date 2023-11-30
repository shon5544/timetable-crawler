from fastapi import FastAPI
from crawler.crawler import Crawler
from dto.loginRequestDto import LoginRequestDto
from global_module.driverSetting import DriverSetting

app = FastAPI()


# 테스트 용 api
@app.get("/login")
def login(loginRequestDto: LoginRequestDto):
    driverSetting = DriverSetting()
    crawler = Crawler(driverSetting)

    userId = loginRequestDto.userId
    userPw = loginRequestDto.userPw

    print(userId, userPw)

    crawler.login(userId, userPw)
    crawler.quit()

    return {
        "isSuccess": True
    }
