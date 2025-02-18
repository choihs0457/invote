from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# AWS RDS PostgreSQL 연결 정보
DATABASE_URL = "postgresql://invote:@invote-db.cje0mqkkmgel.ap-northeast-2.rds.amazonaws.com:5432/postgres"

# SQLAlchemy 엔진 및 세션 설정
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
