from convert_from_military_time import convert_from_military_time 
from check_packages import check_packages

def print_final_information(packages, arrival_times, miles_travelled):
    """
    Prints the final results of running the algorithm.
    
    :param packages: A hash table with the packages that were delivered.
    :param arrival_times: List of times, in military time, at which the trucks
    arrived back at the Hub.
    :param miles_travelled: The total miles travelled by all the trucks.
    """
    print("\nWGUPS Routing Program\n")
    for i in range(len(arrival_times)):
        print(f"Truck {i + 1} Arrival, Miles Travelled: \
              {convert_from_military_time(arrival_times[i])}, {miles_travelled[i]}")
    
    print(f"\nTotal Miles Travelled: {"":<24} {sum(miles_travelled)}\n")

    on_time, late, not_delivered = check_packages(packages)

    print(f"Packages Delivered On Time: {"":<19} {on_time}")
    print(f"Packages Delivered Late: {"":<22} {late}")
    print(f"Packages Not Delivered: {"":<23} {not_delivered}\n")
