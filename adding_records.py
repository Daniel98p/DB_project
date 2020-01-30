from sqlalchemy.orm import sessionmaker
from create_db import get_engine, Expenses
from datetime import datetime


def get_name():
    name = input("Enter the name of product: ")
    return name


def get_category():
    category = input("Enter the category of purchased product: ")
    return category


def get_price():
    price = int(input("Enter the price od purchased product: "))
    return price


def add_record():
    name = get_name()
    category = get_category()
    price = get_price()

    Session = sessionmaker()

    engine = get_engine()
    session = Session(bind=engine)

    new_object = Expenses(name=name, category=category, price=price, date=datetime.now())

    session.add(new_object)
    session.commit()
    print(session.query(Expenses).all())
    session.close()


if __name__ == '__main__':
    add_record()
