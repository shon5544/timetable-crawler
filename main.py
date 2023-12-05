from fastapi import FastAPI
from crawler.crawler import Crawler
from global_module.driverSetting import DriverSetting

app = FastAPI()

@app.get("/crawling/{userId}/{userPw}")
def crawling(userId: str, userPw: str):
    driverSetting = DriverSetting()
    crawler = Crawler(driverSetting)

    crawler.login(userId, userPw)
    result = crawler.crawlingTimeTable()
    crawler.quit()

    return {
        "isSuccess": True,
        "result": result
    }
