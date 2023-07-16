from core.usecase.flights.get_flight_usecase import GetFlightUseCase, GetFlightRequest, GetFlightResponse, GetFlightError
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from colorama import Fore, Style

class TestGetFlightUseCase:
    def test_get_flight_usecase(self):
        file = ReadFiles("./data_files/flight_data_test").read()
        file_flight_repository = FileFlightRepository(file)

        get_flight_request = GetFlightRequest("A411")
        get_flight_usecase = GetFlightUseCase(file_flight_repository, get_flight_request)
        get_flight_response = get_flight_usecase.execute()

        if isinstance(get_flight_response, GetFlightResponse):
            return(Fore.GREEN + "Test get flight usecase passed" + Style.RESET_ALL)
        elif isinstance(get_flight_response, GetFlightError):
            return(Fore.RED + "Test get flight usecase failed: " + get_flight_response.message + Style.RESET_ALL)