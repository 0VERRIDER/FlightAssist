from  presentation.common import *
from presentation.customer.modules.list_all_flights import list_all_flights
from presentation.customer.modules.search_flight import search_flight
def customer_login():
    print_header()
    print_header("WELCOME CUSTOMER")
    print("1. List All Flights")
    print("2. Search Flights")
    print("3. Cancel Booking")
    print("4. Get Details of Booking")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        clear_terminal()
        list_all_flights()
    elif choice == "2":
        clear_terminal()
        search_flight()
    elif choice == "3":
        clear_terminal()
        cancel_booking()
    elif choice == "4":
        clear_terminal()
        get_details_of_booking()
    elif choice == "5":
        exit()
    else:
        print("Invalid Choice")
        customer_login()