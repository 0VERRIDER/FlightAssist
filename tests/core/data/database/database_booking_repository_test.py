from colorama import Fore, Style
from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.entity.booking import Booking
from core.utils.database_handler import DatabaseHandler as database_handler


class DatabaseBookingRepositoryTest:
        def __init__(self):
            database = database_handler("test.db")
            self.database_booking_repository = DatabaseBookingRepository(database)
            self.test_booking = Booking(
                                booking_id = 1,
                                flight_id = "A1234",
                                booking_date = "2021-01-01",
                                booking_status = "Confirmed",
                                booked_seats = ["1A", "1B", "1C", "1D", "1E"],
                                booked_seats_type = ["window", "aisle", "aisle", "aisle", "window"],
                                flight_class = "Economy",
                                meal_preference = "Vegetarian"
                 )
            with database:
                database.create_table(
                            table_name="booking", 
                            columns=[
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
                                    ("meal_preference", "TEXT")
                                    ])
                    
        def test_add_booking(self):
            try:
                self.database_booking_repository.add_booking(
                    booking = self.test_booking
                )
                return(Fore.GREEN + "Repository Test passed" + Style.RESET_ALL)
            except Exception as e:
                return(Fore.RED + "Repository Test failed: " + str(e) + Style.RESET_ALL)

        def test_get_booking(self):
            try:
                data = self.database_booking_repository.get_booking(booking_id = 1)
                return(Fore.GREEN + "Repository Test passed" + Style.RESET_ALL)
            except Exception as e:
                return(Fore.RED + "Repository Test failed: " + str(e) + Style.RESET_ALL)
    
        def test_get_meal_preference_by_booking_id(self):
            try:
                data = self.database_booking_repository.get_meal_preference_by_booking_id(booking_id = 1)
                return(Fore.GREEN + "Repository Test passed" + Style.RESET_ALL)
            except Exception as e:
                return(Fore.RED + "Repository Test failed: " + str(e) + Style.RESET_ALL)
    
        def test_set_meal_preference_by_booking_id(self):
            try:
                self.database_booking_repository.set_meal_preference_by_booking_id(booking_id = 1, meal_preference = "Non-Vegetarian")
                return(Fore.GREEN + "Repository Test passed" + Style.RESET_ALL)
            except Exception as e:
                return(Fore.RED + "Repository Test failed: " + str(e) + Style.RESET_ALL)
    
        def test_get_all_bookings(self):
            try:
                data = self.database_booking_repository.get_all_bookings()
                return(Fore.GREEN + "Repository Test passed" + Style.RESET_ALL)
            except Exception as e:
                return(Fore.RED + "Repository Test failed: " + str(e) + Style.RESET_ALL)
    
        def test_update_booking(self):
            try:
                self.test_booking.booking_status = "Cancelled"
                self.database_booking_repository.update_booking(booking = self.test_booking)
                return(Fore.GREEN + "Repository Test passed" + Style.RESET_ALL)
            except Exception as e:
                return(Fore.RED + "Repository Test failed: " + str(e) + Style.RESET_ALL)
    
        def test_delete_booking(self):
            try:
                self.database_booking_repository.delete_booking(booking_id = 1)
                return(Fore.GREEN + "Repository Test passed" + Style.RESET_ALL)
            except Exception as e:
                return(Fore.RED + "Repository Test failed: " + str(e) + Style.RESET_ALL)
