from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.usecase.booking.get_meal_preference_by_booking_id_usecase import GetMealPreferenceByBookingIdUseCase, GetMealPreferenceByBookingIdRequest, GetMealPreferenceByBookingIdResponse, GetMealPreferenceByBookingIdError
from core.data.database.database_handler import DatabaseHandler as database_handler
from colorama import Fore, Style

class TestGetMealPreferenceByBookingIdUsecase:
        
            def __init__(self):
                database = database_handler("test.db")
                self.database_booking_repository = DatabaseBookingRepository(database)
        
            def test_get_meal_preference_by_booking_id(self):
                request = GetMealPreferenceByBookingIdRequest(booking_id=1)
                
                usecase = GetMealPreferenceByBookingIdUseCase(self.database_booking_repository, request)
                response = usecase.execute()
        
                if isinstance(response, GetMealPreferenceByBookingIdResponse):
                    return(Fore.GREEN + "Use cases test passed" + Style.RESET_ALL)
                elif isinstance(response, GetMealPreferenceByBookingIdError):
                    return(Fore.RED + "Use cases test failed: " + response.message + Style.RESET_ALL)