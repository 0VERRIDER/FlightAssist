import tests.core.usecase.booking.add_booking_usecase_test as add_booking_usecase_test
import tests.core.usecase.booking.delete_booking_usecase_test as delete_booking_usecase_test
import tests.core.usecase.booking.get_booking_usecase_test as get_booking_usecase_test
import tests.core.usecase.booking.get_all_bookings_usecase_test as get_all_bookings_usecase_test
import tests.core.usecase.booking.get_meal_preference_by_booking_id_usecase_test as get_meal_preference_by_booking_id_usecase_test
import tests.core.usecase.booking.set_meal_preference_by_booking_id_usecase_test as set_meal_preference_by_booking_id_usecase_test
import tests.core.usecase.booking.update_booking_usecase_test as update_booking_usecase_test
from colorama import Fore, Back, Style

class TestBookingUsecases:
    def __init__(self):
        pass
    def run(self):
        print(Fore.BLACK)
        print(Back.WHITE + "Running tests for Booking Usecases" + Style.RESET_ALL + "\n")
        print("Add Booking Usecase : " + add_booking_usecase_test.TestAddBookingUsecase.test_add_booking(self))
        print("Get Booking Usecase : " + get_booking_usecase_test.TestGetBookingUsecase.test_get_booking(self))
        print("Get All Bookings Usecase : " + get_all_bookings_usecase_test.TestGetAllBookingsUsecase.test_get_all_bookings(self))
        print("Get Meal Preference By Booking Id Usecase : " + get_meal_preference_by_booking_id_usecase_test.TestGetMealPreferenceByBookingIdUsecase.test_get_meal_preference_by_booking_id(self))
        print("Set Meal Preference By Booking Id Usecase : " + set_meal_preference_by_booking_id_usecase_test.TestSetMealPreferenceByBookingIdUsecase.test_set_meal_preference_by_booking_id(self))
        print("Update Booking Usecase : " + update_booking_usecase_test.TestUpdateBookingUsecase.test_update_booking(self))
        print("Delete Booking Usecase : " + delete_booking_usecase_test.TestDeleteBookingUsecase.test_delete_booking(self))
        print("Usecase Tests completed. \n")