from core.usecase.booking.set_meal_prefrence_by_booking_id_usecase import SetMealPreferenceByBookingIdUseCase, SetMealPreferenceByBookingIdRequest, SetMealPreferenceByBookingIdResponse, SetMealPreferenceByBookingIdError
from presentation.common import *

def update_meal_preference(booking_repository):
    print_header()
    print_header("UPDATE MEAL PREFERENCE")
    booking_id = input("Enter the booking id: ")
    print("Select meal preference:")
    print("1. Veg")
    print("2. Non-Veg")
    print("3. None")

    meal_choice = input("Enter your choice: ")
    
    if meal_choice == "1":
        meal_preference = "VEG"
    elif meal_choice == "2":
        meal_preference = "NON-VEG"
    else:
        meal_preference = "None"

    set_meal_preference_by_booking_id_request = SetMealPreferenceByBookingIdRequest(booking_id, meal_preference)
    set_meal_preference_by_booking_id_usecase = SetMealPreferenceByBookingIdUseCase(booking_repository, set_meal_preference_by_booking_id_request)
    set_meal_preference_by_booking_id_response = set_meal_preference_by_booking_id_usecase.execute()
    if isinstance(set_meal_preference_by_booking_id_response, SetMealPreferenceByBookingIdResponse):
        print("Meal preference updated successfully")
    else:
        print("Meal preference updation failed")
    return