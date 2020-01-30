from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String, Integer, DateTime, create_engine

Base = declarative_base()


class Expenses(Base):
    __tablename__ = "Expenses"
    id = Column(Integer, primary_key=True, name="id")
    price = Column(Float, name="price")
    date = Column(DateTime, name="date")
    name = Column(String, name="name")
    category = Column(String, name="category")


if __name__ == '__main__':
    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)