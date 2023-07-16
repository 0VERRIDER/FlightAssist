from tests.core.usecase.flights.get_all_flight_usecase_test import TestGetAllFlightUseCase
from tests.core.usecase.flights.get_all_flights_and_seats_usecase_test import TestGetAllFlightsAndSeatsUseCase
from tests.core.usecase.flights.get_flight_seat_types_by_id_usecase_test import TestGetFlightSeatTypesByIdUseCase
from tests.core.usecase.flights.get_flight_seats_by_id_and_type_usecase_test import TestGetFlightSeatsByIdAndTypeUseCase
from tests.core.usecase.flights.get_flight_seats_by_id_usecase_test import TestGetFlightSeatsByIdUseCase
from tests.core.usecase.flights.get_flight_usecase_test import TestGetFlightUseCase
from tests.core.usecase.flights.get_flights_by_destination_and_origin_usecase_test import TestGetFlightByDestinationAndOriginUseCase
from tests.core.usecase.flights.get_flights_by_origin_usecase_test import TestGetFlightByOriginUseCase
from tests.core.usecase.flights.get_flights_by_destination_usecase_test import TestGetFlightByDestinationUseCase
from colorama import Back, Fore, Style

class TestFlightUseCases:
    def run(self):
        print(Fore.BLACK)
        print(Back.WHITE + "Test flight usecases" + Style.RESET_ALL + "\n")
        print("Get All flight usecase :" + TestGetAllFlightUseCase().test_get_all_flight_usecase())
        print("Get all flights and seats usecase :" + TestGetAllFlightsAndSeatsUseCase().test_get_all_flights_and_seats_usecase())
        print("Get flight seat type by id usecase :" + TestGetFlightSeatTypesByIdUseCase().test_get_flight_seat_types_by_id_usecase())
        print("Get flight seats by id and type usecase :" + TestGetFlightSeatsByIdAndTypeUseCase().test_get_flight_seats_by_id_and_type_usecase())
        print("Get flight seats by id usecase :" + TestGetFlightSeatsByIdUseCase().test_get_flight_seats_by_id_usecase())
        print("Get flight usecase :" + TestGetFlightUseCase().test_get_flight_usecase())
        print("Get flight by origin and destination usecase :" + TestGetFlightByDestinationAndOriginUseCase().test_get_flight_by_destination_and_origin_usecase())
        print("Get flight by origin usecase :" + TestGetFlightByOriginUseCase().test_get_flight_by_origin_usecase())
        print("Get flight by destination usecase :" + TestGetFlightByDestinationUseCase().test_get_flight_by_destination_usecase())
        print("Test flight usecases passed\n") 