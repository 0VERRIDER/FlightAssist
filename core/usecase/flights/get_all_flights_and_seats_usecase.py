#import
from core.usecase.usecase import request, response, error

# Request
class GetAllFlightsAndSeatsRequest(request):
    def __init__(self):
        pass

# Response
class GetAllFlightsAndSeatsResponse(response):
    def __init__(self, flights_and_seats):
        self.flights_and_seats = flights_and_seats

# Error
class GetAllFlightsAndSeatsError(error):
    def __init__(self, message):
        self.message = message

# Usecase
class GetAllFlightsAndSeatsUseCase:
    def __init__(self, flight_repository, request):
        self.flight_repository = flight_repository
        self.request = request

    def execute(self):
        flights_and_seats = self.flight_repository.get_all_flights_and_seats()
        try:
            response = GetAllFlightsAndSeatsResponse(flights_and_seats)
            return response
        except:
            error = GetAllFlightsAndSeatsError("Error getting all flights and seats")
            return error