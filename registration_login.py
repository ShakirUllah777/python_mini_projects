users = []
import re

def register():
    print('-----Registtation------')

    name = input("Enter You Name: ").strip()

    email = input("Enter Your Email: ").strip()
    if not email.endswith('@gmail.com'):
        print('Erro: Email must conation the @gmail.com')
        return
    
    for user in users:
        if user['email'] == email:
            print('Email Alreday exits!')
            return

    try:
        age = int(input("Enter Your age: "))
        if age <= 18:
            print('Error: Age must be grater than 18')
            return
    except ValueError:
        print('Erro: Age must be Number!')
        return
    
    city = input("Enter Your City: ")


    country = input("Enter Your Country: ").strip().lower()
    if country != 'pakistan':
        print('Error: Only Pakistan Country is allowed')
        return
    
    password = input("Enter Your Password: ")
    if len(password) < 8:
        print('Error: Password must be atleast 8 chaacter')
    elif not re.search("[A-Za-z]",password):
        print("Error: Password must conation Letter: ")
    elif not re.search('[0-9]',password):
        print('Error: Password must contain number: ')
        return

    users_data = {
        'name': name,
        'email': email,
        "age":  age,
        'city' : city,
        'country': country,
        "password": password
    }

    users.append(users_data)
    print('Data Added succesfully!')


def login():
    print('---Login Page-----')


    identifier = input('Enter Name/Email: ').strip()
    password = input('Enter Password: ')

    for user in users:
            if user['email'] == identifier or user['name'] == identifier and user['password'] == password:
                print(f"Login Successful! Welcome {user['name']}\n")
                return

    print('Invalid Credeational!')



def main():
    while True:
        print('----- Menu -----')
        print('1. Register')
        print('2. Login')
        print('3. Exits')


        choice = input('Enter Your Choice (1/2/3): ')


        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print('GoodBye....')
            break
        else:
            print('Invalid Options!')


if __name__ == '__main__':
    main()

        
