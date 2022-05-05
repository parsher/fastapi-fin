from ty.PyObjectId import PyObjectId
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List
from models.Diary import Diary

from bson import ObjectId

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    avatar: Optional[HttpUrl] = Field(None)
    diaryList: Optional[List[Diary]] = Field([])

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": "1",
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