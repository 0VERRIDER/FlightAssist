from core.services.view_seat_meal_pref_service import ViewSeatMealPrefService
from presentation.common import *

# This is the function that will be called from the main menu
def flight_meal_list(booking_repository, flight_repository):
    print_header()
    print_header("FLIGHT MEAL PREFRENCES")

    # Create an instance of the service
    view_seat_meal_pref_service = ViewSeatMealPrefService(booking_repository)   

    # Get the flight id from the user
    flight_id = input("Enter Flight ID: ").upper()

    # Get the class from the user
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

    # Call the service to get the seat meal prefrences
    response = view_seat_meal_pref_service.get_seat_meal_pref(flight_id, class_name)

    print_header("FLIGHT MEAL PREFRENCES FOR FLIGHT ID: " + flight_id + " AND CLASS: " + class_name)

    # Print the response
    for mf in response:
        print("Seat: " + mf["booked_seats"] + " Meal Pref: " + mf["meal_preference"])
    input("Press enter to continue...")
    clear_terminal()