from tests.core.usecase.booking.tests import TestBookingUsecases
from tests.core.data.database.tests import TestDatabaseBookingRepository
from tests.core.data.files.tests import TestFileFlightRepository

import os

def run_tests():

    TestDatabaseBookingRepository().run()
    TestBookingUsecases().run()
    TestFileFlightRepository().run()
    os.remove("test.db")
