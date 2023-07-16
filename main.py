import sys
# import os

sys.path.append('/core/')
sys.path.append('/test/')
sys.path.append('/presentation/')


# import tests.unittests as unittests
# from tests.core.services.book_flight_service_test import BookFlightServiceTest
# from tests.core.services.cancel_flight_service_test import CancelFlightServiceTest
# from tests.core.services.view_seat_meal_pref_service_test import ViewSeatMealPrefServiceTest
# from tests.core.services.available_seats_by_flight_and_class_service_test import AvailableSeatsByFlightandClassServiceTest

# if __name__ == '__main__':
#     unittests.run_tests()
#     book_flight_service_test = BookFlightServiceTest()
#     book_flight_service_test.test_book_flight()
#     cancel_flight_service_test = CancelFlightServiceTest()
#     cancel_flight_service_test.test_cancel_flight()
#     view_seat_meal_pref_service_test = ViewSeatMealPrefServiceTest()
#     view_seat_meal_pref_service_test.test_view_seat_meal_pref()
#     available_seats_by_flight_and_class_service_test = AvailableSeatsByFlightandClassServiceTest()
#     available_seats_by_flight_and_class_service_test.test_available_seats_by_flight_and_class()
#     os.remove("./test.db")

from presentation.intro import intro

if __name__ == '__main__':
    while(True):
        intro.start()
