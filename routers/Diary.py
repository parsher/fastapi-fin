from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Body, HTTPException, status
from models.DiaryUpdate import DiaryUpdate
from models.Diary import Diary
from typing import List
from db import db


router = APIRouter(prefix='/diary')


@router.post("/", response_description="Add new diary", response_model=Diary)
async def create_diary(diary: Diary = Body(...)):
    diary = jsonable_encoder(diary)
    new_diary = await db["diaries"].insert_one(diary)
    created_diary = await db["diaries"].find_one({"_id": new_diary.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_diary)


@router.get(
    "/", response_description="List all diaries", response_model=List[Diary]
)
async def list_diaries():
    diaries = await db["diaries"].find().to_list(1000)
    return diaries


@router.get(
    "/{id}", response_description="Get a single diary", response_model=Diary
)
async def show_diary(id: str):
    if (diary := await db["diaries"].find_one({"_id": id})) is not None:
        return diary

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"diary {id} not found")


@router.put("/{id}", response_description="Update a diary", response_model=Diary)
async def update_diary(id: str, diary: DiaryUpdate = Body(...)):
    diary = {k: v for k, v in diary.dict().items() if v is not None}

    if len(diary) >= 1:
        update_result = await db["diaries"].update_one({"_id": id}, {"$set": diary})

        if update_result.modified_count == 1:
            if (
                updated_diary := await db["diaries"].find_one({"_id": id})
            ) is not None:
                return updated_diary

    if (existing_diary := await db["diaries"].find_one({"_id": id})) is not None:
        return existing_diary

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"diary {id} not found")


@router.delete("/{id}", response_description="Delete a diary")
async def delete_diary(id: str):
    delete_result = await db["diaries"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"diary {id} not found")

