import sys

sys.path.append('/core/')
sys.path.append('/test/')

from test.core.data.database.database_booking_repository_test import TestDatabaseBookingRepository

test_database_booking_repository = TestDatabaseBookingRepository()
test_database_booking_repository.setup_method()
test_database_booking_repository.test_get_meal_preference_by_booking_id()



