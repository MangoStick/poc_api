import pandas as pd
from sqlalchemy import create_engine

SERVER = 'DESKTOP-8IL2S7E\MSSQLSERVER02'
DATABASE = 'fast'
USERNAME = 'sa'
PASSWORD = 'admin123'


# Create a SQLAlchemy engine
connection_string = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
engine = create_engine(connection_string)


def sql_query(_query):
    # Execute the SQL query and return the result as a DataFrame
    with engine.connect() as connection:
        df = pd.read_sql_query(_query, connection)
        data = df.to_dict(orient='records')
    return data

def sql():
    try:
        _query = "SELECT TOP 5 * FROM tb_fast"
        data = sql_query(_query)
        print(data)
        return data
    except Exception as e:
        print(f"Error: {str(e)}")