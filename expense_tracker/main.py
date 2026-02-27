from utils import initialize_file
from expense import Expense


initialize_file()

def main():
    while True:
        print('\n ======= Your Daily Expense Tracker =====')
        print('1. Add Expense')
        print('2. View Expense')
        print('3. Delete Expense')
        print('4. Exits')

        choice = input('Enter Your Choice: ')


        if choice == '1':
            date = input('Enter date (YYYY-MM-DD)')
            category  = input('Enter category (Food/Travel/etc): ')
            amount  = input('Enteramount ')
            description  = input('Enter description ')
            Expense.add_expense(date, category, amount , description)

        elif choice == '2':
            Expense.view_expense()

        elif choice == '3':
            expense_id = input('Enter Expense Id to delete: ')
            Expense.delete_expense(expense_id)

        elif choice == '4':
            print('Goodbye...')
            break
        else:
            print('Invalid Choice!')


if __name__ == '__main__':
    main()

        