from app.backend.db import Base, engine
from app.models import User, Task
from sqlalchemy.schema import CreateTable

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Печать SQL для каждой модели
print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))
