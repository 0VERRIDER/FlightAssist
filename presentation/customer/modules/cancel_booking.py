from core.services.cancel_flight_service import CancelFlightService
from core.data.database.database_handler import DatabaseHandler as database_handler
from presentation.common import *

def cancel_booking(booking_repository, flight_repository):
    print_header()
    print_header("CANCEL FLIGHT")

    cancel_flight_service = CancelFlightService(booking_repository, flight_repository )
    booking_id = input("Enter booking ID: ")
    seats_to_cancel = input("Enter seats to cancel(enter with comma seperation): ").split(",")
    seats_to_cancel = [seat.strip() for seat in seats_to_cancel]
    response = cancel_flight_service.cancel_flight(
        booking_id, 
        seats_to_cancel
    )
    print(response)
    input("Press enter to continue...")
    clear_terminal()