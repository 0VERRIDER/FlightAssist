from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles 
from colorama import Fore, Style

class TestFileFlightRepository:
        
        def __init__(self):
            file = ReadFiles("./data_files/flight_data").read()
            self.file_flight_repository = FileFlightRepository(file)
        
        def test_get_all_flights(self):
            flights = self.file_flight_repository.get_all_flights()
            if len(flights) >= 1:
                return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
            else:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_flight(self):
            flight = self.file_flight_repository.get_flight("A411")
            if len(flight) == 1:
                return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
            else:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_flight_by_destination(self):
            flight = self.file_flight_repository.get_flight_by_destination("COIMBATORE")
            if len(flight) >= 1:
                return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL) 
            else:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_flight_by_origin(self):
            flight = self.file_flight_repository.get_flight_by_origin("CHENNAI")
            if len(flight) >= 1:
                return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
            else:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_flight_by_date(self):
            pass

        def test_get_flight_by_seats(self):
            pass

        def test_get_flight_by_destination_and_seats(self):
            pass

        def test_get_flight_seats_by_id(self):
            seats = self.file_flight_repository.get_flight_seats_by_id("A411")
            if len(seats) >= 1:
                return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
            else:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_all_flights_and_seats(self):
            flights_and_seats = self.file_flight_repository.get_all_flights_and_seats()
            if len(flights_and_seats) >= 1:
                return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
            else:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_flight_seats_by_id_and_type(self):
            seats = self.file_flight_repository.get_flight_seats_by_id_and_type("A411", "BUSINESS")
            if len(seats) >= 1:
                return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
            else:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_flight_types_by_id(self):
            types = self.file_flight_repository.get_flight_types_by_id("A411")
            if len(types) >= 1:
                return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
            else:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)



            




        
        