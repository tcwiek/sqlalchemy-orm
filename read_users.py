# from models import Session, User
#
#
# def main():
#     session = Session()
#     query = session.query(User)
#     for row in query.all():
#         print(row)
#
#
# if __name__ == '__main__':
#     main()

# limit wyswietlen ilosci wersow
# from models import Session, User
#
#
# def main():
#     session = Session()
#     query = session.query(User).limit(5).offset(1)
#
#
# if __name__ == '__main__':
#     main()

# wybor kilku rekordow z najwieksazymi zarobkami
from models import Session, User


def main():
    session = Session()
    query = session.query(User).order_by(User.salary.desc())


if __name__ == '__main__':
    main()
    