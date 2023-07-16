from core.usecase.flights.get_all_flight_usecase import GetAllFlightsUseCase, GetAllFlightsResponse, GetAllFlightsError, GetAllFlightsRequest
from core.data.files.file_flight_repository import FileFlightRepository
from core.utils.directory_reader import ReadFiles
from presentation.common import *
def list_all_flights():
    print_header()
    print_header("LIST ALL FLIGHTS")
    file = ReadFiles("./data_files/flight_data").read()
    file_flight_repository = FileFlightRepository(file)
    request = GetAllFlightsRequest()
    usecase = GetAllFlightsUseCase(file_flight_repository, request)
    response = usecase.execute()

    if isinstance(response, GetAllFlightsResponse):
        for i, flight in enumerate(response.flights):
            print(f"{i + 1}. {flight['flight_name']}")
        
        choice = input("\nSelect a flight or 0 to exit: ")
        if choice == "0":
            clear_terminal()
        else:
            clear_terminal()
            print(f"Flight {choice} selected")
            

    elif isinstance(response, GetAllFlightsError):
        print("Use cases test failed: " + response.message)