from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles 
from colorama import Fore, Style

class FileFlightRepositoryTest:
        
        def __init__(self):
            file = ReadFiles("./data_files/flight_data_test").read()
            self.file_flight_repository = FileFlightRepository(file)
        
        def test_get_all_flights(self):
            try:
                flights = self.file_flight_repository.get_all_flights()
                if len(flights) >= 1:
                    return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
                else:
                    return(Fore.RED + "File flight repository test failed: No data" + Style.RESET_ALL)
            except:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
        
        def test_get_flight(self):
            try:
                flight = self.file_flight_repository.get_flight("A411")
                if flight:
                    return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
                else:
                    return(Fore.RED + "File flight repository test failed: No data" + Style.RESET_ALL)
            except:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_flight_by_destination(self):
            try:
                flight = self.file_flight_repository.get_flight_by_destination("BANGALORE")
                if len(flight) >= 1:
                    return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
                else:
                    return(Fore.RED + "File flight repository test failed: No data" + Style.RESET_ALL)
            except:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_flight_by_origin(self):
            try:
                flight = self.file_flight_repository.get_flight_by_origin("CHENNAI")
                if len(flight) >= 1:
                    return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
                else:
                    return(Fore.RED + "File flight repository test failed: No data" + Style.RESET_ALL)
            except:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_flight_by_date(self):
            pass

        def test_get_flight_by_seats(self):
            pass

        def test_get_flight_by_destination_and_seats(self):
            pass

        def test_get_flight_seats_by_id(self):
            try:
                seats = self.file_flight_repository.get_flight_seats_by_id("A411")
                if len(seats) >= 1:
                    return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
                else:
                    return(Fore.RED + "File flight repository test failed: No data" + Style.RESET_ALL)
            except:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_all_flights_and_seats(self):
            try:
                flights = self.file_flight_repository.get_all_flights_and_seats()
                if len(flights) >= 1:
                    return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
                else:
                    return(Fore.RED + "File flight repository test failed: No data" + Style.RESET_ALL)
            except:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_flight_seats_by_id_and_type(self):
            try:
                seats = self.file_flight_repository.get_flight_seats_by_id_and_type("A411", "ECONOMY")
                if len(seats) >= 1:
                    return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
                else:
                    return(Fore.RED + "File flight repository test failed: No data" + Style.RESET_ALL)
            except:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)
            
        def test_get_flight_types_by_id(self):
            try:
                types = self.file_flight_repository.get_flight_types_by_id("A411")
                if len(types) >= 1:
                    return(Fore.GREEN + "File flight repository test passed" + Style.RESET_ALL)
                else:
                    return(Fore.RED + "File flight repository test failed: No data" + Style.RESET_ALL)
            except:
                return(Fore.RED + "File flight repository test failed" + Style.RESET_ALL)



            




        
        