from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# 유저 생성 요청 스키마
class UserCreate(BaseModel):
    username: str
    password: str
    age: Optional[int] = None
    gender: Optional[str] = None
    job: Optional[str] = None

# 유저 응답 스키마
class User(BaseModel):
    id: int
    username: str
    age: Optional[int]
    gender: Optional[str]
    job: Optional[str]

    class Config:
        orm_mode = True

# 투표 생성 요청 스키마
class VoteCreate(BaseModel):
    question: str

# 투표 응답 스키마
class Vote(BaseModel):
    id: int
    question: str
    created_at: datetime

    class Config:
        orm_mode = True

# 유저 투표 요청 스키마
class UserVoteCreate(BaseModel):
    vote_id: int
    choice: bool  # True = 찬성, False = 반대

# 댓글 생성 요청 스키마
class CommentCreate(BaseModel):
    vote_id: int
    user_id: int
    content: str
    parent_id: Optional[int] = None
