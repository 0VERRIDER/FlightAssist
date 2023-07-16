from tests.core.usecase.booking.tests import TestBookingUsecases
from tests.core.data.database.tests import TestDatabaseBookingRepository
import os

def run_tests():
    TestDatabaseBookingRepository().run()
    TestBookingUsecases().run()

    os.remove("test.db")