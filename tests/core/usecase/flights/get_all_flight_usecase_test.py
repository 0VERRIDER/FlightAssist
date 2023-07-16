from core.usecase.flights.get_all_flight_usecase import GetAllFlightsUseCase, GetAllFlightsResponse, GetAllFlightsError, GetAllFlightsRequest
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from colorama import Fore, Style

class TestGetAllFlightUseCase:
    def test_get_all_flight_usecase(self):
        file = ReadFiles("./data_files/flight_data_test").read()
        file_flight_repository = FileFlightRepository(file)

        get_all_flight_request = GetAllFlightsRequest()

        get_all_flight_usecase = GetAllFlightsUseCase(file_flight_repository, get_all_flight_request)
        get_all_flight_response = get_all_flight_usecase.execute()

        if isinstance(get_all_flight_response, GetAllFlightsResponse):
            return(Fore.GREEN + "Test get all flight usecase passed" + Style.RESET_ALL)
        elif isinstance(get_all_flight_response, GetAllFlightsError):
            return(Fore.RED + "Test get all flight usecase failed: " + get_all_flight_response.message + Style.RESET_ALL)

        
        