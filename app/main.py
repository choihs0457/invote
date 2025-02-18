from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, models, schemas

app = FastAPI()

# DB 세션 가져오기
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 유저 생성 API
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# 특정 유저 조회 API
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

# 전체 투표 조회 API
@app.get("/votes/", response_model=list[schemas.Vote])
def read_votes(db: Session = Depends(get_db)):
    return crud.get_votes(db)

# 새로운 투표 생성 API
@app.post("/votes/", response_model=schemas.Vote)
def create_vote(vote: schemas.VoteCreate, db: Session = Depends(get_db)):
    return crud.create_vote(db, vote)

# 유저가 투표하기
@app.post("/votes/{vote_id}/vote/")
def user_vote(vote_id: int, user_id: int, choice: bool, db: Session = Depends(get_db)):
    return crud.user_vote(db, user_id, vote_id, choice)

# 댓글 작성 API
@app.post("/comments/", response_model=schemas.CommentCreate)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db, comment)
