from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.usecase.booking.get_booking_usecase import GetBookingUseCase, GetBookingRequest, GetBookingResponse, GetBookingError
from core.data.database.database_handler import DatabaseHandler as database_handler
from colorama import Fore, Style

class TestGetBookingUsecase:
        
            def __init__(self):
                database = database_handler("test.db")
                self.database_booking_repository = DatabaseBookingRepository(database)
        
            def test_get_booking(self):
                request = GetBookingRequest(booking_id=2)
                
                usecase = GetBookingUseCase(self.database_booking_repository, request)
                response = usecase.execute()
        
                if isinstance(response, GetBookingResponse):
                    return(Fore.GREEN + "Use cases test passed" + Style.RESET_ALL)
                elif isinstance(response, GetBookingError):
                    return(Fore.RED + "Use cases test failed: " + response.message + Style.RESET_ALL)