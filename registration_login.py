users = []

def register():
    print('-----Registtation------')

    name = input("Enter You Name: ")
    email = input("Enter Your Email: ")
    age = int(input("Enter Your age: "))
    city = input("Enter Your City: ")
    country = input("Enter Your Country: ")
    password = input("Enter Your Password: ")


    for user in users:
        if user['email'] == email:
            print('Email Alreday exits!')
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
    print('1. Email + Password')
    print('2. Name + Password')

    choice = input('Enter the choice (1/2) ')

    identifier = input('Enter Name/Email: ')
    password = input('Enter Password: ')

    for user in users:
        if choice == '1':
            if user['email'] == identifier and user['password'] == password:
                print(f"Login Successful! Welcome {user['name']}\n")
                return
            
        elif choice == '2':
            if user['name'] == identifier and user['password'] == password:
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

        
