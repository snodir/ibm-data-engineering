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






# print(wiki_res.__class__)
# print(wiki_res.status_code)

# If successful, parse the HTML
# if wiki_res.status_code == 200:
#    soup = BeautifulSoup(wiki_res.text, "html.parser")
#    tables = soup.find_all("table", {"class": "wikitable"})
#    print(tables[0].prettify()[:500])  # Print the first 500 characters of the first table
#    print(f"Found {len(tables)} tables")
