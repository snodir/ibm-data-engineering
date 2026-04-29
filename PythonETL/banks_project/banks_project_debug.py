# Task 1: Defining log function at the top to ensure it's available for all subsequent code

log_file = "C:/Users/user/ProgrammingProjects/Coursera/IBM_DE/ibm-data-engineering/PythonETL/banks_project/code_log.txt"

def log_progress(message):
    '''Logs the progress of the ETL code execution to a text file.'''
    timestamp_format = '%Y-%b-%d-%H:%M:%S'  # Year-Month-Day-Hour-Minute-Second
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + " : " + message + "\n")


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime
from io import StringIO


wiki_url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
headers = {"User-Agent": "Mozilla/5.0"}

log_progress("Preliminaries complete. Initiating ETL process...")




def extract(url=wiki_url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    # Find the heading "By market capitalization"
    heading = soup.find(lambda tag: tag.name in ["h2", "h3"] and "capitalization" in tag.get_text())
    target_table = heading.find_next("table", {"class": "wikitable"})
    df = pd.read_html(StringIO(str(target_table)))[0]

    # Flatten MultiIndex columns
    df.columns = [' '.join([str(c) for c in col if c]) if isinstance(col, tuple) else str(col) for col in df.columns]
    df.columns = [c.strip() for c in df.columns]

    print("Extracted columns:", df.columns.tolist())  # Debug

    # Dynamically detect columns
    name_col = [c for c in df.columns if "Bank" in c or "Name" in c][0]
    mc_col   = [c for c in df.columns if "Market" in c and "US$" in c][0]

    df = df[[name_col, mc_col]]
    df = df.rename(columns={name_col: "Name", mc_col: "MC_USD_Billion"})

    # Clean Market Cap values
    df["MC_USD_Billion"] = df["MC_USD_Billion"].astype(str).str.replace(r"\n", "", regex=True)
    df["MC_USD_Billion"] = df["MC_USD_Billion"].astype(float)

    return df.head(10)

print(extract(url=wiki_url))


def transform(df, exchange_csv):
    log_progress("Transformation started")
    rates = pd.read_csv(exchange_csv)
    rates_dict = dict(zip(rates["Currency"], rates["Rate"]))

    df["MC_GBP_Billion"] = (df["MC_USD_Billion"] * rates_dict["GBP"]).round(2)
    df["MC_EUR_Billion"] = (df["MC_USD_Billion"] * rates_dict["EUR"]).round(2)
    df["MC_INR_Billion"] = (df["MC_USD_Billion"] * rates_dict["INR"]).round(2)

    log_progress("Transformation completed")
    return df


def load_to_csv(df, path):
    log_progress("Loading to CSV started")
    df.to_csv(path, index=False)
    log_progress("Loading to CSV completed")



def load_to_db(df, db_name, table_name):
    log_progress("Loading to DB started")
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    log_progress("Loading to DB completed")



def run_queries(db_name, table_name):
    log_progress("Running queries started")
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Example queries
    print(cur.execute(f"SELECT * FROM {table_name}").fetchall())
    print(cur.execute(f"SELECT AVG(MC_USD_Billion) FROM {table_name}").fetchone())

    conn.close()
    log_progress("Running queries completed")


# print(wiki_res.__class__)
# print(wiki_res.status_code)

# If successful, parse the HTML
# if wiki_res.status_code == 200:
#    soup = BeautifulSoup(wiki_res.text, "html.parser")
#    tables = soup.find_all("table", {"class": "wikitable"})
#    print(tables[0].prettify()[:500])  # Print the first 500 characters of the first table
#    print(f"Found {len(tables)} tables")
