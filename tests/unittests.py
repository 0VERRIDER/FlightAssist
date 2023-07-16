from tests.core.usecase.booking.tests import TestBookingUsecases
from tests.core.data.database.tests import TestDatabaseBookingRepository
from tests.core.data.files.file_flight_repository_test import TestFileFlightRepository

import os

def run_tests():
    # TestDatabaseBookingRepository().run()
    # TestBookingUsecases().run()
    print(TestFileFlightRepository().test_get_flight_types_by_id())

    # os.remove("test.db")