def slice_list(original_list, pattern_list):
    sliced_list = []
    start_index = 0

    for slice_length in pattern_list:
        end_index = start_index + slice_length
        sliced_list.append(original_list[start_index:end_index])
        start_index = end_index

    return sliced_list

def get_seat_type_from_seat_arrangement(seat_arrangement):
  middle = []
  aisle = []
  window = [1]

  seat_row = [i for i in range(1,sum(seat_arrangement)+1)]
  window.extend([seat_row[-1]])
  seat_row = [i for i in seat_row if i not in window ]
  seat_arrangement[0] -= 1
  seat_arrangement[-1] -= 1

  seat_sections = slice_list(seat_row, seat_arrangement)

  for seats in seat_sections:
    if len(seats) > 0:
      aisle.append(seats[0])
      aisle.append(seats[-1])

      seats= [i for i in seats if i not in aisle ]
      
      for seat in seats:
        middle.append(seat)
  return (window,middle,aisle)


def get_seat_type_from_seat_number(seat_arrangement, seatnumbers):
    window, middle, aisle = get_seat_type_from_seat_arrangement(seat_arrangement)

    middle_set = set(middle)
    aisle_set = set(aisle)
    window_set = set(window)

    seat_types = ["M" if to_num(seatnumber[-1]) in middle_set
                  else "A" if to_num(seatnumber[-1]) in aisle_set
                  else "W" if to_num(seatnumber[-1]) in window_set
                  else "Invalid_seat"
                  for seatnumber in seatnumbers]

    return seat_types

def to_num(letter):
  return ord(letter) - 64

def generate_seat_structure(seat_structure, num_rows, booked_seats):
    booked_seats =   [f"{int(seat.split('_')[0]):02d}_{seat.split('_')[1]}" for seat in booked_seats]
    seat_list = []
    for row_num in range(num_rows):
        row_number = str(row_num + 1).zfill(2)  # Adjust row number to two digits
        row_letter = chr(ord('A') + row_num)
        seats = []
        seat_number = 1
        for num_seats in seat_structure:
            for _ in range(num_seats):
                column_letter = chr(ord('A') + (seat_number - 1))
                seat_label = f"{row_number}_{column_letter}"
                seats.append(seat_label)
                seat_number += 1
            seats.extend([''] * 2)
            seats = [seat if seat not in booked_seats else "XX_X" for seat in seats]  
        row = " ".join(seats)
        seat_list.append(row)
    return seat_list
