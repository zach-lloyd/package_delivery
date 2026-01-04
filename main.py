# Student ID: 012849717
# Name: Zach Lloyd

from import_packages import import_packages
from import_distances import import_distances
from load_trucks import load_trucks
from Truck import Truck
from print_final_information import print_final_information
from user_interface import user_interface
from CustomHashTable import CustomHashTable

PACKAGES_FILENAME = "WGUPS Package File.csv"
DISTANCES_FILENAME = "WGUPS Distance Table.csv"
CAPACITY = 16
MPH = 18

# Truck 1 will handle the package with a 9:00 AM deadline and will not be 
# loaded with any packages that are arriving late, so it leaves ASAP
TRUCK1_DEPARTURE_TIME = 800
# Truck 2 waits on all the packages that are delayed until 9:05 AM, then departs
# as soon as they arrive
TRUCK2_DEPARTURE_TIME = 905
# Because we only have 2 drivers, we don't know Truck 3's departure time at the
# start of the program. It will depend on which of Truck 1 or Truck 2 finishes
# it's deliveries first (probably Truck 1, but we don't want to assume that)
TRUCK3_DEPARTURE_TIME = None

def main():
    # Step 1: Initialize the hash table with one bucket for each package
    hash_table = CustomHashTable(40)

    # Step 2: Read the data from the packages and distances files
    packages = import_packages(PACKAGES_FILENAME, hash_table)
    distances = import_distances(DISTANCES_FILENAME)

    # Step 3: Create the truck objects. For this project, there are three trucks,
    # so we create three objects
    truck1 = Truck(CAPACITY, MPH)
    truck2 = Truck(CAPACITY, MPH)
    truck3 = Truck(CAPACITY, MPH)

    # Step 4: Load the packages onto the trucks and check for any packages that
    # weren't loaded
    overflow = load_trucks(packages, [truck1, truck2, truck3])

    if overflow:
        print(f"Warning: {len(overflow)} packages were not loaded!")

    # Step 5: Set Truck 1 and 2 departure times and deliver their packages
    truck1.set_departure_time(TRUCK1_DEPARTURE_TIME)
    truck2.set_departure_time(TRUCK2_DEPARTURE_TIME)
    truck1_return_time, truck1_miles_travelled = truck1.deliver_packages(distances)
    truck2_return_time, truck2_miles_travelled = truck2.deliver_packages(distances)

    # Step 6: Get Truck 3's departure time is based on whichever of the first 2
    # trucks got back first (keeping in mind that regardless of how quickly the
    # first two trucks arrive back, the third truck MUST wait until at least 10:20
    # to get the corrected address for Package 9)
    earliest_return_time = min(truck1_return_time, truck2_return_time)
    
    if earliest_return_time >= 1020:
        TRUCK3_DEPARTURE_TIME = earliest_return_time
    else:
        TRUCK3_DEPARTURE_TIME = 1020

    # Step 7: Set Truck 3's departure time and deliver its packages
    truck3.set_departure_time(TRUCK3_DEPARTURE_TIME)
    truck3_return_time, truck3_miles_travelled = truck3.deliver_packages(distances)

    # Step 8: Print the return times and miles travelled of each truck, the total
    # miles travelled, and the number of packages delivered on time, late, or not
    # delivered at all
    print_final_information(
        packages, 
        [truck1_return_time, truck2_return_time, truck3_return_time],
        [truck1_miles_travelled, truck2_miles_travelled, truck3_miles_travelled]
    )

    # Step 9: Run the user interface to allow the user to check the status of
    # packages at any time
    user_interface(hash_table)

if __name__ == "__main__":
    main()
