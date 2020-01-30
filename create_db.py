from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String, Integer, DateTime, create_engine

Base = declarative_base()


def create_database():
    engine = create_engine('mysql://root:*******@localhost')
    engine.execute("CREATE DATABASE exp_db")


class Expenses(Base):
    __tablename__ = "Expenses"
    id = Column(Integer, primary_key=True, name="id")
    price = Column(Float, name="price")
    date = Column(DateTime, name="date")
    name = Column(String(50), name="name")
    category = Column(String(50), name="category")

    def __repr__(self):
        return f"<Expenses(price={self.price}, date={self.date}, name={self.name}, category={self.category})>"


def get_engine():
    engine = create_engine(
        "mysql+pymysql://root:*******@localhost/exp_db"
    )
    return engine


def create_table():
    engine = create_engine(
        "mysql+pymysql://root:*******@localhost/exp_db")
    Base.metadata.create_all(engine)
