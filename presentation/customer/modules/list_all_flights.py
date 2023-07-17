from core.usecase.flights.get_all_flight_usecase import GetAllFlightsUseCase, GetAllFlightsResponse, GetAllFlightsError, GetAllFlightsRequest
from presentation.common import *
from presentation.customer.modules.book_flight import book_flight
def list_all_flights(booking_repository, flight_repository):
    print_header()
    print_header("LIST ALL FLIGHTS")
    request = GetAllFlightsRequest()
    usecase = GetAllFlightsUseCase(flight_repository, request)
    response = usecase.execute()

    if isinstance(response, GetAllFlightsResponse):
        for i, flight in enumerate(response.flights):
            print(f"{i + 1}. {flight['flight_name']}")
        
        choice = input("\nSelect a flight to book or 0 to exit: ")
        if choice == "0":
            clear_terminal()
        else:
            clear_terminal()
            book_flight(booking_repository, flight_repository, response.flights[int(choice) - 1])
            

    elif isinstance(response, GetAllFlightsError):
        print("Use cases test failed: " + response.message)