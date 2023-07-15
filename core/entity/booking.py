#class for booking entity
class Booking:
    def __init__(self, booking_id, flight_id, booking_date, booking_status, booked_seats, meal_preference):
        self.booking_id = booking_id
        self.flight_id = flight_id
        self.booking_date = booking_date
        self.booking_status = booking_status
        self.booked_seats = booked_seats #Booked seeats is a list of tuples
        self.meal_preference = meal_preference

    def __str__(self):
        return f'{self.booking_id} {self.flight_id} {self.booking_date} {self.booking_status} {self.booked_seats} {self.meal_preference}'
    