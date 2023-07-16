from core.usecase.usecase import request, response, error
# Request
class DeleteBookingRequest(request):
    def __init__(self, booking_id: int):
        self.booking_id = booking_id

# Response
class DeleteBookingResponse(response):
    def __init__(self):
        pass

# Error
class DeleteBookingError(error):
    def __init__(self, message: str):
        self.message = message

# Execute
class DeleteBookingUseCase:
    def __init__(self, booking_repository, request: DeleteBookingRequest):
        self.booking_repository = booking_repository
        self.request = request

    def execute(self):
        try:
            self.booking_repository.delete_booking(self.request.booking_id)
            return DeleteBookingResponse()
        except Exception as err:
            return DeleteBookingError(str(err))