from ty.PyObjectId import PyObjectId
from ty.Mood import Mood
from ty.Weather import Weather
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

class Diary(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    userId: PyObjectId = Field(...)
    created: datetime = Field(default_factory=datetime.utcnow)
    updated: datetime = Field(default_factory=datetime.utcnow)
    title: Optional[str] = Field(None)
    content: Optional[str] = Field(None)
    mood: Mood = Field(...)
    weather: Weather = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": "1",
                "userId": "62662bb2edc28d6e8624e858",
                "dateTime": "153456786",
                "title": "오늘의 일기",
                "content": "오늘 너무너무 재미있었다.",
                "mood": "sad",
                "weather": "sun",
            }
        }