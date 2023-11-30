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

    userId: str = crawlingRequestDto.userId
    userPw: str = crawlingRequestDto.userPw

    print(userId, userPw)

    crawler.login(userId, userPw)
    result = crawler.crawlingTimeTable()
    crawler.quit()

    return {
        "isSuccess": True,
        "result": result
    }
