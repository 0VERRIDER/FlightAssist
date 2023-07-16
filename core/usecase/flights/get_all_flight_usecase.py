#import
from core.usecase.usecase import request, response, error

# Request
class GetAllFlightsRequest(request):
    def __init__(self):
        pass

# Response  
class GetAllFlightsResponse(response):
    def __init__(self, flights):
        self.flights = flights

# Error
class GetAllFlightsError(error):
    def __init__(self, message):
        self.message = message

# Usecase
class GetAllFlightsUseCase:
    def __init__(self, flight_repository, request):
        self.flight_repository = flight_repository
        self.request = request

    def execute(self):
        flights = self.flight_repository.get_all_flights()
        try:
            response = GetAllFlightsResponse(flights)
            return response
        except:
            error = GetAllFlightsError("Error getting all flights")
            return error