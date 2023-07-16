#import
from core.usecase.usecase import request, response, error

# Request
class GetFlightSeatTypesByIdRequest(request):
    def __init__(self, flight_id):
        self.flight_id = flight_id

# Response
class GetFlightSeatTypesByIdResponse(response):
    def __init__(self, flight_seat):
        self.flight_seat = flight_seat

# Error
class GetFlightSeatTypesByIdError(error):
    def __init__(self, message):
        self.message = message

# Usecase
class GetFlightSeatTypesByIdUseCase:
    def __init__(self, flight_repository, request):
        self.flight_repository = flight_repository
        self.request = request

    def execute(self):
        try:
            flight_seat = self.flight_repository.get_flight_types_by_id(self.request.flight_id)
            response = GetFlightSeatTypesByIdResponse(flight_seat)
            return response
        except Exception as e:
            error = GetFlightSeatTypesByIdError("Error getting flight seat by id" + str(e))
            return error
