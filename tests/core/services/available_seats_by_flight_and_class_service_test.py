from core.services.available_seats_by_flight_and_class_service import AvailableSeatsByFlightAndClassService
from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.data.files.file_flight_repository import FileFlightRepository
from core.data.database.database_handler import DatabaseHandler as database_handler
from core.utils.directory_reader import ReadFiles

class AvailableSeatsByFlightandClassServiceTest:
    def __init__(self):
        database = database_handler("test.db")
        database_booking_repository = DatabaseBookingRepository(database)
        files = ReadFiles("./data_files/flight_data_test").read()
        fileFlightRepository = FileFlightRepository(files)
        self.available_seats_by_flight_and_class_service = AvailableSeatsByFlightAndClassService(database_booking_repository, fileFlightRepository) 

    def test_available_seats_by_flight_and_class(self):
        flight_id = "A411"
        flight_class = "ECONOMY"
        response = self.available_seats_by_flight_and_class_service.get_available_seats_by_flight_and_class(flight_id, flight_class)
        return response