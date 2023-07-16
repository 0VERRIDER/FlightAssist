#import
from core.usecase.usecase import request, response, error

#request
class GetFlightByOriginRequest(request):
    def __init__(self, origin):
        self.origin = origin

#response
class GetFlightByOriginResponse(response):
    def __init__(self, flight):
        self.flight = flight

#error
class GetFlightByOriginError(error):
    def __init__(self, message):
        self.message = message

#usecase
class GetFlightByOriginUseCase:
    def __init__(self, flight_repository, request):
        self.flight_repository = flight_repository
        self.request = request

    def execute(self):
        try:
            flight = self.flight_repository.get_flight_by_origin(self.request.origin)
            response = GetFlightByOriginResponse(flight)
            return response
        except:
            error = GetFlightByOriginError("Error getting flight by origin")
            return error
        