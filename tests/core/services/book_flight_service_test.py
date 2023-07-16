from core.services.book_flight_service import BookFlightService
from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.data.files.file_flight_repository import FileFlightRepository
from core.data.database.database_handler import DatabaseHandler as database_handler
from core.utils.directory_reader import ReadFiles

class BookFlightServiceTest():
    def __init__(self):
        database = database_handler("test.db")
        database_booking_repository = DatabaseBookingRepository(database)
        files = ReadFiles("./data_files/flight_data_test").read()
        fileFlightRepository = FileFlightRepository(files)
        self.book_flight_service = BookFlightService(database_booking_repository, fileFlightRepository)               
        with database:
                database.create_table(table_name="booking", columns=[
                        ("booking_id", "INTEGER", ["PRIMARY KEY", "AUTOINCREMENT"]),
                        ("booking_email", "TEXT"),
                        ("booking_phone", "TEXT"),
                        ("booking_name", "TEXT"),
                        ("flight_id", "TEXT"),
                        ("booking_date", "TEXT"),
                        ("booking_status", "TEXT"),
                        ("booked_seats", "TEXT"),
                        ("booked_seats_type", "TEXT"),
                        ("flight_class", "TEXT"),
                        ("meal_preference", "TEXT"),
                        ("flight_price", "TEXT")])

    def test_book_flight(self):
        booking_id = "B001"
        flight_id = "A411"
        booking_date = "2021-04-01"
        booking_status = "Confirmed"
        booked_seats = ["1_F","2_F"]
        flight_class = "ECONOMY"
        meal_preference = "None"
        booking_email = ""
        booking_phone = ""
        booking_name = ""

        response = self.book_flight_service.book_flight(
            booking_id, 
            flight_id, 
            booking_date, 
            booking_status, 
            booked_seats, 
            flight_class, 
            meal_preference,
            booking_email,
            booking_phone,
            booking_name,
            )
        
