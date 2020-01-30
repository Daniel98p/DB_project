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

    def __repr__(self):
        return f"<Expenses(price={self.price}, date={self.date}, name={self.name}, category={self.category})>"


def create_table():
    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)
