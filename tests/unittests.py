from tests.core.usecase.booking.tests import TestBookingUsecases
from tests.core.data.database.tests import TestDatabaseBookingRepository
from tests.core.data.files.tests import TestFileFlightRepository
from tests.core.usecase.flights.tests import TestFlightUseCases

import os

def run_tests():

    TestDatabaseBookingRepository().run()
    TestBookingUsecases().run()
    TestFileFlightRepository().run()
    TestFlightUseCases().run()
    os.remove("test.db")
