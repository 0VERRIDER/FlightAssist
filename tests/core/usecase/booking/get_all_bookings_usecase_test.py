from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.usecase.booking.get_all_bookings_usecase import GetAllBookingsUseCase, GetAllBookingsRequest, GetAllBookingsResponse, GetAllBookingsError
from core.utils.database_handler import DatabaseHandler as database_handler
from colorama import Fore, Style

class TestGetAllBookingsUsecase:
    
        def __init__(self):
            database = database_handler("test.db")
            self.database_booking_repository = DatabaseBookingRepository(database)
    
        def test_get_all_bookings(self):
            request = GetAllBookingsRequest()
            
            usecase = GetAllBookingsUseCase(self.database_booking_repository, request)
            response = usecase.execute()
    
            if isinstance(response, GetAllBookingsResponse):
                return(Fore.GREEN + "Use cases test passed" + Style.RESET_ALL)
            elif isinstance(response, GetAllBookingsError):
                return(Fore.RED + "Use cases test failed: " + response.message + Style.RESET_ALL)
