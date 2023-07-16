from core.usecase.flights.get_flight_by_destination_and_origin_usecase import GetFlightByDestinationAndOriginUseCase, GetFlightByDestinationAndOriginRequest, GetFlightByDestinationAndOriginResponse, GetFlightByDestinationAndOriginError
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from presentation.common import *
def search_flight():
    print_header()
    print_header("SEARCH FLIGHTS")
    file = ReadFiles("./data_files/flight_data").read()
    file_flight_repository = FileFlightRepository(file)

    source = input("Enter source: ").upper()
    destination = input("Enter destination: ").upper()

    request = GetFlightByDestinationAndOriginRequest(destination, source)
    usecase = GetFlightByDestinationAndOriginUseCase(file_flight_repository, request)
    response = usecase.execute()

    if isinstance(response, GetFlightByDestinationAndOriginResponse):
        for i, flight in enumerate(response.flights):
            print(f"{i + 1}. {flight['flight_name']}")
        
        choice = input("\nSelect a flight or 0 to exit: ")
        if choice == "0":
            clear_terminal()
        elif choice.isnumeric() and choice <= len(response.flights) + 1:
            clear_terminal()
            print(f"Flight {choice} selected")
            

    elif isinstance(response, GetFlightByDestinationAndOriginError):
        print("Use cases test failed: " + response.message)