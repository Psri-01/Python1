def format_address(address_string):
  # Declare variables
  house_number = ""
  street_name = ""
  # Separate the address string into parts
  address_string = address_string.split()
  # Traverse through the address parts
  for number in address_string:
    # Determine if the address part is the
    # house number or part of the street name
    if number.isdigit():
      house_number = number 
  # give street names in order with a space in between them
    else:
      street_name += number
      street_name += " "
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
