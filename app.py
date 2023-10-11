import pyodbc
import pandas as pd
from pyodbc import Connection

SERVER = 'DESKTOP-8IL2S7E\MSSQLSERVER02'
DATABASE = 'fast'
USERNAME = 'sa'
PASSWORD = 'admin123'

connection_string = (
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    f'UID={USERNAME};'
    f'PWD={PASSWORD};'
    'Encrypt=yes;'
    'TrustServerCertificate=yes;'
)

conn: Connection = None


def sql_query(_query):
    conn = pyodbc.connect(connection_string)
    df = pd.read_sql_query(_query, conn)
    data = df.to_dict(orient='records')
    conn.close()
    return data

try:
    # conn = pyodbc.connect(connection_string)
    _query = "SELECT TOP 5 * FROM tb_fast"
    # df = pd.read_sql_query(_query, conn)
    # data = df.to_dict(orient='records')
    # print(data)

    data = sql_query(_query)
    print(data)


except pyodbc.Error as e:
    print(f"Error connecting to the database: {str(e)}")
# finally:
#     conn.close()