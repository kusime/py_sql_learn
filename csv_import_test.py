# CONNECT

import pymysql
from sqlalchemy import create_engine, select
import sqlalchemy
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker

# the base level of sqlalchemy
db_url = f"mysql+pymysql://admin:admin123#@localhost:3306/local_loyaltyprogram?charset=utf8mb4&local_infile=1"
engine = create_engine(db_url, echo=False)

Session = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)

with Session() as session:
    # CSV file and table name
    csv_file = "/home/kusime/Desktop/Project/loyaer/users.csv"
    table = "csv_import_test"

    # SQL query to load data
    sql = text(
        f"""
        LOAD DATA LOCAL INFILE '{csv_file}'
        REPLACE
        INTO TABLE {table}
        FIELDS TERMINATED BY ','
        LINES TERMINATED BY '\n';  -- assuming the CSV has a header row to ignore
        """
    )
    # REPLACE
    # validate data type
    # when pk is same: update(replace) the data

    # DEFAULT OR INGORE
    # pass the validate data type
    # insert the data as possible

    try:
        res = session.execute(sql)
        print("row?? > ", res.rowcount)
        session.commit()
        print("Data loaded successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
# sql = text("""show global variables like 'local_infile';""")
# sql = text("""set global local_infile=true;""")
