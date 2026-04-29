# TASK 1: Defining log function at the top to ensure it's available for all subsequent code
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





# TASK 2: Extract function to scrape the Wikipedia page and return a cleaned DataFrame with the top 10 banks by market capitalization.
def extract(url=wiki_url):
    log_progress("Starting data extraction from Wikipedia...")
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

    log_progress("Data extraction from Wikipedia completed.")

    return df.head(10)

print(extract())

# print(wiki_res.__class__)
# print(wiki_res.status_code)

# If successful, parse the HTML
# if wiki_res.status_code == 200:
#    soup = BeautifulSoup(wiki_res.text, "html.parser")
#    tables = soup.find_all("table", {"class": "wikitable"})
#    print(tables[0].prettify()[:500])  # Print the first 500 characters of the first table
#    print(f"Found {len(tables)} tables")
