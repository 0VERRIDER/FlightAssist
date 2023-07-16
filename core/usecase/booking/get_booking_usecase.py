from core.usecase.usecase import request, response, error

# Request
class GetBookingRequest(request):
    def __init__(self, booking_id: int):
        self.booking_id = booking_id

# Response
class GetBookingResponse(response):
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

# Error
class GetBookingError(error):
    def __init__(self, message: str):
        self.message = message

# Execute
class GetBookingUseCase:
    def __init__(self, booking_repository, request: GetBookingRequest):
        self.booking_repository = booking_repository
        self.request = request

    def execute(self):
        try:
            booking = self.booking_repository.get_booking(self.request.booking_id)

            if booking == []:
                raise Exception("Booking not found")
            
            return GetBookingResponse(*booking[0])
            
        except Exception as err:
            return GetBookingError(str(err))