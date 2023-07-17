from presentation.common import *
from core.services.available_seats_by_flight_and_class_service import AvailableSeatsByFlightAndClassService

def seat_availability(booking_repository, flight_repository):
    print_header()
    print_header("SEAT AVAILABILITY")

    flight_id = input("Enter flight ID: ")
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
        seat_availability(booking_repository, flight_repository)

    print_header("Available seats in: " + class_name)
            
    available_seats_by_flight_and_class_service = AvailableSeatsByFlightAndClassService(booking_repository, flight_repository) 

    response = available_seats_by_flight_and_class_service.get_available_seats_by_flight_and_class(flight_id, class_name)
    
    for seat_row in response:
        print(seat_row)
        
    input("Press enter to continue...")
    clear_terminal()