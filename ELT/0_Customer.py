import pandas as pd
from sqlalchemy import create_engine


data = pd.read_csv(r"D:\DAC_K49\Customer Master.csv")

data['ingestion_date'] = pd.Timestamp.now()

print(data.head())

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
print("Connection to PostgreSQL database successfully!")

data.to_sql(
    name = 'customer',
    con = engine,
    schema = 'bronze',
    if_exists = 'replace'
)

