from core.usecase.flights.get_flight_by_origin_usecase import GetFlightByOriginUseCase, GetFlightByOriginRequest, GetFlightByOriginResponse, GetFlightByOriginError
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from colorama import Fore, Style

class TestGetFlightByOriginUseCase:
    def test_get_flight_by_origin_usecase(self):
        file = ReadFiles("./data_files/flight_data_test").read()
        file_flight_repository = FileFlightRepository(file)

        get_flight_by_origin_request = GetFlightByOriginRequest("CHENNAI")
        get_flight_by_origin_usecase = GetFlightByOriginUseCase(file_flight_repository, get_flight_by_origin_request)
        get_flight_by_origin_response = get_flight_by_origin_usecase.execute()

        if isinstance(get_flight_by_origin_response, GetFlightByOriginResponse):
            return(Fore.GREEN + "Test get flight by origin usecase passed" + Style.RESET_ALL)
        elif isinstance(get_flight_by_origin_response, GetFlightByOriginError):
            return(Fore.RED + "Test get flight by origin usecase failed: " + get_flight_by_origin_response.message + Style.RESET_ALL)