from core.usecase.usecase import request, response, error

# Request
class GetAllBookingsRequest(request):
    def __init__(self):
        pass

# Response
class GetAllBookingsResponse(response):
    def __init__(self, bookings: list):
        self.bookings = bookings

# Error
class GetAllBookingsError(error):
    def __init__(self, message: str):
        self.message = message

# Execute
class GetAllBookingsUseCase:
    def __init__(self, booking_repository, request: GetAllBookingsRequest):
        self.booking_repository = booking_repository
        self.request = request

    def execute(self):
        try:
            bookings = self.booking_repository.get_all_bookings()
            return GetAllBookingsResponse(bookings)
        except Exception as err:
            return GetAllBookingsError(str(err))