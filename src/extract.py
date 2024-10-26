import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import errorcode
import numpy as np
import os
import pandas as pd
import yaml

# drinks = pd.read_csv('./drinks_dataset.csv')
# df = pd.DataFrame(drinks)

def load_csv(csv_directory):
    try:
        for files in os.listdir(csv_directory):
            if files.endswith('.csv'):
                books = pd.read_csv(os.path.join(csv_directory, files))  # If the values in the CSV file contain commas, then it must be enclosed inside double quotes.
                df = pd.DataFrame(books)
                print(df)

    except FileNotFoundError:
        print(f'Directory must exist {csv_directory}')

def main():
    csv_directory = '../data/tests/'
    load_csv(csv_directory)


main()

