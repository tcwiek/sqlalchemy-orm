# # from models import Session, User
# #
# #
# # def main():
# #     session = Session()
# #     query = session.query(User).filter_by(first_name="John")
# #     for user in query:
# #         print(user.first_name, user.last_name, user.email)
# #
# #
# # if __name__ == '__main__':
# #     main()
#
#
# # imiona od J
# # from models import Session, User
# #
# #
# # def main():
# #     session = Session()
# #     query = session.query(User).filter(User.first_name.like("J%"))
# #     for user in query:
# #         print(user.first_name, user.last_name, user.email)
# #
# #
# # if __name__ == '__main__':
# #     main()
#
#
# # przedzial zarobkow
# # from models import Session, User
# #
# #
# # def main():
# #     session = Session()
# #     query = session.query(User).filter(User.salary.between(5000, 6000))
# #     for user in query:
# #         print(user.first_name, user.last_name, user.email)
# #
# #
# # if __name__ == '__main__':
# #     main()
#
# from models import Session, User
# from sqlalchemy import and_, or_
#
#
# def main():
#     session = Session()
#     query = session.query(User).filter(
#         and_(
#             User.salary > 5000,
#             User.salary < 6000
#         )
#     )
#     for user in query:
#         print(user.first_name, user.last_name, user.email)
#
#
# if __name__ == '__main__':
#     main()
#
#
# from models import Session, User
#
#
# def main():
#     session = Session()
#     query = session.query(User).filter(
#         User.salary.between(5000, 6000)
#     ).order_by(User.salary.desc())
#     for user in query.limit(3):
#         print(user.first_name, user.last_name, user.email)
#
#     print('------------------')
#     # one, scalar, first, get
#     result = session.query(User).filter(
#         User.salary > 5_000_000
#     ).scalar()
#     print(result)
#
#     print('------------------')
#     # all
#     result = session.query(User).filter(
#         User.first_name.like("A%")
#     ).all()
#     print(result)
#
#     print('------------------')
#     query = session.query(
#         User.id, User.email, User.creation_date
#     )
#     for row in query:
#         print(row.id, row.email, row.creation_date)
#
#
# if __name__ == '__main__':
#     main()

from sqlalchemy import and_
from models import Session, User


def main():
    session = Session()
    query = session.query(User).filter(
        User.salary.between(5000, 6000)
    ).order_by(User.salary.desc())
    for user in query.limit(3):
        print(user.first_name, user.last_name, user.email)

    print('------------------')
    # one, scalar, first, get
    result = session.query(User).filter(
        User.salary > 5_000_000
    ).scalar()
    print(result)

    print('------------------')
    # all
    result = session.query(User).filter(
        User.first_name.like("A%")
    ).all()
    print(result)

    print('------------------')
    query = session.query(
        User.id, User.email, User.creation_date
    ).filter(
        and_(
            User.salary.between(5000, 6000),
            User.first_name.like("J%")
        )
    ).order_by(
        User.salary.desc(),
        User.creation_date.asc()
    )
    for row in query:
        print(row.id, row.email, row.creation_date)


if __name__ == '__main__':
    main()
