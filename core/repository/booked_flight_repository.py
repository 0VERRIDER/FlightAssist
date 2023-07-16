#  Inteface for booked flight repository
from abc import ABC, abstractmethod

class BookedFlightRepository(ABC):

    @abstractmethod
    def add_booked_flight(self, booked_flight):
        pass

    @abstractmethod
    def get_all_booked_flights(self):
        pass

    @abstractmethod
    def update_booked_flight(self, booked_flight):
        pass

    @abstractmethod
    def delete_booked_flight(self, booked_flight_id):
        pass

    @abstractmethod
    def get_booked_flight_by_flight_id(self, flight_id):
        pass
