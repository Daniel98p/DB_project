from sqlalchemy.orm import sessionmaker
from create_db import get_engine, Expenses
from datetime import datetime


def get_year():
    year = int(input("Enter a year: "))
    return year


def get_month():
    month = int(input("Enter a month: "))
    return month


def get_day():
    day = int(input("Enter a day: "))
    return day


def query():
    from_year = get_year()
    from_month = get_month()
    from_day = get_day()

    to_year = get_year()
    to_month = get_month()
    to_day = get_day()

    from_date = datetime(from_year, from_month, from_day)
    to_date = datetime(to_year, to_month, to_day)

    Session = sessionmaker()

    engine = get_engine()
    session = Session(bind=engine)

    for some_object in session.query(Expenses).filter(
            Expenses.date > from_date).filter(Expenses.date < to_date):
        print(some_object.name, some_object.price)

    session.close()


if __name__ == '__main__':
    query()
