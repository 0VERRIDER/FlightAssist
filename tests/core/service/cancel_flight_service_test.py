from core.services.cancel_flight_service import CancelFlightService
from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.data.database.database_handler import DatabaseHandler as database_handler

class CancelFlightServiceTest:
    def __init__(self):
        database = database_handler("test.db")
        database_booking_repository = DatabaseBookingRepository(database)
        self.cancel_flight_service = CancelFlightService(database_booking_repository)               

    def test_cancel_flight(self):
        booking_id = "0"
        flight_id = "A411"
        booking_date = "2021-04-01"
        booking_status = "Confirmed"
        seats_to_cancel = ["A5"]
        flight_class = "ECONOMY"
        meal_preference = "None"
        booking_email = ""
        booking_phone = ""
        booking_name = ""

        response = self.cancel_flight_service.cancel_flight(
            booking_id, 
            seats_to_cancel
        )
            
        return response