# class for flight entity
class Flight:
    def __init__(
            self, 
            flight_id, 
            flight_name, 
            flight_source, 
            flight_destination, 
            flight_fare, 
            flight_status,
            flight_type,
            seat_arrangement,
        ):
        
        self.flight_id = flight_id
        self.flight_name = flight_name
        self.flight_source = flight_source
        self.flight_destination = flight_destination
        self.flight_fare = flight_fare
        self.flight_status = flight_status
        self.flight_type = flight_type
        self.seat_arrangement = seat_arrangement

    def __str__(self):
        return f'{self.flight_id} {self.flight_name} {self.flight_source} {self.flight_destination} {self.flight_fare} {self.flight_status} {self.flight_type} {self.seat_arrangement} {self.available_seats}'
