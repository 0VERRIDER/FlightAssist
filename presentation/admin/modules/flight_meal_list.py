from core.services.view_seat_meal_pref_service import ViewSeatMealPrefService
from presentation.common import *

def flight_meal_list(booking_repository, flight_repository):
    print_header()
    print_header("FLIGHT MEAL PREFRENCES")

    view_seat_meal_pref_service = ViewSeatMealPrefService(booking_repository)   
    flight_id = input("Enter Flight ID: ").upper()

    print("Select class:")
    print("1. Economy")
    print("2. Business")

    class_choice = input("Enter your choice: ")

    if class_choice == "1":
        class_name = "ECONOMY"
    elif class_choice == "2":
        class_name = "BUSINESS"
    else:
        print("Invalid Choice")

    response = view_seat_meal_pref_service.get_seat_meal_pref(flight_id, class_name)
    print_header("FLIGHT MEAL PREFRENCES FOR FLIGHT ID: " + flight_id + " AND CLASS: " + class_name)
    for mf in response:
        print("Seat: " + mf["booked_seats"] + " Meal Pref: " + mf["meal_preference"])
    input("Press enter to continue...")
    clear_terminal()