from find_closest_package import find_closest_package

class Truck:
    def __init__(self, capacity, mph):
        """
        Called upon creation of a Truck object.
        
        :param capacity: The number of packages the truck can hold.
        :param departure_time: The time the truck will leave.
        :param mph: Average speed of the truck.
        """
        self.capacity = capacity
        # Will store the time the truck departs in military time. Initially None
        # because the truck's departure time is not set until it actually leaves.
        self.departure_time = None # Military time
        # Will store the time the current time in military time, for use in 
        # determining when packages are delivered and when the truck returns to
        # the hub. When the truck departs, the initial value of current_time is
        # set to be equal to departure_time.
        self.current_time = None # Military time
        self.packages = []
        self.mph = mph
        self.miles_travelled = 0
        # Every truck starts out at the Hub
        self.current_location = "4001 South 700 East"
        self.snapshots = {} 
    
    def set_departure_time(self, time):
        """
        Sets the truck's departure time and also initializes current_time to be
        the truck's departure time.
        
        :param time: An integer reflecting the departure time, expressed in
        military time.
        """
        self.departure_time = time
        self.current_time = time
    
    def update_time(self, dist):
        """
        Updates self.current_time to reflect the time elapsed travelling to 
        deliver the next package.
        
        :param dist: Distance travelled to deliver the package.
        """
        time_travelled_mins = (dist / self.mph) * 60
        
        # Convert current time (HHMM military time) to total minutes since midnight
        current_total_minutes = (int(self.current_time) // 100) * 60 + \
                                (int(self.current_time) % 100)
        
        new_total_minutes = current_total_minutes + time_travelled_mins

        # Convert back to HHMM military time
        hours = int(new_total_minutes // 60)
        minutes = int(new_total_minutes % 60)

        self.current_time = (hours * 100) + minutes

    def load_package(self, p):
        """
        Loads package p onto the truck.
        
        :param p: The package to be loaded onto the truck.

        Returns: True if the package was successfully loaded, False otherwise.
        """
        if len(self.packages) < self.capacity:
            self.packages.append(p)
            return True
        else:
            return False
        
    def deliver_next_package(self, distances):
        """
        Finds the next package on the truck and delivers it.
        
        :param distances: A nested dictionary of distances between locations.

        Returns: False if there are no more packages to deliver on this truck,
        True otherwise.
        """
        if len(self.packages) == 0:
            return False
        
        distance, next_package = find_closest_package(
            self.current_location, 
            self.packages,
            distances
        )

        self.current_location = next_package.addr
        self.miles_travelled += distance
        self.update_time(distance)
        next_package.update_status("delivered", self.current_time)
        self.packages.remove(next_package)

        return True
    
    def return_to_hub(self, distances):
        """
        Returns the truck to the hub.
        
        :param distances: A nested dictionary of distances between locations.
        """
        distance = distances[self.current_location]["4001 South 700 East"]
        self.update_time(distance)
        self.current_location = "4001 South 700 East"
    
    def create_snapshot(self, time):
        """
        Creates a snapshot of the truck's package statuses and miles travelled
        at the specified time.
        
        :param time: Time, in military time, at which to create the snapshot.
        """
        package_statuses = {}

        for p in self.packages:
            package_statuses[p.ID] = p.status
        
        self.snapshots[time] = (package_statuses, self.miles_travelled)
    
    def get_snapshot(self, time):
        """
        Returns a snapshot of the truck's package statuses and miles travelled
        at the time specified or, if a snapshot at that exact time is not 
        available, at the time in the snapshot dictionary that is closest to
        (but not after) the specified time. In other words, if time = 1330 and
        the snapshot dictionary has snapshots for 1312 and 1345 but not 1330,
        the snapshot for 1312 is returned.
        
        :param time: Time of the snapshot that is being requested.
        """
        if time in self.snapshots:
            return self.snapshots[time]
        else:
            closest_time = max(
                (tm for tm in self.snapshots if tm <= time), 
                default=None
            )

            return self.snapshots[closest_time]

    def deliver_packages(self, distances):
        """
        Iterates over the truck's package array and delivers all the packages.
        
        :param distances: A nested dictionary of distances between each pair of 
        locations.

        Returns: The current time when the truck arrives back at the hub after
        the deliveries and the total miles the truck travelled making the 
        deliveries.
        """
        # When the truck begins its deliveries, the status of every package 
        # should be updated from "At the Hub" to "En Route"
        for p in self.packages:
            p.update_status("En Route")
        
        self.create_snapshot(self.current_time)

        while True:
            delivered = self.deliver_next_package(distances)

            if delivered:
                self.create_snapshot(self.current_time)

            # If deliver_next_package returns False, it measn there are no 
            # more packages for this truck to deliver, so it can return to
            # the Hub
            if not delivered:
                self.return_to_hub(distances)
                self.create_snapshot(self.current_time)
                
                return self.current_time, self.miles_travelled
