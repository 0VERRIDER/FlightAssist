from core.repository.booking_repository import BookingRepository
from core.entity.booking import Booking
from core.utils.database_handler import DatabaseHandler as database_handler

class DatabaseBookingRepository(BookingRepository):

    def __init__(self, database):
        self.database = database
        self.table_name = "booking"

    def __enter__(self):
        return database_handler(self.database)

    def add_booking(self, booking: Booking):
        try:
            with database_handler as db:
                db.insert(table_name=self.table_name, columns=booking.__dict__.keys(), values=booking.__dict__.values())
        except Exception as e:
            return e

    def get_booking(self, booking_id) -> Booking:
        try:
            with database_handler as db:
                booking = db.select(table_name=self.table_name, columns=["*"], where="booking_id = '" + booking_id + "'")
                return booking
        except Exception as e:
            return e

    def get_meal_preference_by_booking_id(self, booking_id):
        try:
            with database_handler as db:
                meal_preference = db.select(table_name=self.table_name, columns=["meal_preference"], where="booking_id = '" + booking_id + "'")
                return meal_preference
        except Exception as e:
            return e

    def set_meal_preference_by_booking_id(self, booking_id, meal_preference):
        try:
            with database_handler as db:
                db.update(table_name=self.table_name, columns=["meal_preference"], values=[meal_preference], where="booking_id = '" + booking_id + "'")
        except Exception as e:
            return e

    def get_all_bookings(self) -> list(Booking):
        try:
            with database_handler as db:
                bookings = db.select(table_name=self.table_name, columns=["*"])
                return bookings
        except Exception as e:
            return e

    def update_booking(self, booking: Booking):
        try:
            with database_handler as db:
                db.update(table_name=self.table_name, columns=booking.__dict__.keys(), values=booking.__dict__.values(), where="booking_id = '" + booking.booking_id + "'")
        except Exception as e:
            return e

    def delete_booking(self, booking_id):
        try:
            with database_handler as db:
                db.delete(table_name=self.table_name, where="booking_id = '" + booking_id + "'")
        except Exception as e:
            return e
