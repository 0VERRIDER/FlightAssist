from core.usecase.booking.add_booking_usecase import AddBookingUseCase, AddBookingRequest, AddBookingResponse, AddBookingError
from core.usecase.booking.get_flight_by_flight_id_and_flight_class_usecase import GetFlightByFlightIdAndFlightClassUseCase, GetFlightByFlightIdAndFlightClassRequest, GetFlightByFlightIdAndFlightClassResponse, GetFlightByFlightIdAndFlightClassError
from core.utils.seat_util import get_seat_type_from_seat_number as get_seat_type
from core.utils.seat_util import generate_seat_structure
from core.usecase.flights.get_flight_seats_by_id_usecase import GetFlightSeatByIdUseCase, GetFlightSeatByIdRequest, GetFlightSeatByIdResponse, GetFlightSeatByIdError
from core.utils.string_utils import StringUtils

class AvailableSeatsByFlightAndClassService:
    def __init__(self, booking_repository, flight_repository):
        self.booking_repository = booking_repository
        self.flight_repository = flight_repository

    def get_available_seats_by_flight_and_class(self, flight_id, flight_class):
        try:
            # Count of bookings
            get_booked_flight_details = GetFlightByFlightIdAndFlightClassRequest(flight_id, flight_class)
            get_booked_flight_details_usecase = GetFlightByFlightIdAndFlightClassUseCase(self.booking_repository, get_booked_flight_details)
            get_booked_flight_details_response = get_booked_flight_details_usecase.execute()
            flights= []

            if isinstance(get_booked_flight_details_response, GetFlightByFlightIdAndFlightClassResponse):
                flights = get_booked_flight_details_response.flight
            elif isinstance(get_booked_flight_details_response, GetFlightByFlightIdAndFlightClassError):
                raise Exception("Booking Failed!" + get_booked_flight_details_response.message)

            #Get Seat Details
            get_flight_seats = GetFlightSeatByIdRequest(flight_id)
            get_flight_seats_usecase = GetFlightSeatByIdUseCase(self.flight_repository, get_flight_seats)
            get_flight_seats_response = get_flight_seats_usecase.execute()
            seats = {}

            if isinstance(get_flight_seats_response, GetFlightSeatByIdResponse):
                seats = get_flight_seats_response.flight_seat
            elif isinstance(get_flight_seats_response, GetFlightSeatByIdError):
                raise Exception("Booking Failed!" + get_flight_seats_response.message)
            
            total_booked_seats = []
            for booking in flights:
                booking =StringUtils(booking["booked_seats"]).to_list()
                total_booked_seats.extend(booking)
            
            return generate_seat_structure(seats[flight_class]["seat_arrangement"],seats[flight_class]["rows"], total_booked_seats)

        except Exception as e:
            return AddBookingError(str(e))