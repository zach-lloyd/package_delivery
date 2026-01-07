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
HUB_ADDRESS = "4001 South 700 East"
# Packages whose arrival at the hub is delayed until 9:05 AM
LATE_PACKAGE_IDS = [6, 25, 28, 32]

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

TRUCK1_ID = 1
TRUCK2_ID = 2
TRUCK3_ID = 3

def main():
    # Step 1: Initialize the hash table with one bucket for each package
    packages = CustomHashTable(40)

    # Step 2: Read the data from the packages and distances files
    import_packages(PACKAGES_FILENAME, packages)
    distances = import_distances(DISTANCES_FILENAME)

    # Step 3: Create the truck objects. For this project, there are three trucks,
    # so we create three objects
    truck1 = Truck(TRUCK1_ID, CAPACITY, MPH, HUB_ADDRESS)
    truck2 = Truck(TRUCK2_ID, CAPACITY, MPH, HUB_ADDRESS)
    truck3 = Truck(TRUCK3_ID, CAPACITY, MPH, HUB_ADDRESS)

    # Step 4: Load the packages onto the trucks and check for any packages that
    # weren't loaded. Note that here, loading refers to "constructive loading",
    # i.e. assigning each package to a truck based on its deadline and note (if any).
    # The packages that are delayed are of course not actually physically loaded
    # onto their assigned truck until they arrive at the Hub
    overflow = load_trucks(packages, [truck1, truck2, truck3])

    if overflow:
        print(f"Warning: the following packages were not loaded:")
        for pkg in overflow:
            print(pkg.addr)
    
    # Simulate the arrival and loading of all packages other than those that are late
    for p in packages:
        if p.ID not in LATE_PACKAGE_IDS:
            p.set_arrival_time(800)
            p.update_status("At the Hub")

    # Step 5: Set Truck 1 departs and begins delivering its packages
    truck1.set_departure_time(TRUCK1_DEPARTURE_TIME)
    truck1_return_time, truck1_miles_travelled = truck1.deliver_packages(distances)

    # Step 6: The delayed packages arrive and are loaded onto Truck 2, which then
    # departs and begins delivering its packages
    for id in LATE_PACKAGE_IDS:
        p = packages.lookup(id)
        p.set_arrival_time(905)
        p.update_status("At the Hub")

    truck2.set_departure_time(TRUCK2_DEPARTURE_TIME)
    truck2_return_time, truck2_miles_travelled = truck2.deliver_packages(distances)

    # Step 7: Set Truck 3's departure time, which is based on whichever of the first 2
    # trucks got back first (keeping in mind that regardless of how quickly the
    # first two trucks arrive back, the third truck MUST wait until at least 10:20
    # to get the corrected address for Package 9)
    earliest_return_time = min(truck1_return_time, truck2_return_time)
    
    if earliest_return_time >= 1020:
        TRUCK3_DEPARTURE_TIME = earliest_return_time
    else:
        TRUCK3_DEPARTURE_TIME = 1020

    # Step 8: The correct address for Package 9 is received. Update it, then 
    # set Truck 3's departure time and deliver its packages
    corrected_package = packages.lookup(9)
    corrected_package.update_address("410 S State St")
    corrected_package.update_zip("84111")

    truck3.set_departure_time(TRUCK3_DEPARTURE_TIME)
    truck3_return_time, truck3_miles_travelled = truck3.deliver_packages(distances)

    # Step 9: Print the return times and miles travelled of each truck, the total
    # miles travelled, and the number of packages delivered on time, late, or not
    # delivered at all
    print_final_information(
        packages, 
        [truck1_return_time, truck2_return_time, truck3_return_time],
        [truck1_miles_travelled, truck2_miles_travelled, truck3_miles_travelled]
    )

    # Step 10: Run the user interface to allow the user to check the status of
    # packages at any time
    user_interface(packages)

if __name__ == "__main__":
    main()
