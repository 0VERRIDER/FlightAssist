from core.usecase.flights.get_flight_seats_by_id_usecase import GetFlightSeatByIdUseCase, GetFlightSeatByIdRequest, GetFlightSeatByIdResponse, GetFlightSeatByIdError
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from colorama import Fore, Style

class TestGetFlightSeatsByIdUseCase:
    def test_get_flight_seats_by_id_usecase(self):
        file = ReadFiles("./data_files/flight_data_test").read()
        file_flight_repository = FileFlightRepository(file)

        get_flight_seats_by_id_request = GetFlightSeatByIdRequest("A411")
        get_flight_seats_by_id_usecase = GetFlightSeatByIdUseCase(file_flight_repository, get_flight_seats_by_id_request)
        get_flight_seats_by_id_response = get_flight_seats_by_id_usecase.execute()

        if isinstance(get_flight_seats_by_id_response, GetFlightSeatByIdResponse):
            return(Fore.GREEN + "Test get flight seats by id usecase passed" + Style.RESET_ALL)
        elif isinstance(get_flight_seats_by_id_response, GetFlightSeatByIdError):
            return(Fore.RED + "Test get flight seats by id usecase failed: " + get_flight_seats_by_id_response.message + Style.RESET_ALL)