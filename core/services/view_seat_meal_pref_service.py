from core.usecase.booking.get_flight_by_flight_id_and_flight_class_usecase import GetFlightByFlightIdAndFlightClassUseCase, GetFlightByFlightIdAndFlightClassRequest, GetFlightByFlightIdAndFlightClassResponse, GetFlightByFlightIdAndFlightClassError

class ViewSeatMealPrefService:
    def __init__(self, booking_repository):
        self.booking_repository = booking_repository

    def get_seat_meal_pref(self, flight_id, flight_class):
        try:
            get_seat_meal_pref_request = GetFlightByFlightIdAndFlightClassRequest(flight_id, flight_class)
            get_seat_meal_pref_usecase = GetFlightByFlightIdAndFlightClassUseCase(self.booking_repository, get_seat_meal_pref_request)
            get_seat_meal_pref_response = get_seat_meal_pref_usecase.execute()
            flights= []

            if isinstance(get_seat_meal_pref_response, GetFlightByFlightIdAndFlightClassResponse):
                flights = get_seat_meal_pref_response.flight
            elif isinstance(get_seat_meal_pref_response, GetFlightByFlightIdAndFlightClassError):
                raise Exception("Error" + get_seat_meal_pref_response.message)

            print(flights)
        except Exception as err:
            raise Exception("Error" + str(err))