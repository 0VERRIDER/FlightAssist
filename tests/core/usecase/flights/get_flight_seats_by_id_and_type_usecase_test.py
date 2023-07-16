from core.usecase.flights.get_flight_seats_by_id_and_type_usecase import GetFlightSeatsByIdAndTypeUseCase, GetFlightSeatsByIdAndTypeRequest, GetFlightSeatsByIdAndTypeResponse, GetFlightSeatsByIdAndTypeError
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from colorama import Fore, Style

class TestGetFlightSeatsByIdAndTypeUseCase:
    def test_get_flight_seats_by_id_and_type_usecase(self):
        file = ReadFiles("./data_files/flight_data_test").read()
        file_flight_repository = FileFlightRepository(file)

        get_flight_seats_by_id_and_type_request = GetFlightSeatsByIdAndTypeRequest("A411", "BUSINESS")
        get_flight_seats_by_id_and_type_usecase = GetFlightSeatsByIdAndTypeUseCase(file_flight_repository, get_flight_seats_by_id_and_type_request)
        get_flight_seats_by_id_and_type_response = get_flight_seats_by_id_and_type_usecase.execute()

        if isinstance(get_flight_seats_by_id_and_type_response, GetFlightSeatsByIdAndTypeResponse):
            return(Fore.GREEN + "Test get flight seats by id and type usecase passed" + Style.RESET_ALL)
        elif isinstance(get_flight_seats_by_id_and_type_response, GetFlightSeatsByIdAndTypeError):
            return(Fore.RED + "Test get flight seats by id and type usecase failed: " + get_flight_seats_by_id_and_type_response.message + Style.RESET_ALL)