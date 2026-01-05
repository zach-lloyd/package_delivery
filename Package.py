from convert_to_military_time import convert_to_military_time

class Package:
    def __init__(self, ID, addr, deadline, city, state, zip, weight, note, status = "At the Hub"):
        """
        Called upon creation of an object.
        
        :param ID: The package's unique ID.
        :param addr: The address the package is to be delivered to.
        :param deadline: The package's delivery deadline.
        :param city: The city where the package should be delivered to.
        :param state: The state where the package should be delivered to.
        :param zip: The zip code of the package's delivery address.
        :param weight: The weight of the package.
        :param note: Any special note attached to the package. If no such note, 
        this is an empty string.
        :param status: The package's delivery status (every package starts "At the Hub").
        """
        self.ID = ID
        self.addr = addr
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.note = note
        self.status = status
        self.delivery_time = None # Military time
        # Convert the deadline to military time to faclitate arithmetic logic 
        self.deadline_military = convert_to_military_time(self.deadline)
        # Track whether the package was delivered on time or late, to faciliate
        # assessing whether the algorithm succeeds in delivering each package by
        # its deadline
        self.on_time_or_late = None
        # The time the package leaves the Hub, in military time
        self.departure_time = None
        # ID of the truck that the package is loaded to
        self.truck_id = None 
    
    def __str__(self):
        """
        Prints a formatted string containing all of the package's information.
        """
        return f"{self.ID}, {self.addr}, {self.city}, {self.state}, {self.zip}, \
                 {self.deadline}, {self.weight}, {self.status}"
    
    def update_status(self, status, del_time = None):
        """
        Updates the status of the package.
        
        :param status: String representing the new status of the package.
        :param del_time: If the package was delivered

        Returns: True or False, depending on whether the package was delivered
        or not.
        """
        self.status = status
        self.delivery_time = del_time
        
        if del_time is None:
            return False
        elif del_time <= self.deadline_military:
            self.on_time_or_late = "On Time"
        else:
            self.on_time_or_late = "Late"
        
        return True
    
    def get_status(self):
        """
        Returns the package's current status.
        """
        return self.status
    
    def get_on_time_or_late(self):
        """
        If the package has been delivered, returns a string indicating whether
        it was delivered on time or late. If the package has not been delivered,
        returns None. 
        """
        return self.on_time_or_late
    
    def get_status_at_time(self, time_query):
        """
        Gets the package's status at the time specified in the user's time query.

        :param time_query: Time for which the user requests a snapshot of the 
        package statuses, expressed in military time.

        Returns: The status of the package at the queried time (either Delivered,
        En Route, or At the Hub).
        """
        # If delivered, check if the delivery happened before the query time
        if self.delivery_time and self.delivery_time <= time_query:
            return "Delivered"
        # If not delivered yet, check if the truck has left
        elif self.departure_time and self.departure_time <= time_query:
            return "En Route"
        # Otherwise, it's still at the Hub
        else:
            return "At the Hub"
    
    def set_departure_time(self, time):
        """
        Sets the time at which the package departed from the Hub, in military 
        time.
        
        :param time: The time at which the package departed from the Hub, in 
        military time.
        """
        self.departure_time = time
    
    def set_truck_id(self, id):
        """
        Identifies the ID of the truck the package is loaded to.

        :param id: ID of the truck the package is loaded to.
        """
        self.truck_id = id
