from  presentation.common import *
from presentation.customer.modules.cancel_booking import cancel_booking
from presentation.customer.modules.get_details_of_booking import get_booking_details
from presentation.customer.modules.list_all_flights import list_all_flights
from presentation.customer.modules.search_flight import search_flight
from presentation.customer.modules.seat_availability import seat_availability

def customer_login(booking_repository, flight_repository):
    print_header()
    print_header("WELCOME CUSTOMER")
    print("1. List All Flights")
    print("2. Search Flights")
    print("3. Check Seat Availability")
    print("4. Get Details of Booking")
    print("5. Cancel Booking")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        clear_terminal()
        list_all_flights(booking_repository, flight_repository)
    elif choice == "2":
        clear_terminal()
        search_flight(booking_repository, flight_repository)
    elif choice == "3":
        clear_terminal()
        seat_availability(booking_repository, flight_repository)
    elif choice == "4":
        clear_terminal()
        get_booking_details(booking_repository)
   
    elif choice == "5":
        clear_terminal()
        cancel_booking(booking_repository, flight_repository)

    elif choice == "6":
        exit()
    else:
        print("Invalid Choice")
        customer_login()