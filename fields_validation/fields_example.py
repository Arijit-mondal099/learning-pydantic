from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Optional

class User(BaseModel):
    id: int
    full_name: str = Field(..., min_length=3, max_length=16, description="User name", examples=["jhon doe"])
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=16)
    avater: Optional[str] = None
    posts: List[int]
    address: Dict[str, str]

user_input = {
    "id": 1,
    "full_name": "arijit mondal",
    "email": "arijitm717@gmail.com",
    "password": "12345678",
    "posts": [1, 2, 3, 4],
    "address": {
        "dist": "murshidabad",
        "ps": "beldanga",
        "vill+po": "madda",
        "pin": "742133",
    }
}

user_1 = User(**user_input)
