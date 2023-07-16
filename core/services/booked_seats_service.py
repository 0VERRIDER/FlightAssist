from core.usecase.booking.get_flight_by_flight_id_and_flight_class_usecase import GetFlightByFlightIdAndFlightClassUseCase, GetFlightByFlightIdAndFlightClassRequest, GetFlightByFlightIdAndFlightClassResponse, GetFlightByFlightIdAndFlightClassError
from core.utils.string_utils import StringUtils

class BookedSeatsService:
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

            
            total_booked_seats = []
            for booking in flights:
                booking =StringUtils(booking["booked_seats"]).to_list()
                total_booked_seats.extend(booking)
            
            return total_booked_seats
        except Exception as e:
            return "Error"