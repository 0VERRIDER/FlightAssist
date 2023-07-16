from core.usecase.usecase import request, response, error
from core.entity.booking import Booking

# Request
class AddBookingRequest(request):
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
                flight_price,
                booking_email = None,
                booking_phone = None,
                booking_name = None
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


# Response
class AddBookingResponse(response):
    def __init__(self, booking_id: str = None):
        self.booking_id = booking_id

# Error
class AddBookingError(error):
    def __init__(self, message: str):
        self.message = message

#Execute
class AddBookingUseCase:
    def __init__(self, booking_repository, request: AddBookingRequest):
        self.booking_repository = booking_repository
        self.request = request

    def execute(self):
        try:
            new_booking = Booking(
                self.request.booking_id,
                self.request.flight_id,
                self.request.booking_date,
                self.request.booking_status,
                self.request.booked_seats,
                self.request.booked_seats_type,
                self.request.flight_class,
                self.request.meal_preference,
                self.request.booking_email,
                self.request.booking_phone,
                self.request.booking_name,
                self.request.flight_price
            )
            booking_id = self.booking_repository.add_booking(new_booking)
            return AddBookingResponse(booking_id)
        except Exception as err:
            return AddBookingError(str(err))
        