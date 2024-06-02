from sqlalchemy import create_engine, select


from sqlalchemy.orm import sessionmaker

db_url = f"mysql+pymysql://admin:admin123#@localhost:3306/local_loyaltyprogram?charset=utf8mb4"
# the base level of sqlalchemy

engine = create_engine(db_url)
