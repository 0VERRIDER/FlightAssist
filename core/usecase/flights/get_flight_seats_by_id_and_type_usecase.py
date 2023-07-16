# import
from core.usecase.usecase import request, response, error

# Request
class GetFlightSeatsByIdAndTypeRequest(request):
    def __init__(self, flight_id, seat_type):
        self.flight_id = flight_id
        self.seat_type = seat_type

# Response
class GetFlightSeatsByIdAndTypeResponse(response):
    def __init__(self, flight_seats):
        self.flight_seats = flight_seats

# Error
class GetFlightSeatsByIdAndTypeError(error):
    def __init__(self, message):
        self.message = message

# Usecase
class GetFlightSeatsByIdAndTypeUseCase:
    def __init__(self, flight_repository, request):
        self.flight_repository = flight_repository
        self.request = request

    def execute(self):
        try:
            flight_seats = self.flight_repository.get_flight_seats_by_id_and_type(self.request.flight_id, self.request.seat_type)
            response = GetFlightSeatsByIdAndTypeResponse(flight_seats)
            return response
        except:
            error = GetFlightSeatsByIdAndTypeError("Error getting flight seats by id and type")
            return error