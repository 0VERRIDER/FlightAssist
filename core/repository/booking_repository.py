from abc import abstractmethod,ABC
from core.entity.booking import Booking

# interface for BookingRepository
class BookingRepository(ABC):

    @abstractmethod
    def add_flight(self, flight):
        pass

    @abstractmethod
    def get_flight(self, flight_id):
        pass
    
    @abstractmethod
    def get_all_flights(self):
        pass
    
    @abstractmethod
    def update_flight(self, flight):
        pass
    
    @abstractmethod
    def delete_flight(self, flight_id):
        pass

    @abstractmethod
    def get_flight_by_destination(self, destination):
        pass
    
    @abstractmethod
    def get_flight_by_origin(self, origin):
        pass
    
    @abstractmethod
    def get_flight_by_date(self, date):
        pass

    @abstractmethod
    def get_flight_by_seats(self, seats):
        pass

    @abstractmethod
    def get_flight_by_destination_and_seats(self, destination, seats):
        pass

    @abstractmethod
    def get_flight_seats_by_id(self, flight_id):
        pass
    
    @abstractmethod 
    def get_all_flights_and_seats(self):
        pass

    @abstractmethod
    def get_flight_seats_by_id_and_type(self, flight_id, flight_type):
        pass
        
    @abstractmethod
    def update_flight_seats_by_id(self, flight_id, seats):
        pass

    @abstractmethod
    def get_flight_types_by_id(self, flight_id, flight_type):
        pass

    @abstractmethod
    def get_flight_by_type_and_seats(self, flight_type, seats):
        pass