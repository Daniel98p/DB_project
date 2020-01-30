from sqlalchemy.orm import sessionmaker
from create_db import create_table


def get_name():
    name = input("Enter the name of product: ")
    return name


def get_category():
    category = input("Enter the category of purchased product: ")
    return category


def get_price():
    price = int(input("Enter the price od purchased product: "))
    return price



