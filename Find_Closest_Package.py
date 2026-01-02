def find_closest_package(current_address, packages_in_truck, distances):
    """
    Finds the package in the truck closest to the address of the package 
    currently being delivered.
    
    :param current_address: The address of the package currently being delivered.
    :param packages_in_truck: A list of the packages still on the truck.
    :param distances: A nested dictionary of the distances between addresses.
    """
    min_distance = float("inf")
    closest_package = None
    current_deadline = float("inf")

    packages_in_truck.sort(key = lambda x: x.deadline_military)

    for p in packages_in_truck:
        # Make sure to deliver packages with the earliest deadlines first, even
        # if they are further away
        if p.deadline_military > current_deadline:
            break

        distance = distances[current_address][p.addr]

        if min_distance > distance:
            min_distance = distance
            closest_package = p
            current_deadline = p.deadline_military
        
    return min_distance, closest_package
