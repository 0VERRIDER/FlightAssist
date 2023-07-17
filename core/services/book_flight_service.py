from core.usecase.booking.add_booking_usecase import AddBookingUseCase, AddBookingRequest, AddBookingResponse, AddBookingError
from core.usecase.booking.get_flight_by_flight_id_and_flight_class_usecase import GetFlightByFlightIdAndFlightClassUseCase, GetFlightByFlightIdAndFlightClassRequest, GetFlightByFlightIdAndFlightClassResponse, GetFlightByFlightIdAndFlightClassError
from core.utils.seat_util import get_seat_type_from_seat_number as get_seat_type
from core.usecase.flights.get_flight_seats_by_id_usecase import GetFlightSeatByIdUseCase, GetFlightSeatByIdRequest, GetFlightSeatByIdResponse, GetFlightSeatByIdError
from core.utils.string_utils import StringUtils

class BookFlightService:
    def __init__(self, booking_repository, flight_repository):
        self.booking_repository = booking_repository
        self.flight_repository = flight_repository

    def book_flight(
            self, 
            booking_id, 
            flight_id, 
            booking_date, 
            booking_status, 
            booked_seats, 
            flight_class, 
            meal_preference,
            booking_email = None,
            booking_phone = None,
            booking_name = None,
            ):
        try:
            # Count of bookings
            get_booked_flight_details = GetFlightByFlightIdAndFlightClassRequest(flight_id, flight_class)
            get_booked_flight_details_usecase = GetFlightByFlightIdAndFlightClassUseCase(self.booking_repository, get_booked_flight_details)
            get_booked_flight_details_response = get_booked_flight_details_usecase.execute()
            flights= []

            if isinstance(get_booked_flight_details_response, GetFlightByFlightIdAndFlightClassResponse):
                flights = get_booked_flight_details_response.flight
            elif isinstance(get_booked_flight_details_response, GetFlightByFlightIdAndFlightClassError):
                raise Exception("Booking Failed!" + get_booked_flight_details_response.message)

            #Get Seat Details
            get_flight_seats = GetFlightSeatByIdRequest(flight_id)
            get_flight_seats_usecase = GetFlightSeatByIdUseCase(self.flight_repository, get_flight_seats)
            get_flight_seats_response = get_flight_seats_usecase.execute()
            seats = {}

            if isinstance(get_flight_seats_response, GetFlightSeatByIdResponse):
                seats = get_flight_seats_response.flight_seat
            elif isinstance(get_flight_seats_response, GetFlightSeatByIdError):
                raise Exception("Booking Failed!" + get_flight_seats_response.message)

            
            total_booked_seats = []
            for booking in flights:
                booking =StringUtils(booking["booked_seats"]).to_list()
                total_booked_seats.extend(booking)

            # Check if seats are available
            if len(booked_seats) >= (seats[flight_class]["total_seats"] - len(total_booked_seats)):
                raise Exception("Booking Failed! No seats available")
            
            # check if the seats are already taken
            if total_booked_seats and set(booked_seats).intersection(total_booked_seats):
                raise Exception("Booking Failed! Seats already taken")
 


            seat_types = get_seat_type(seats[flight_class]["seat_arrangement"],booked_seats)

            # Calculate price
            increment = 0

            if flight_class == "ECONOMY":
                increment += 100 * len(booked_seats) * len(flights)
            elif flight_class == "BUSINESS":
                increment += 200 * len(booked_seats)* len(flights)

            if meal_preference != "None":
                increment += 200 * len(booked_seats)

            increment += (seat_types.count("A") + seat_types.count("W")) * 100

            base_flight_charge = 0
            if flight_class == "ECONOMY":
                base_flight_charge = 1000 * len(booked_seats)
            elif flight_class == "BUSINESS":
                base_flight_charge = 2000 * len(booked_seats)


            total_flight_price = base_flight_charge + increment

            # Add Booking
            add_booking_request = AddBookingRequest(
                booking_id = booking_id, 
                flight_id = flight_id, 
                booking_date = booking_date, 
                booking_status = booking_status, 
                booked_seats = booked_seats, 
                booked_seats_type= seat_types,
                flight_class = flight_class, 
                meal_preference = meal_preference,
                flight_price = total_flight_price
                )
            
            add_booking_usecase = AddBookingUseCase(self.booking_repository, add_booking_request)  
            add_booking_response = add_booking_usecase.execute()

            if isinstance(add_booking_response, AddBookingResponse):
                return (add_booking_response, total_flight_price)
            elif isinstance(add_booking_response, AddBookingError):
                return add_booking_response.message
            

        except Exception as err:
            return("Booking Failed!" + str(err))
        
        