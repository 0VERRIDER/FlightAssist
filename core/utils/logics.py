def mark_seat(seat_structure, seat_number):
    total_seats_in_row = sum(seat_structure)

    # Check if the seat number is within the valid range
    if seat_number < 1 or seat_number > total_seats_in_row:
        return "Invalid seat number"

    # Calculate the row number and column index of the seat
    row_number = (seat_number - 1) // total_seats_in_row + 1
    column_index = (seat_number - 1) % total_seats_in_row

    # Determine the seat type based on its position
    if column_index < seat_structure[0]:
        seat_type = "Window"
    elif column_index < seat_structure[0] + seat_structure[1]:
        seat_type = "Middle"
    else:
        seat_type = "Aisle"

    # Return the seat type and row number
    return seat_type, row_number
