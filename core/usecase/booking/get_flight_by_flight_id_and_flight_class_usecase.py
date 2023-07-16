# import
from core.usecase.usecase import request, response, error

# Request
class GetFlightByFlightIdAndFlightClassRequest(request):
    def __init__(self, flight_id, flight_class):
        self.flight_id = flight_id
        self.flight_class = flight_class

# Response
class GetFlightByFlightIdAndFlightClassResponse(response):
    def __init__(self, flight):
        self.flight = flight

# Error
class GetFlightByFlightIdAndFlightClassError(error):
    def __init__(self, message):
        super().__init__(message)

# Usecase
class GetFlightByFlightIdAndFlightClassUseCase:
    def __init__(self, flight_repository, request):
        self.flight_repository = flight_repository
        self.request = request

    def execute(self):
        try:
            flight = self.flight_repository.get_flight_by_flight_id_and_flight_class(self.request.flight_id, self.request.flight_class)
            return GetFlightByFlightIdAndFlightClassResponse(flight)
        except Exception as err:
            return GetFlightByFlightIdAndFlightClassError(err)