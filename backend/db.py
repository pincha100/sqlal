from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Настройка базы данных
DATABASE_URL = "sqlite:///taskmanager.db"

# Создание движка
engine = create_engine(DATABASE_URL, echo=True)

# Локальная сессия
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
class Base(DeclarativeBase):
    pass
