from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 密码处理（如果包含特殊字符）
password = "hcol@2025"  # 请确认实际密码
encoded_password = quote_plus(password)

# 连接配置
DATABASE_URL = f"postgresql://postgres:{encoded_password}@124.71.81.247:5433/postgres"
# 或从环境变量读取
# DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    connect_args={"connect_timeout": 5},  # 添加连接超时
    pool_pre_ping=True  # 建议添加连接健康检查
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
