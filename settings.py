from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

path = 'postgresql://postgres:password@localhost:5432/postgres'
# path = 'mysql+pymysql://root:@127.0.0.1:3306/alembic_sample'

# Engine の作成
Engine = create_engine(
    path,
    encoding="utf-8",
    echo=False
)
Base = declarative_base()
