from core.usecase.usecase import request, response, error

# Request
class GetBookingRequest(request):
    def __init__(self, booking_id: int):
        self.booking_id = booking_id

# Response
class GetBookingResponse(response):
     def __init__(self, booking):
        self.booking = booking

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

            if len(booking) == 0:
                raise Exception("Booking not found")
            
            return GetBookingResponse(booking[0])
            
        except Exception as err:
            return GetBookingError(str(err))