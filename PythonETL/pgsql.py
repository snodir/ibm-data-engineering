import pandas as pd
import psycopg2
from psycopg2 import OperationalError, sql

# Connection parameters — replace with your actual cluster details
DB_HOST = "your-cluster-name.postgres.cosmos.azure.com"
DB_PORT = 5432
DB_NAME = "your_database"
DB_USER = "your_user@your-cluster-name"
DB_PASSWORD = "your_password"
SSL_MODE = "require"  # Azure Cosmos DB for PostgreSQL requires SSL

def create_connection():
    """Create a PostgreSQL connection with SSL."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            sslmode=SSL_MODE
        )
        print("✅ Connection to Azure Cosmos DB for PostgreSQL successful.")
        return conn
    except OperationalError as e:
        print(f"❌ Error: Could not connect to the database.\nDetails: {e}")
        return None

def fetch_data(query):
    """Fetch data into a pandas DataFrame."""
    conn = create_connection()
    if conn is None:
        return None
    try:
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        print(f"❌ Error executing query: {e}")
        return None
    finally:
        conn.close()

if __name__ == "__main__":
    # Example query — adjust to your table
    query = "SELECT * FROM your_table LIMIT 10;"
    df = fetch_data(query)
    if df is not None:
        print(df)


from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
)

df = pd.read_sql("SELECT * FROM your_table LIMIT 10;", engine)
print(df)
