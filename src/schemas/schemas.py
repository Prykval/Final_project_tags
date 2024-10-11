from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class TagModel(BaseModel):
    name: str = Field(max_length=25)


class TagResponse(TagModel):
    id: int

    class Config:
        orm_mode = True


class NoteBase(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=150)


class NoteModel(NoteBase):
    tags: List[int]


class NoteUpdate(NoteModel):
    done: bool


class NoteStatusUpdate(BaseModel):
    done: bool


class NoteResponse(NoteBase):
    id: int
    created_at: datetime
    tags: List[TagResponse]

    class Config:
        orm_mode = True

class ImageResponce(BaseModel):
    id: int
    description: str
    image_url: str
    author_id: int
    qr_code_url: str
    created_dt: datetime


class CropImageRequest(BaseModel):
    image_id: int
    width: int
    height: int
    description: str


class RoundCornersImageRequest(BaseModel):
    image_id: int
    radius: int
    description: str


class EffectImageRequest(BaseModel):
    image_id: int
    description: str