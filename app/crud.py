from sqlalchemy.orm import Session
from models import User, Vote, UserVote, Comment
from schemas import UserCreate, VoteCreate, CommentCreate

# 유저 생성
def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, password=user.password, age=user.age, gender=user.gender, job=user.job)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 특정 유저 조회
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# 전체 투표 조회
def get_votes(db: Session):
    return db.query(Vote).all()

# 새로운 투표 생성
def create_vote(db: Session, vote: VoteCreate):
    db_vote = Vote(question=vote.question)
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote

# 유저가 투표하기
def user_vote(db: Session, user_id: int, vote_id: int, choice: bool):
    db_vote = UserVote(user_id=user_id, vote_id=vote_id, choice=choice)
    db.add(db_vote)
    db.commit()
    return db_vote

# 댓글 생성
def create_comment(db: Session, comment: CommentCreate):
    db_comment = Comment(vote_id=comment.vote_id, user_id=comment.user_id, content=comment.content, parent_id=comment.parent_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
