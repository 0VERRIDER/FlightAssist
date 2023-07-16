# import
from core.usecase.usecase import request, response, error

# Request
class GetFlightRequest(request):
    def __init__(self, flight_id):
        self.flight_id = flight_id

# Response
class GetFlightResponse(response):
    def __init__(self, flight):
        self.flight = flight

# Error
class GetFlightError(error):
    def __init__(self, message):
        self.message = message

# Usecase
class GetFlightUseCase:
    def __init__(self, flight_repository, request):
        self.flight_repository = flight_repository
        self.request = request

    def execute(self):
        try:
            flight = self.flight_repository.get_flight(self.request.flight_id)
            response = GetFlightResponse(flight)
            return response
        except:
            error = GetFlightError("Error getting flight")
            return error
