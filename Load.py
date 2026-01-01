def load(packages, num_trucks, capacity):
    # Step 1: Initialize Trucks and pending packages list
    trucks = [[] for _ in range(num_trucks)]
    pending_packages = []

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
            trucks[0].append(p)
        elif p.note == "Can only be on truck 2":
            trucks[1].append(p)
        elif p.note == "Wrong address listed":
            trucks[2].append(p) # Truck 3 waits at the Hub for the correction
        elif p.note == "Delayed on flight---will not arrive to depot until 9:05 am":
            trucks[1].append(p) # Truck 2 waits at the Hub for the delayed packages
        else:
            pending_packages.append(p)
    
    # Step 3: Handle Deadlines (Greedy Load)
    # Sort the pending packages list so that the packages with the earliest
    # deadlines are loaded first. Truck 1 leaves before Truck 2 and Truck 2
    # before Truck 3, so this ensures the packages with the earliest deadlines
    # are placed on the trucks leaving the earliest
    pending_packages.sort(key = lambda x: x.deadline_military)

    for p in pending_packages:
        for t in trucks:
            if len(t) < capacity:
                t.append(p)
                break
    
    return trucks
    