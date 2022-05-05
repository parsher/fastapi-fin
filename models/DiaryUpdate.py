from ty.Mood import Mood
from ty.Weather import Weather
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from bson import ObjectId

class DiaryUpdate(BaseModel):
    updated: datetime = Field(default_factory=datetime.utcnow)
    title: Optional[str] = Field(None)
    content: Optional[str] = Field(None)
    mood: Optional[Mood] = Field(None)
    weather: Optional[Weather] = Field(None)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "오늘의 일기",
                "content": "오늘 너무너무 재미있었다.",
                "mood": "sad",
                "weather": "sun",
            }
        }