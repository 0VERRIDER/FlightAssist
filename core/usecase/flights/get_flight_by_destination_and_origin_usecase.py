# import
from core.usecase.usecase import request, response, error

# Request
class GetFlightByDestinationAndOriginRequest(request):
    def __init__(self, destination, origin):
        self.destination = destination
        self.origin = origin

# Response
class GetFlightByDestinationAndOriginResponse(response):
    def __init__(self, flights):
        self.flights = flights
# Error
class GetFlightByDestinationAndOriginError(error):
    def __init__(self, message):
        self.message = message

# Usecase
class GetFlightByDestinationAndOriginUseCase:
    def __init__(self, flight_repository, request):
        self.flight_repository = flight_repository
        self.request = request

    def execute(self):
        try:
            flights = self.flight_repository.get_flight_by_origin_and_destination(self.request.destination, self.request.origin)
            response = GetFlightByDestinationAndOriginResponse(flights)
            return response
        
        except Exception as e:
            error = GetFlightByDestinationAndOriginError("Error getting flight by destination and origin" + str(e))
            return error