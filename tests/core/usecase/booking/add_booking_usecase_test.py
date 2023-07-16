from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.usecase.booking.add_booking_usecase import AddBookingUseCase, AddBookingRequest, AddBookingResponse, AddBookingError
from core.utils.database_handler import DatabaseHandler as database_handler
from colorama import Fore, Style

class TestAddBookingUsecase:
    def test_add_booking(self):
        # Arrange
        database = database_handler("test.db")
        self.database_booking_repository = DatabaseBookingRepository(database)

        request = AddBookingRequest(
            booking_id = "1",
            flight_id = "A1234",
            booking_date = "2021-01-01",
            booking_status = "Confirmed",
            booked_seats = ["1A", "1B", "1C", "1D", "1E"],
            booked_seats_type = ["window", "aisle", "aisle", "aisle", "window"],
            flight_class = "Economy",
            meal_preference = "Vegetarian"
        )

        usecase = AddBookingUseCase(self.database_booking_repository, request)

        # Act
        response = usecase.execute()

        if isinstance(response, AddBookingResponse):
            return(Fore.GREEN + "Use cases test passed" + Style.RESET_ALL)
        elif isinstance(response, AddBookingError):
            return(Fore.RED + "Use cases test failed: " + response.message + Style.RESET_ALL)
        else:
            return(Fore.RED + "Use cases test failed: " + "Unknown Error"+ Style.RESET_ALL)

        
