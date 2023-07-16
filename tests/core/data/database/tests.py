from tests.core.data.database.database_booking_repository_test import DatabaseBookingRepositoryTest

class TestDatabaseBookingRepository:
    def __init__(self):
        pass
    
    def run(self):
        test_unit = DatabaseBookingRepositoryTest()
        print("Running tests for database_booking_repository")
        print("Add Booking : " + test_unit.test_add_booking())
        print("Get Booking : " + test_unit.test_get_booking())
        print("Get Meal Preference By Booking Id : " + test_unit.test_get_meal_preference_by_booking_id())
        print("Set Meal Preference By Booking Id : " + test_unit.test_set_meal_preference_by_booking_id())
        print("Get All Bookings : " + test_unit.test_get_all_bookings())
        print("Update Booking : " + test_unit.test_update_booking())
        print("Delete Booking : " + test_unit.test_delete_booking())
        print("Booking Repository Tests completed. \n")