from fastapi import FastAPI
from crawler.crawler import Crawler
from dto.crawlingRequestDto import CrawlingRequestDto
from global_module.driverSetting import DriverSetting

app = FastAPI()


# 테스트 용 api
@app.get("/crawling")
def crawling(crawlingRequestDto: CrawlingRequestDto):
    driverSetting = DriverSetting()
    crawler = Crawler(driverSetting)

    userId = crawlingRequestDto.userId
    userPw = crawlingRequestDto.userPw

    print(userId, userPw)

    crawler.login(userId, userPw)
    crawler.quit()

    return {
        "isSuccess": True
    }
