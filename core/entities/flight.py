# class for flight entity
class Flight:
    def __init__(
            self, flight_id, 
            flight_name, 
            flight_source, 
            flight_destination, 
            flight_fare, 
            flight_status,
            seat_arrangement,
            available_seats
        ):
        
        self.flight_id = flight_id
        self.flight_name = flight_name
        self.flight_source = flight_source
        self.flight_destination = flight_destination
        self.flight_fare = flight_fare
        self.flight_status = flight_status
        self.seat_arrangement = seat_arrangement
        self.available_seats = available_seats

    def __str__(self):
        return f'{self.flight_id} {self.flight_name} {self.flight_source} {self.flight_destination} {self.flight_fare} {self.flight_status} {self.seat_arrangement} {self.available_seats}'
