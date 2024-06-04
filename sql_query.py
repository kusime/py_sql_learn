# DB config
import time
from decouple import config

# CONNECT
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

# the base level of sqlalchemy
from contextlib import contextmanager
from models import Address, User

POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
APP_DATABASE = config("APP_DATABASE")
DB_HOST = "localhost:6666"

# db_url = f"postgresql://postgres:{POSTGRES_PASSWORD}@{DB_HOST}/{APP_DATABASE}"
db_url = f"mysql+pymysql://admin:admin123#@localhost:3306/local_loyaltyprogram?charset=utf8mb4"


# 1. commit() ?
# 2.

print(db_url)
engine = create_engine(db_url)
Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# @contextmanager
# def get_db() -> Iterator[Session]:
#     # https://stackoverflow.com/questions/49733699/python-type-hints-and-context-managers
#     try:
#         db = session()
#         yield db
#     finally:
#         db.close()


# Base.metadata.create_all(engine)
# CREATE = True
# if CREATE:
#     with Session.begin() as session:
#         # create Atom operation
#         spongebob = User(
#             name="spongebob",
#             fullname="Sponge",
#             addresses=[Address(email_address="spongebob@")],
#         )
#         sandy = User(
#             name="sandy",
#             fullname="Sandy Cheeks",
#             addresses=[
#                 Address(email_address="sandy@sqlal"),
#                 Address(email_address="sandy@squirre"),
#             ],
#         )
#         patrick = User(name="patrick", fullname="Patrick Star")
#         session.add_all([spongebob, sandy, patrick])
# any exception before commnit will rollback the session
# session.commit()


# raw
# begin will automatically create a new connection
# from sqlalchemy.sql import text

# with Session() as session:
#     result = session.execute(text("SHOW TRANSACTION ISOLATION LEVEL;"))
#     for row in result:
#         print(row[0])

# from models import Address, User
# from sqlalchemy.sql.expression import func
# import pandas as pd

# # write
# with Session() as session:
#     # query for ``User`` objects
#     stmt = select(User.name, User.fullname).order_by(func.random()).limit(10)

#     res = pd.read_sql(stmt, session.bind)
#     res.to_csv("users.csv", index=False)

# read
# with Session() as session:
#     # https://stackoverflow.com/questions/70422598/obtain-list-of-ids-inserted-from-pandas-to-sql-function
#     # query for ``User`` objects
#     content = pd.read_csv("users.csv")
#     table_name = "user_account"

#     # auto commnit here
#     ret = content.to_sql(table_name, session.bind, if_exists="append", index=False)
#     # https://github.com/pandas-dev/pandas/issues/23998
#     print(ret)
