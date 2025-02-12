from registry import Registry

# Coding Exercise Part 1:
#
# The DVLA has a system for keeping track of vehicle registration numbers, any vehicle they are associated with and the year the registration was created.
# A registration can be not assigned to a vehicle, but is still associated with a year.
#
# Create a suitable in memory object/structure to store such data and populate this with the data from the provided sheet.
#
# Feature 1:
#
# Return the total number of registration numbers.

# Feature 2:

# Return the vehicle ID for a given registration number.


# Plan:
#
# create a dictionary to link a registration number to an inner dictionary
# the inner dictionary contains the year and optionally the vehicle id (does the vehicle ID always exist and link to an empty string, or does it only exist as a key once added?)
#
# to implement the base feature we need 2 functions, 
#     1 to create a registration and add a year (and optional argument to add vehicle id), 
#     the second to add a vehicle id to said registration
#
# feature 1 then can just return the length of the dictionary
# feature 2 then can use the registration number to find an appropriate inner 

if __name__ == "__main__":

    vehicleRegistry = Registry()

    vehicleRegistry.addNewRegistration("AB01 CDE", "2001")
    vehicleRegistry.addNewRegistration("FG02 HJK", "2002")
    vehicleRegistry.addNewRegistration("L33T H4X0R", "2022")

    vehicleRegistry.addIDToRegistration("AB01 CDE", "12345")
    vehicleRegistry.addIDToRegistration("FG02 HJK", "67890")

    print(vehicleRegistry.registry)
    
