from  presentation.common import *
import tests.unittests as unittests
from presentation.admin.modules.flight_meal_list import flight_meal_list

def admin_login(booking_repository, flight_repository):
    print_header()
    print_header("WELCOME ADMIN")
    print()
    print("1. Run Unit Tests")
    print("2. Show Flight and meal details")
    print("*** Other Features are not implemented ***")
    print("3. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        clear_terminal()
        unittests.run_tests()

    elif choice == "2":
        flight_meal_list(booking_repository, flight_repository)

    elif choice == "3":
        exit()

    else:
        print("Invalid Choice")
        admin_login(booking_repository, flight_repository)
            