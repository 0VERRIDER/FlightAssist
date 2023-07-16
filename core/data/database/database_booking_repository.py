from core.repository.booking_repository import BookingRepository
from core.entity.booking import Booking
from core.utils.database_handler import DatabaseHandler

class DatabaseBookingRepository(BookingRepository):

    def __init__(self, database: DatabaseHandler):
        self.database = database
        self.table_name = "booking"


    def add_booking(self, booking: Booking):
            with self.database:
                columns = list(booking.__dict__.keys())[1:]
                values = list(booking.__dict__.values())[1:]
                self.database.insert(table_name=self.table_name, columns=columns, values=values)

    def get_booking(self, booking_id):
            with self.database:
                booking = self.database.select(table_name=self.table_name, columns=["*"], where="booking_id = '" + str(booking_id) + "'")
                return booking

    def get_meal_preference_by_booking_id(self, booking_id):
            with self.database:
                meal_preference = self.database.select(table_name=self.table_name, columns=["meal_preference"], where="booking_id = '" + str(booking_id) + "'")
                return meal_preference

    def set_meal_preference_by_booking_id(self, booking_id, meal_preference):
            with self.database:
                self.database.update(table_name=self.table_name, columns=["meal_preference"], values=[meal_preference], where="booking_id = '" + str(booking_id) + "'")

    def get_all_bookings(self):
            with self.database:
                bookings = self.database.select(table_name=self.table_name, columns=["*"])
                return bookings

    def update_booking(self, booking: Booking):
            with self.database:
                columns = list(booking.__dict__.keys())[1:]
                values = list(booking.__dict__.values())[1:]
                self.database.update(table_name=self.table_name, columns=columns, values=values, where="booking_id = '" + str(booking.booking_id) + "'")

    def delete_booking(self, booking_id):
        try:
            with self.database:
                self.database.delete(table_name=self.table_name, where="booking_id = '" + str(booking_id) + "'")
        except Exception as e:
            return e
