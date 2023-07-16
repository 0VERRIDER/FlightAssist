# calss for Booked Flight entity

class BookedFlight:
    def __init__(
            self, 
            booked_flight_id, 
            booked_flight_name, 
            booked_flight_source, 
            booked_flight_destination, 
            booked_flight_fare,
            booked_flight_status,
            booked_flight_type,
            booked_flight_seats
        ):
        
        self.booked_flight_id = booked_flight_id
        self.booked_flight_name = booked_flight_name
        self.booked_flight_source = booked_flight_source
        self.booked_flight_destination = booked_flight_destination
        self.booked_flight_fare = booked_flight_fare
        self.booked_flight_status = booked_flight_status
        self.booked_flight_type = booked_flight_type
        self.booked_flight_seats = booked_flight_seats