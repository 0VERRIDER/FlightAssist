from core.services.view_seat_meal_pref_service import ViewSeatMealPrefService
from core.data.database.database_booking_repository import DatabaseBookingRepository
from core.data.database.database_handler import DatabaseHandler as database_handler

class ViewSeatMealPrefServiceTest:
    def __init__(self):
        database = database_handler("test.db")
        database_booking_repository = DatabaseBookingRepository(database)
        self.view_seat_meal_pref_service = ViewSeatMealPrefService(database_booking_repository)   
         

    def test_view_seat_meal_pref(self):
        response = self.view_seat_meal_pref_service.get_seat_meal_pref("A411", "ECONOMY")
        return response