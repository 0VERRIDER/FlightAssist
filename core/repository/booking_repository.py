from abc import abstractmethod,ABC
from core.entity.booking import Booking

# interface for BookingRepository
class BookingRepository(ABC):

    @abstractmethod
    def add_booking(self, booking: Booking):
        pass

    @abstractmethod
    def get_booking(self, booking_id):
        pass

    @abstractmethod
    def get_meal_preference_by_booking_id(self, booking_id):
        pass

    @abstractmethod
    def set_meal_preference_by_booking_id(self, booking_id, meal_preference):
        pass

    @abstractmethod
    def get_all_bookings(self):
        pass

    @abstractmethod
    def update_booking(self, booking: Booking):
        pass

    @abstractmethod
    def delete_booking(self, booking_id):
        pass

    
