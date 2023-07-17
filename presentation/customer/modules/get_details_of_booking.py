from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.usecase.booking.get_booking_usecase import GetBookingUseCase, GetBookingRequest, GetBookingResponse, GetBookingError
from core.data.database.database_handler import DatabaseHandler as database_handler
from presentation.common import *

def get_booking_details(booking_repository):
    print_header()
    print_header("GET BOOKING")
    
    booking_id = input("Enter booking ID: ")
    request = GetBookingRequest(booking_id=booking_id)
    usecase = GetBookingUseCase(booking_repository, request)
    response = usecase.execute()

    if isinstance(response, GetBookingResponse):
        print_header("Booking Details for booking ID: " + str(booking_id))
        print("Booking ID: " + str(response.booking["booking_id"]))
        print("Flight ID: " + str(response.booking["flight_id"]))
        print("Seats: " + str(response.booking["booked_seats"]))
        print("Total Price: " + str(response.booking["flight_price"]))
        print("Date: " + str(response.booking["booking_date"]))
        print("Status: " + str(response.booking["booking_status"]))
        print("Seats Type: " + str(response.booking["booked_seats_type"]))
        print("Class: " + str(response.booking["flight_class"]))
        print("Meal Preference: " + str(response.booking["meal_preference"]))
    elif isinstance(response, GetBookingError):
        print(response.message)
    input("Press enter to continue...")
    clear_terminal()