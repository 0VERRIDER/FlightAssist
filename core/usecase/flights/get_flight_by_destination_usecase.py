#import
from core.usecase.usecase import request, response, error

# Request
class GetFlightByDestinationRequest(request):
    def __init__(self, destination):
        self.destination = destination

# Response
class GetFlightByDestinationResponse(response):
    def __init__(self, flight):
        self.flight = flight

# Error
class GetFlightByDestinationError(error):
    def __init__(self, message):
        self.message = message

# Usecase
class GetFlightByDestinationUseCase:
    def __init__(self, flight_repository, request):
        self.flight_repository = flight_repository
        self.request = request

    def execute(self):
        try:
            flight = self.flight_repository.get_flight_by_destination(self.request.destination)
            response = GetFlightByDestinationResponse(flight)
            return response
        except:
            error = GetFlightByDestinationError("Error getting flight by destination")
            return error