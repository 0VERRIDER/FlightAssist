from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.usecase.booking.update_booking_usecase import UpdateBookingUseCase, UpdateBookingRequest, UpdateBookingResponse, UpdateBookingError
from core.utils.database_handler import DatabaseHandler as database_handler
from colorama import Fore, Style

class TestUpdateBookingUsecase:
        
            def __init__(self):
                database = database_handler("test.db")
                self.database_booking_repository = DatabaseBookingRepository(database)
        
            def test_update_booking(self):
                request = UpdateBookingRequest(
                booking_id=1,
                flight_id=1,
                booking_date="2021-05-05",
                booking_status="Confirmed",
                booked_seats=1,
                booked_seats_type="Adult",
                flight_class=  "Economy",
                meal_preference="Vegan",
                booking_email="",
                booking_phone="",
                booking_name=""
                )
                
                usecase = UpdateBookingUseCase(self.database_booking_repository, request)
                response = usecase.execute()
        
                if isinstance(response, UpdateBookingResponse):
                    return(Fore.GREEN + "Use cases test passed" + Style.RESET_ALL)
                elif isinstance(response, UpdateBookingError):
                    return(Fore.RED + "Use cases test failed: " + response.message + Style.RESET_ALL)
