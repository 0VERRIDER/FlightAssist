from core.usecase.flights.get_flight_by_destination_usecase import GetFlightByDestinationUseCase, GetFlightByDestinationRequest, GetFlightByDestinationResponse, GetFlightByDestinationError
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from colorama import Fore, Style

class TestGetFlightByDestinationUseCase:
    def test_get_flight_by_destination_usecase(self):
        file = ReadFiles("./data_files/flight_data_test").read()
        file_flight_repository = FileFlightRepository(file)

        get_flight_by_destination_request = GetFlightByDestinationRequest("BANGLORE")
        get_flight_by_destination_usecase = GetFlightByDestinationUseCase(file_flight_repository, get_flight_by_destination_request)
        get_flight_by_destination_response = get_flight_by_destination_usecase.execute()

        if isinstance(get_flight_by_destination_response, GetFlightByDestinationResponse):
            return(Fore.GREEN + "Test get flight by destination usecase passed" + Style.RESET_ALL)
        elif isinstance(get_flight_by_destination_response, GetFlightByDestinationError):
            return(Fore.RED + "Test get flight by destination usecase failed: " + get_flight_by_destination_response.message + Style.RESET_ALL)
        