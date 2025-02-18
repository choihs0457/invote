from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database import Base

# 유저 테이블
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    job = Column(String, nullable=True)

    votes = relationship("UserVote", back_populates="user")
    comments = relationship("Comment", back_populates="user")

# 투표 테이블
class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    user_votes = relationship("UserVote", back_populates="vote")
    comments = relationship("Comment", back_populates="vote")

# 유저 투표 기록 테이블
class UserVote(Base):
    __tablename__ = "user_votes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    vote_id = Column(Integer, ForeignKey("votes.id"))
    choice = Column(Boolean, nullable=False)

    user = relationship("User", back_populates="votes")
    vote = relationship("Vote", back_populates="user_votes")

# 댓글 테이블 (대댓글 지원)
class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    vote_id = Column(Integer, ForeignKey("votes.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    parent_id = Column(Integer, ForeignKey("comments.id"), nullable=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    vote = relationship("Vote", back_populates="comments")
    user = relationship("User", back_populates="comments")
    replies = relationship("Comment", remote_side=[id], backref="parent")
