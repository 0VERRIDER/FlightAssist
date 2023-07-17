def get_flight_data(data):
  flights = []

  for file_name, content in data.items():
    flight_data = dict()
    file_name = file_name.split(".")[0]
    from_filename = file_name.split("-")
    flight_data["flight_id"] = from_filename[1]
    flight_data['flight_name'] = file_name
    flight_data['source'] = from_filename[2]
    flight_data['destination'] = from_filename[3]
    flight_data["seat_details"] ={}

    raw_data = content['data']

    for class_data in raw_data:
      extracted_data = dict()
      split_data = class_data.split(":")
      class_name = split_data[0].strip()
      nums, value = eval(split_data[1].strip().replace("{", "[").replace("}", "]"))
      seat_arrangement = nums
      num_of_rows = value

      extracted_data = {
          'seat_arrangement': seat_arrangement,
          'rows': num_of_rows,
          'total_seats': sum(seat_arrangement) * num_of_rows 
      }

      flight_data["seat_details"][class_name] = extracted_data
      flight_data["flight_status"] = "Confirmed"
    
    flights.append(flight_data)
  return flights

