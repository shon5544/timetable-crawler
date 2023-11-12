from dataclasses import dataclass

@dataclass
class LoginRequestDto:
    userId: str
    userPw: str