from core.repository.flight_repository import FlightRepository
from core.data.files.get_flight_data import get_flight_data

class FileFlightRepository(FlightRepository):
    def __init__(self, file):
        self.file = file

    def add_flight(self, flight):
        pass

    def get_flight(self, flight_id):
        flights = self.get_all_flights()
        flight = [item for item in flights if item.get("flight_id") == flight_id]
        return flight

    def get_all_flights(self):
        data = self.file
        flights = get_flight_data(data)
        return flights

    def update_flight(self, flight):
        pass

    def delete_flight(self, flight_id):
        pass

    def get_flight_by_destination(self, destination):
        flights = self.get_all_flights()
        flights_by_destination = [item for item in flights if item.get("destination") == destination ]
        return flights_by_destination

    def get_flight_by_origin(self, origin):
        flights = self.get_all_flights()
        flights_by_destination = [item for item in flights if item.get("source") == origin ]
        return flights_by_destination

    def get_flight_by_date(self, date):
        pass

    def get_flight_by_seats(self, seats):
        pass

    def get_flight_by_destination_and_seats(self, destination, seats):
        pass

    def get_flight_seats_by_id(self, flight_id):
        flight = self.get_flight(flight_id)[0]
        return flight["seat_details"]
    
    def get_all_flights_and_seats(self):
        flights = self.get_all_flights()
        flights_and_seats = [{"flight_id": item["flight_id"], "seat_details": item["seat_details"]} for item in flights]
        return flights_and_seats


    def get_flight_seats_by_id_and_type(self, flight_id, flight_type):
        flight = self.get_flight(flight_id)[0]
        return flight["seat_details"][flight_type]
        
    def update_flight_seats_by_id(self, flight_id, seats):
        pass

    def get_flight_types_by_id(self, flight_id):
        flight = self.get_flight(flight_id)[0]
        return list(flight["seat_details"].keys())

    def get_flight_by_type_and_seats(self, flight_type, seats):
        pass

    def get_flight_by_origin_and_destination(self, origin, destination):
        flights = self.get_all_flights()
        flights_by_origin_and_destination = [item for item in flights if item.get("source") == origin and item.get("destination") == destination ]
        return flights_by_origin_and_destination
    