from core.usecase.usecase import request, response, error

# Request
class GetMealPreferenceByBookingIdRequest(request):
    def __init__(self, booking_id: int):
        self.booking_id = booking_id

# Response
class GetMealPreferenceByBookingIdResponse(response):
    def __init__(self, meal_preference: str):
        self.meal_preference = meal_preference

# Error
class GetMealPreferenceByBookingIdError(error):
    def __init__(self, message: str):
        self.message = message

# Execute
class GetMealPreferenceByBookingIdUseCase:
    def __init__(self, booking_repository, request: GetMealPreferenceByBookingIdRequest):
        self.booking_repository = booking_repository
        self.request = request

    def execute(self):
        try:
            meal_preference = self.booking_repository.get_meal_preference_by_booking_id(self.request.booking_id)
            return GetMealPreferenceByBookingIdResponse(meal_preference)
        except Exception as err:
            return GetMealPreferenceByBookingIdError(str(err))
