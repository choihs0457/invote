import os
from dotenv import load_dotenv
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context

# .env 파일 로드
load_dotenv()

# .env에서 DATABASE_URL 가져오기
DATABASE_URL = os.getenv("DATABASE_URL")

# Alembic Config 객체 가져오기
config = context.config

# 기존 ini 파일에서 불러오는 방식 대신 .env에서 직접 DATABASE_URL을 가져와 설정
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# 로깅 설정
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# SQLAlchemy 모델의 MetaData 가져오기
from models import Base
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Offline 모드에서 마이그레이션 실행 (DB 연결 없이 SQL 생성)"""
    context.configure(
        url=DATABASE_URL,  # .env에서 불러온 URL 사용
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Online 모드에서 마이그레이션 실행 (DB에 직접 적용)"""
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Offline/Online 모드 감지 후 실행
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
