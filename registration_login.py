import re
import getpass  

users = []
MAX_ATTEMPTS = 3


def register():
    print("\n===== Registration =====")

    name = input("Enter Name: ").strip()

    email = input("Enter Email: ").strip()
    if not email.endswith("@gmail.com"):
        print("Error: Email must contain @gmail.com\n")
        return

    for user in users:
        if user["email"] == email:
            print("Error: Email already registered!\n")
            return

    try:
        age = int(input("Enter Age: "))
        if age <= 18:
            print("Error: Age must be greater than 18\n")
            return
    except ValueError:
        print("Error: Age must be a number\n")
        return

    city = input("Enter City: ").strip()

    country = input("Enter Country: ").strip().lower()
    if country != "pakistan":
        print("Error: Country must be Pakistan\n")
        return

    password = getpass.getpass("Enter Password: ")

    if len(password) < 8:
        print("Error: Password must be at least 8 characters\n")
        return

    if not re.search("[A-Za-z]", password):
        print("Error: Password must contain letters\n")
        return

    if not re.search("[0-9]", password):
        print("Error: Password must contain numbers\n")
        return

    users.append({
        "name": name,
        "email": email,
        "age": age,
        "city": city,
        "country": country,
        "password": password
    })

    print("Registration Successful!\n")


def user_dashboard(user):
    while True:
        print(f"\n===== Welcome {user['name']} =====")
        print("1. View My Details")
        print("2. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            print("\n--- Your Details ---")
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("Age:", user["age"])
            print("City:", user["city"])
            print("Country:", user["country"])
        elif choice == "2":
            print("Logged out successfully.\n")
            break
        else:
            print("Invalid option!")


def login():
    print("\n===== Login =====")

    attempts = 0

    while attempts < MAX_ATTEMPTS:
        identifier = input("Enter Email or Name: ").strip()
        password = getpass.getpass("Enter Password: ")

        for user in users:
            if (user["email"] == identifier or user["name"] == identifier) and user["password"] == password:
                print("Login Successful!\n")
                user_dashboard(user)
                return

        attempts += 1
        print(f"Invalid credentials! Attempts left: {MAX_ATTEMPTS - attempts}")

    print("Too many failed attempts. You are logged out!\n")


def main():
    while True:
        print("===== MAIN MENU =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()