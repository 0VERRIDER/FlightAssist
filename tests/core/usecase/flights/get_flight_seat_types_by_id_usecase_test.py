from core.usecase.flights.get_flight_seat_types_by_id_usecase import GetFlightSeatTypesByIdUseCase, GetFlightSeatTypesByIdRequest, GetFlightSeatTypesByIdResponse, GetFlightSeatTypesByIdError
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from colorama import Fore, Style

class TestGetFlightSeatTypesByIdUseCase:
    def test_get_flight_seat_types_by_id_usecase(self):
        file = ReadFiles("./data_files/flight_data_test").read()
        file_flight_repository = FileFlightRepository(file)

        get_flight_seat_types_by_id_request = GetFlightSeatTypesByIdRequest("A411")
        get_flight_seat_types_by_id_usecase = GetFlightSeatTypesByIdUseCase(file_flight_repository, get_flight_seat_types_by_id_request)
        get_flight_seat_types_by_id_response = get_flight_seat_types_by_id_usecase.execute()

        if isinstance(get_flight_seat_types_by_id_response, GetFlightSeatTypesByIdResponse):
            return(Fore.GREEN + "Test get flight seat by id usecase passed" + Style.RESET_ALL)
        elif isinstance(get_flight_seat_types_by_id_response, GetFlightSeatTypesByIdError):
            return(Fore.RED + "Test get flight seat by id usecase failed: " + get_flight_seat_types_by_id_response.message + Style.RESET_ALL)