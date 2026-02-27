# utility function (like the file initialization)
import csv
import os


FILE_PATH = 'data/expense.csv'

def initialize_file():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, mode='w' , newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Date", "Category", "Amount", "Description"])

