from core.usecase.flights.get_flight_by_destination_and_origin_usecase import GetFlightByDestinationAndOriginUseCase, GetFlightByDestinationAndOriginRequest, GetFlightByDestinationAndOriginResponse, GetFlightByDestinationAndOriginError
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from colorama import Fore, Style

class TestGetFlightByDestinationAndOriginUseCase:
    def test_get_flight_by_destination_and_origin_usecase(self):
        file = ReadFiles("./data_files/flight_data_test").read()
        file_flight_repository = FileFlightRepository(file)

        get_flight_by_destination_and_origin_request = GetFlightByDestinationAndOriginRequest("BANGLORE", "CHENNAI")
        get_flight_by_destination_and_origin_usecase = GetFlightByDestinationAndOriginUseCase(file_flight_repository, get_flight_by_destination_and_origin_request)
        get_flight_by_destination_and_origin_response = get_flight_by_destination_and_origin_usecase.execute()

        if isinstance(get_flight_by_destination_and_origin_response, GetFlightByDestinationAndOriginResponse):
            return(Fore.GREEN + "Test get flight by destination and origin usecase passed" + Style.RESET_ALL)   
        elif isinstance(get_flight_by_destination_and_origin_response, GetFlightByDestinationAndOriginError):
            return(Fore.RED + "Test get flight by destination and origin usecase failed: " + get_flight_by_destination_and_origin_response.message + Style.RESET_ALL)