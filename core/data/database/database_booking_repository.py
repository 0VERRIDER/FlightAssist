from core.repository.booking_repository import BookingRepository
from core.entity.booking import Booking
from core.data.database.database_handler import DatabaseHandler

class DatabaseBookingRepository(BookingRepository):

    def __init__(self, database: DatabaseHandler):
        self.database = database
        self.table_name = "booking"

    # To add a booking to the database
    def add_booking(self, booking: Booking):
            with self.database:
                columns = list(booking.__dict__.keys())[1:]
                values = list(booking.__dict__.values())[1:]
                return self.database.insert(table_name=self.table_name, columns=columns, values=values)
    
    # To get a booking from the database
    def get_booking(self, booking_id):
            with self.database:
                booking = self.database.select(table_name=self.table_name, columns=["*"], where="booking_id = '" + str(booking_id) + "'")
                return booking

    # To get meal prefrence alone by booking id from the database
    def get_meal_preference_by_booking_id(self, booking_id):
            with self.database:
                meal_preference = self.database.select(table_name=self.table_name, columns=["meal_preference"], where="booking_id = '" + str(booking_id) + "'")
                return meal_preference

    # To set meal prefrence by booking id from the database
    def set_meal_preference_by_booking_id(self, booking_id, meal_preference):
            with self.database:
                self.database.update(table_name=self.table_name, columns=["meal_preference"], values=[meal_preference], where="booking_id = '" + str(booking_id) + "'")

    #  To get all bookings from the database           
    def get_all_bookings(self):
            with self.database:
                bookings = self.database.select(table_name=self.table_name, columns=["*"])
                return bookings

    # To update a booking in the database
    def update_booking(self, booking: Booking):
            with self.database:
                booking_dict = {k: v for k, v in booking.__dict__.items() if v}
                columns = list(booking_dict.keys())[1:]
                values = list(booking_dict.values())[1:]
                self.database.update(table_name=self.table_name, columns=columns, values=values, where="booking_id = '" + str(booking.booking_id) + "'")

    # To delete a booking from the database
    def delete_booking(self, booking_id):
        try:
            with self.database:
                self.database.delete(table_name=self.table_name, where="booking_id = '" + str(booking_id) + "'")
        except Exception as e:
            return e
        
    # get all flight details in the booking database by flight id and flight class
    def get_flight_by_flight_id_and_flight_class(self, flight_id, flight_class):
        try:
            with self.database:
                flight = self.database.select(table_name=self.table_name, columns=["booked_seats", "meal_preference"], where="flight_id = '" + str(flight_id) + "' AND flight_class = '" + str(flight_class) + "'")
                return flight
        except Exception as e:
            return e
        
