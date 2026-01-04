from convert_from_military_time import convert_from_military_time 
from check_packages import check_packages

def print_final_information(packages, arrival_times, miles_travelled):
    print("WGUPS Routing Program")
    for i in range(len(arrival_times)):
        print(f"Truck {i + 1} Arrival, Miles Travelled: \
              {convert_from_military_time(arrival_times[i])}, {miles_travelled[i]}")
    
    print(f"Total Miles Travelled: {sum(miles_travelled)}")

    on_time, late, not_delivered = check_packages(packages)

    print(f"Packages Delivered On Time: {on_time}")
    print(f"Packages Delivered Late: {late}")
    print(f"Packages Not Delivered: {not_delivered}")
