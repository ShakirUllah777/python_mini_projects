# Expense class and CRUD operations
import csv
from utils import FILE_PATH


class Expense:
    @staticmethod
    def add_expense(date, category, amount, description):
        with open(FILE_PATH, 'r') as file:
            reader = list(csv.reader(file))
            id = len(reader)

        with open(FILE_PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, date, category, amount, description])

        print('Expense Added Successfully!')
    
    @staticmethod
    def view_expense():
        with open(FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    @staticmethod
    def delete_expense(expense_id):
        rows = []
        with open(FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != expense_id:
                    rows.append(row)

        with open(FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(rows)
        print(f'Expense with ID {expense_id} Deleted Succesfully!')
         