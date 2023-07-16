from core.usecase.booking.update_booking_usecase import UpdateBookingUseCase, UpdateBookingRequest, UpdateBookingResponse, UpdateBookingError
from core.usecase.booking.delete_booking_usecase import DeleteBookingUseCase, DeleteBookingRequest, DeleteBookingResponse, DeleteBookingError
from core.usecase.booking.get_booking_usecase import GetBookingUseCase, GetBookingRequest, GetBookingResponse, GetBookingError
from core.utils.string_utils import StringUtils
from core.utils.seat_util import get_seat_type_from_seat_number as get_seat_type
from core.usecase.flights.get_flight_seats_by_id_usecase import GetFlightSeatByIdUseCase, GetFlightSeatByIdRequest, GetFlightSeatByIdResponse, GetFlightSeatByIdError

class CancelFlightService:
    def __init__(self, booking_repository, flight_repository):
        self.booking_repository = booking_repository
        self.flight_repository = flight_repository

    def cancel_flight(self, booking_id, seats_to_cancel):
        booking = []
        # Get booking details
        get_booking_request = GetBookingRequest(booking_id)
        get_booking_usecase = GetBookingUseCase(self.booking_repository, get_booking_request)
        get_booking_response = get_booking_usecase.execute()
        if isinstance(get_booking_response, GetBookingResponse):
            booking = get_booking_response.booking
        elif isinstance(get_booking_response, GetBookingError):
            raise Exception(get_booking_response.message)
        

        # If the number of seats to cancel is equal to the number of seats in the booking, delete the booking
        if len(seats_to_cancel) == 0 or seats_to_cancel == StringUtils(booking["booked_seats"]).to_list():
            delete_booking_request = DeleteBookingRequest(booking_id)
            delete_booking_usecase = DeleteBookingUseCase(self.booking_repository, delete_booking_request)
            delete_booking_response = delete_booking_usecase.execute()
            if isinstance(delete_booking_response, DeleteBookingResponse):
                return True
            elif isinstance(delete_booking_response, DeleteBookingError):
                return False
        else:
            # get flight seat-arrangement
            get_flight_seats = GetFlightSeatByIdRequest(booking["flight_id"])
            get_flight_seats_usecase = GetFlightSeatByIdUseCase(self.flight_repository, get_flight_seats)
            get_flight_seats_response = get_flight_seats_usecase.execute()
            seats = {}

            if isinstance(get_flight_seats_response, GetFlightSeatByIdResponse):
                seats = get_flight_seats_response.flight_seat
            elif isinstance(get_flight_seats_response, GetFlightSeatByIdError):
                raise Exception("Booking Failed!" + get_flight_seats_response.message)
            

            old_seats = StringUtils(booking["booked_seats"]).to_list()
            updated_seats = [seat for seat in old_seats if seat not in seats_to_cancel]
            updated_seat_types = get_seat_type(seats[booking["flight_class"]]["seat_arrangement"],updated_seats)
            update_booking_request = UpdateBookingRequest(booking_id, None, None, None, updated_seats, updated_seat_types, None, None, None)
            update_booking_usecase = UpdateBookingUseCase(self.booking_repository, update_booking_request)
            update_booking_response = update_booking_usecase.execute()
            if isinstance(update_booking_response, UpdateBookingResponse):
                print("Eureka")
                return True
            elif isinstance(update_booking_response, UpdateBookingError):
                print(update_booking_response.message)
                return False
