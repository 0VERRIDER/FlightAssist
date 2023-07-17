from presentation.common import *
from core.services.available_seats_by_flight_and_class_service import AvailableSeatsByFlightAndClassService
from core.services.book_flight_service import BookFlightService
from datetime import date

def book_flight(booking_repository, flight_repository, flight):
    print_header()
    print_header("Booking Flight " + flight["flight_name"])

    booking_name = input("Enter your name: ")
    booking_email = input("Enter your email: ")

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
        book_flight(booking_repository, flight_repository, flight)

    print_header("Available seats in: " + class_name)
    
    # Create an instance of the service
    available_seats_by_flight_and_class_service = AvailableSeatsByFlightAndClassService(booking_repository, flight_repository) 

    # Call the service to get the available seats
    response = available_seats_by_flight_and_class_service.get_available_seats_by_flight_and_class(flight["flight_id"], class_name)
    
    # Print the response
    for seat_row in response:
        print(seat_row)
        

    seats_to_book = input("Enter seats to book(enter with comma seperation): ").split(",")
    seats_to_book = [seat.strip().upper() for seat in seats_to_book]

    print("Select meal preference:")
    print("1. Veg")
    print("2. Non-Veg")
    print("3. None")

    meal_choice = input("Enter your choice: ")

    if meal_choice == "1":
        meal_preference = "VEG"
    elif meal_choice == "2":
        meal_preference = "NON-VEG"
    else:
        meal_preference = "None"

    book_flight_service = BookFlightService(booking_repository, flight_repository)               
    response = book_flight_service.book_flight(
            0, 
            flight["flight_id"], 
            date.today(), 
            "Confirmed", 
            seats_to_book, 
            class_name, 
            meal_preference,
            booking_email,
            "",
            booking_name,
            )
    
    if response[0].booking_id:
        print("Booking Successful")
        print("Booking ID: " + str(response[0].booking_id))
        print("Total Fare: " + str(response[1]))
    else:
        print(response.message)
    input("Press enter to continue...")


