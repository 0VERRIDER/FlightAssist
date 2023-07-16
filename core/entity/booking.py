#class for booking entity
class Booking:
    def __init__(
            self, 
            booking_id, 
            flight_id, 
            booking_date, 
            booking_status, 
            booked_seats, 
            booked_seats_type, 
            flight_class, 
            meal_preference,
            booking_email = None,
            booking_phone = None,
            booking_name = None,
            flight_price = None
            ):
        
        self.booking_id = booking_id
        self.booking_email = booking_email
        self.booking_phone = booking_phone
        self.booking_name = booking_name
        self.flight_id = flight_id
        self.booking_date = booking_date
        self.booking_status = booking_status
        self.booked_seats = booked_seats
        self.booked_seats_type = booked_seats_type
        self.flight_class = flight_class
        self.meal_preference = meal_preference
        self.flight_price = flight_price
