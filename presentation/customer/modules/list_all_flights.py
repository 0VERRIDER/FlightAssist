from core.usecase.flights.get_all_flight_usecase import GetAllFlightsUseCase, GetAllFlightsResponse, GetAllFlightsError, GetAllFlightsRequest
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles

def list_all_flights():
    file = ReadFiles("./data_files/flight_data_test").read()
    file_flight_repository = FileFlightRepository(file)
    request = GetAllFlightsRequest()
    usecase = GetAllFlightsUseCase(file_flight_repository, request)
    response = usecase.execute()

    if isinstance(response, GetAllFlightsResponse):
        print(response.flights)
    elif isinstance(response, GetAllFlightsError):
        print("Use cases test failed: " + response.message)