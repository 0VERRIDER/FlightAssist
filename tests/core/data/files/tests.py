from tests.core.data.files.file_flight_repository_test import FileFlightRepositoryTest
from colorama import Fore, Back, Style

class TestFileFlightRepository:
    
    def __init__(self):
        pass
    
    def run(self):
        test_unit = FileFlightRepositoryTest()
        
        print(Fore.BLACK)
        print(Back.WHITE + "Running tests for file_flight_repository" + Style.RESET_ALL + "\n")
        print("Get Flight : " + test_unit.test_get_flight())
        print("Get All Flights : " + test_unit.test_get_all_flights())
        print("Get Flight By Destination : " + test_unit.test_get_flight_by_destination())
        print("Get Flight By Origin : " + test_unit.test_get_flight_by_origin())
        print("Get Flight Seats By Id : " + test_unit.test_get_flight_seats_by_id())
        print("Get All Flights And Seats : " + test_unit.test_get_all_flights_and_seats())
        print("Get Flight Seats By Id And Type : " + test_unit.test_get_flight_seats_by_id_and_type())
        print("Get Flight By Source And Destination : " + test_unit.test_get_flight_by_origin_and_destination())
        print("Flight Repository Tests completed. \n")
