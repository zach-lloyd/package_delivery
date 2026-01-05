def load_trucks(packages, trucks):
    """
    Initializes the specified number of trucks and loads the packages onto them
    using a greedy algorithm that first focuses on handling packages with constraints,
    then focuses on loading packages by earliest deadline.
    
    :param packages: A list of package objects.
    :param trucks: A list of truck objects to be loaded. Assume Truck 1 is at 
    index 0, Truck 2 is at index 1, and so on.

    Returns: A list of 'overflow packages', which represent any packages that were
    not able to be loaded onto the trucks.
    """
    # Step 1: Initialize pending packages list
    pending_packages = []
    # Also initialize a list of overflow packages, in case we have more packages
    # than available room on the trucks
    overflow_packages = []

    # Step 2: Handle Packages with Notes
    deliver_together = [13, 14, 15, 16, 19, 20]

    # Note that at this Step 2 of the Loading Phase, we know none of the trucks
    # will be full, so we do not need to check if they have capacity before 
    # loading the packages that have notes
    for p in packages:
        # Truck 1 will leave the earliest, so add all of the packages that need
        # to be delivered together to Truck 1 because Package 15 has a 9:00am 
        # deadline
        if p.ID in deliver_together:
            trucks[0].load_package(p)
            p.set_truck_id(1)
        elif p.note == "Can only be on truck 2":
            trucks[1].load_package(p)
            p.set_truck_id(2)
        elif p.note == "Wrong address listed":
            trucks[2].load_package(p) # Truck 3 waits at the Hub for the correction
            p.set_truck_id(3)
        elif p.note == "Delayed on flight---will not arrive to depot until 9:05 am":
            trucks[1].load_package(p) # Truck 2 waits at the Hub for the delayed packages
            p.set_truck_id(2)
        else:
            pending_packages.append(p)
            
    # Step 3: Handle Deadlines (Greedy Load)
    # Sort the pending packages list so that the packages with the earliest
    # deadlines are loaded first. Truck 1 leaves before Truck 2 and Truck 2
    # before Truck 3, so this ensures the packages with the earliest deadlines
    # are placed on the trucks leaving the earliest
    pending_packages.sort(key = lambda x: x.deadline_military)

    for i in range(len(pending_packages)):
        p = pending_packages[i]
        package_loaded = False

        for t in trucks:
            # If the truck has capacity, its load function will return True and
            # we can break the loop because the package was successfully loaded.
            # If it returns False, that means there was no room on this truck so
            # try the next one.
            if t.load_package(p):
                package_loaded = True
                p.set_truck_id(t.id)
                break

        # Safety check to make sure all packages are loaded. If any are not, mark
        # them as overflow. main.py will use this to print a warning to the user.
        if not package_loaded:
            overflow_packages = pending_packages[i:]
            # Once we know one package can't be loaded, we know all trucks are full,
            # so no need to try to load additional packages.
            break
    
    # Return overflow packages to facilitate checking whether all packages were
    # loaded
    return overflow_packages
    