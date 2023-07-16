from presentation.common import *
from presentation.admin.admin import admin_login
from presentation.customer.customer import customer_login

def start():
    print_header()
    print_header("Continue as:")
    print()
    print("1. Admin")
    print("2. Customer")
    print("3. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        clear_terminal()
        admin_login()
    elif choice == "2":
        clear_terminal()
        customer_login()
    elif choice == "3":
        exit()
    