import sys
from core.data.database.database_handler import DatabaseHandler as database_handler
from presentation.intro import intro
from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.utils.directory_reader import ReadFiles
from core.data.files.file_flight_repository import FileFlightRepository

sys.path.append('/core/')
sys.path.append('/test/')
sys.path.append('/presentation/')

def setup(database):
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


if __name__ == '__main__':
    database = database_handler("booking.db")
    booking_repository = DatabaseBookingRepository(database)
    files = ReadFiles("./data_files/flight_data").read()
    flight_repository = FileFlightRepository(files)    
    from core.data.files.file_flight_repository import FileFlightRepository

    setup(database)
    while(True):
        intro.start(booking_repository, flight_repository)


