from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.usecase.booking.set_meal_prefrence_by_booking_id_usecase import SetMealPreferenceByBookingIdUseCase, SetMealPreferenceByBookingIdRequest, SetMealPreferenceByBookingIdResponse, SetMealPreferenceByBookingIdError
from core.data.database.database_handler import DatabaseHandler as database_handler

class TestSetMealPreferenceByBookingIdUsecase:
            
            def __init__(self):
                database = database_handler("test.db")
                self.database_booking_repository = DatabaseBookingRepository(database)
        
            def test_set_meal_preference_by_booking_id(self):
                request = SetMealPreferenceByBookingIdRequest(booking_id=1, meal_preference="vegan")
                
                usecase = SetMealPreferenceByBookingIdUseCase(self.database_booking_repository, request)
                response = usecase.execute()
        
                if isinstance(response, SetMealPreferenceByBookingIdResponse):
                    return("Use cases test passed")
                elif isinstance(response, SetMealPreferenceByBookingIdError):
                    return("Use cases test failed: " + response.message)