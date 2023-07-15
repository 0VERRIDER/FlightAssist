from core.repository.booking_repository import BookingRepository
from core.entity.booking import Booking

from core.utils.database_handler import DatabaseHandler

class DatabaseBookingRepository(BookingRepository):

    def __init__(self, database: DatabaseHandler):
        self.database = database
        self.table_name = "booking"


    def add_booking(self, booking: Booking):
        try:
            with self.database:
                columns = list(booking.__dict__.keys())
                values = list(booking.__dict__.values())
                self.database.insert(table_name=self.table_name, columns=columns, values=values)
                print("Booking added successfully" )

        except Exception as e:
            return e

    def get_booking(self, booking_id):
        try:
            with self.database:
                booking = self.database.select(table_name=self.table_name, columns=["*"], where="booking_id = '" + str(booking_id) + "'")
                return booking
        except Exception as e:
            return e

    def get_meal_preference_by_booking_id(self, booking_id):
        try:
            with self.database:
                meal_preference = self.database.select(table_name=self.table_name, columns=["meal_preference"], where="booking_id = '" + str(booking_id) + "'")
                return meal_preference
        except Exception as e:
            return e

    def set_meal_preference_by_booking_id(self, booking_id, meal_preference):
        try:
            with self.database:
                self.database.update(table_name=self.table_name, columns=["meal_preference"], values=[meal_preference], where="booking_id = '" + str(booking_id) + "'")
        except Exception as e:
            return e

    def get_all_bookings(self):
        try:
            with self.database:
                bookings = self.database.select(table_name=self.table_name, columns=["*"])
                return bookings
        except Exception as e:
            return e

    def update_booking(self, booking: Booking):
        try:
            with self.database:
                self.database.update(table_name=self.table_name, columns=booking.__dict__.keys(), values=booking.__dict__.values(), where="booking_id = '" + str(booking.booking_id) + "'")
        except Exception as e:
            return e

    def delete_booking(self, booking_id):
        try:
            with self.database:
                self.database.delete(table_name=self.table_name, where="booking_id = '" + str(booking_id) + "'")
        except Exception as e:
            return e
