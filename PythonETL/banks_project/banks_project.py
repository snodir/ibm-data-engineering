import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

log_file = "C:/Users/user/ProgrammingProjects/Coursera/IBM_DE/ibm-data-engineering/PythonETL/banks_project/code_log.txt"

# Defining log function at the top to ensure it's available for all subsequent code
def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 


wiki_url = "https://en.wikipedia.org/wiki/List_of_largest_banks"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36"
}




def extract():
    # Log the initialization of the ETL process 
    log_progress(message = "Extraction started")
    wiki_res = requests.get(url=wiki_url, headers=headers)
    soup = BeautifulSoup(wiki_res.text, "html.parser")

    # Find the table under "By market capitalization"
    tables = soup.find_all("table", {"class": "wikitable"})
    df = pd.read_html(str(tables[0]))[0]   # first table is the one we need

    # Keep only required columns
    df = df[["Bank name", "Market cap(US$ billion)"]]
    df.columns = ["Name", "MC_USD_Billion"]

    # Top 10
    df = df.head(10)
    log_progress("Extraction completed")
    return df

print(extract())


def transform(df, exchange_csv):
    log_progress("Transformation started")
    rates = pd.read_csv(exchange_csv)
    rates_dict = dict(zip(rates["Currency"], rates["Rate"]))

    df["MC_GBP_Billion"] = (df["MC_USD_Billion"] * rates_dict["GBP"]).round(2)
    df["MC_EUR_Billion"] = (df["MC_USD_Billion"] * rates_dict["EUR"]).round(2)
    df["MC_INR_Billion"] = (df["MC_USD_Billion"] * rates_dict["INR"]).round(2)

    log_progress("Transformation completed")
    return df


# print(wiki_res.__class__)
# print(wiki_res.status_code)

# If successful, parse the HTML
# if wiki_res.status_code == 200:
#    soup = BeautifulSoup(wiki_res.text, "html.parser")
#    tables = soup.find_all("table", {"class": "wikitable"})
#    print(tables[0].prettify()[:500])  # Print the first 500 characters of the first table
#    print(f"Found {len(tables)} tables")
