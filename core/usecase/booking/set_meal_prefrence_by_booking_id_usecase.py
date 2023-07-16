from core.usecase.usecase import request, response, error

# Request
class SetMealPreferenceByBookingIdRequest(request):
    def __init__(self, booking_id: int, meal_preference: str):
        self.booking_id = booking_id
        self.meal_preference = meal_preference

# Response
class SetMealPreferenceByBookingIdResponse(response):
    def __init__(self):
        pass

# Error
class SetMealPreferenceByBookingIdError(error):
    def __init__(self, message: str):
        self.message = message

# Execute
class SetMealPreferenceByBookingIdUseCase:
    def __init__(self, booking_repository, request: SetMealPreferenceByBookingIdRequest):
        self.booking_repository = booking_repository
        self.request = request

    def execute(self):
        try:
            self.booking_repository.set_meal_preference_by_booking_id(self.request.booking_id, self.request.meal_preference)
            return SetMealPreferenceByBookingIdResponse()
        except Exception as err:
            return SetMealPreferenceByBookingIdError(str(err))