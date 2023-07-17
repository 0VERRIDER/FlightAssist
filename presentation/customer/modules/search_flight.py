from core.usecase.flights.get_flight_by_destination_and_origin_usecase import GetFlightByDestinationAndOriginUseCase, GetFlightByDestinationAndOriginRequest, GetFlightByDestinationAndOriginResponse, GetFlightByDestinationAndOriginError
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from presentation.customer.modules.book_flight import book_flight

from presentation.common import *
def search_flight(booking_repository, flight_repository):
    print_header()
    print_header("SEARCH FLIGHTS")

    source = input("Enter source: ").upper()
    destination = input("Enter destination: ").upper()

    request = GetFlightByDestinationAndOriginRequest(source, destination)
    usecase = GetFlightByDestinationAndOriginUseCase(flight_repository, request)
    response = usecase.execute()

    print_header(source + " to " + destination + " flights")

    if isinstance(response, GetFlightByDestinationAndOriginResponse):
        for i, flight in enumerate(response.flights):
            print(f"{i + 1}. {flight['flight_name']}")
        
        choice = input("\nSelect a flight to book or 0 to exit: ")
        if choice == "0":
            clear_terminal()
        elif int(choice) <= len(response.flights) + 1:
            clear_terminal()
            book_flight(booking_repository, flight_repository, response.flights[int(choice) - 1])

        else:
            print("Invalid Choice")
            search_flight()
            

    elif isinstance(response, GetFlightByDestinationAndOriginError):
        print("Use cases test failed: " + response.message)