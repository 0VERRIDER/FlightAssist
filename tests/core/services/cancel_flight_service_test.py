from core.services.cancel_flight_service import CancelFlightService
from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.data.database.database_handler import DatabaseHandler as database_handler
from core.utils.directory_reader import ReadFiles
from core.data.files.file_flight_repository import FileFlightRepository

class CancelFlightServiceTest:
    def __init__(self):
        database = database_handler("test.db")
        database_booking_repository = DatabaseBookingRepository(database)
        files = ReadFiles("./data_files/flight_data_test").read()
        fileFlightRepository = FileFlightRepository(files)    
        self.cancel_flight_service = CancelFlightService(database_booking_repository, fileFlightRepository)   
         

    def test_cancel_flight(self):
        booking_id = "2"
        flight_id = "A411"
        booking_date = "2021-04-01"
        booking_status = "Confirmed"
        seats_to_cancel = []
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