import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime
from io import StringIO


# TASK 1: Defining log function at the top to ensure it's available for all subsequent code
log_file     = "C:/Users/user/ProgrammingProjects/Coursera/IBM_DE/ibm-data-engineering/PythonETL/banks_project/code_log.txt"
exchange_csv = "C:/Users/user/ProgrammingProjects/Coursera/IBM_DE/ibm-data-engineering/PythonETL/banks_project/exchange_rate.csv"
output_csv   = "C:/Users/user/ProgrammingProjects/Coursera/IBM_DE/ibm-data-engineering/PythonETL/banks_project/banks_project_output.csv"

def log_progress(message):
    '''Logs the progress of the ETL code execution to a text file.'''
    timestamp_format = '%Y-%b-%d-%H:%M:%S'  # Year-Month-Day-Hour-Minute-Second
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + " : " + message + "\n")

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

# print(extract(url=wiki_url))




# TASK 3: Transform function to convert market capitalization from USD to GBP and EUR using exchange rates from a CSV file.
def transform(df, csv_path):
    '''Transforms the dataframe by adding GBP, EUR, INR columns.'''
    # Read exchange rates into a dictionary
    log_progress("Data transformation started...")
    rates = pd.read_csv(csv_path)
    exchange_rate = rates.set_index("Currency").to_dict()["Rate"]

    # Ensure values are floats
    gbp_rate = float(exchange_rate["GBP"])
    eur_rate = float(exchange_rate["EUR"])
    inr_rate = float(exchange_rate["INR"])

    # Add new columns, rounded to 2 decimals
    df["MC_GBP_Billion"] = [np.round(x * gbp_rate, 2) for x in df["MC_USD_Billion"]]
    df["MC_EUR_Billion"] = [np.round(x * eur_rate, 2) for x in df["MC_USD_Billion"]]
    df["MC_INR_Billion"] = [np.round(x * inr_rate, 2) for x in df["MC_USD_Billion"]]

    # Log entry
    log_progress("Data transformation complete.")

    return df


# TASK 4: Load function to save the transformed DataFrame to a CSV file.
def load_to_csv(df, output_path):
    '''Loads the transformed dataframe to a CSV file.'''
    df.to_csv(output_path, index=False)
    log_progress("Data saved to CSV file")



extracted_df = extract(url=wiki_url)
transformed_df = transform(df=extracted_df, csv_path=exchange_csv)
load_to_csv(df=transformed_df, output_path=output_csv)
#market_cap_5th_largest_eur = transformed_df.loc[4, "MC_EUR_Billion"]

#print(transformed_df)
#print(market_cap_5th_largest_eur)

# print(wiki_res.__class__)
# print(wiki_res.status_code)

# If successful, parse the HTML
# if wiki_res.status_code == 200:
#    soup = BeautifulSoup(wiki_res.text, "html.parser")
#    tables = soup.find_all("table", {"class": "wikitable"})
#    print(tables[0].prettify()[:500])  # Print the first 500 characters of the first table
#    print(f"Found {len(tables)} tables")
