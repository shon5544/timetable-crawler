from dataclasses import dataclass

@dataclass
class CrawlingRequestDto:
    userId: str
    userPw: str