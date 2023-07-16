from core.usecase.booking.delete_booking_usecase import DeleteBookingUseCase, DeleteBookingRequest, DeleteBookingResponse, DeleteBookingError
from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.data.database.database_handler import DatabaseHandler as database_handler
from colorama import Fore, Style

class TestDeleteBookingUsecase:

    def __init__(self):
        database = database_handler("test.db")
        self.database_booking_repository = DatabaseBookingRepository(database)

    def test_delete_booking(self):
        request = DeleteBookingRequest(booking_id=1)
        
        usecase = DeleteBookingUseCase(self.database_booking_repository, request)
        response = usecase.execute()

        if isinstance(response, DeleteBookingResponse):
            return(Fore.GREEN + "Use cases test passed" + Style.RESET_ALL)
        elif isinstance(response, DeleteBookingError):
            return(Fore.RED + "Use cases test failed: " + response.message + Style.RESET_ALL)
