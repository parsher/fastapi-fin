
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List
from models.Diary import Diary
from bson import ObjectId

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None)
    avatar: Optional[HttpUrl] = Field(None)
    diaryList: Optional[List[Diary]] = Field(None)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "avatar": "http://www.naver.com",
                "diaryList": [{
                    "_id": "1",
                    "dateTime": "153456786",
                    "title": "오늘의 일기",
                    "content": "오늘 너무너무 재미있었다.",
                    "mood": "sad",
                    "weather": "sun",
                }]
            }
        }