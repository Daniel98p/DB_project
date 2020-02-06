from adding_records import add_record
from query import query


class WrongValueException(Exception):
    def __repr__(self):
        return "Value must be 1 or 2"


def menu():
    try:
        choice = int(input("Please select 1-add record or 2-show record/s: "))
        if choice == 1:
            add_record()
        if choice == 2:
            query()
        else:
            raise WrongValueException()
    except ValueError:
        print("It must be 1 or 2")


if __name__ == '__main__':
    menu()
