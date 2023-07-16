from core.usecase.flights.get_all_flights_and_seats_usecase import GetAllFlightsAndSeatsUseCase, GetAllFlightsAndSeatsRequest, GetAllFlightsAndSeatsResponse, GetAllFlightsAndSeatsError
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from colorama import Fore, Style

class TestGetAllFlightsAndSeatsUseCase:
    def test_get_all_flights_and_seats_usecase(self):
        file = ReadFiles("./data_files/flight_data_test").read()
        file_flight_repository = FileFlightRepository(file)

        get_all_flights_and_seats_request = GetAllFlightsAndSeatsRequest()
        get_all_flights_and_seats_usecase = GetAllFlightsAndSeatsUseCase(file_flight_repository, get_all_flights_and_seats_request)
        get_all_flights_and_seats_response = get_all_flights_and_seats_usecase.execute()

        if isinstance(get_all_flights_and_seats_response, GetAllFlightsAndSeatsResponse):
            return(Fore.GREEN + "Test get all flights and seats usecase passed" + Style.RESET_ALL)
        elif isinstance(get_all_flights_and_seats_response, GetAllFlightsAndSeatsError):
            return(Fore.RED + "Test get all flights and seats usecase failed: " + get_all_flights_and_seats_response.message + Style.RESET_ALL)