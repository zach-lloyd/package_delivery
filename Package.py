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
        self.delivery_time = None
        self.deadline_military = self.convert_deadline(self.deadline)
    
    def __str__(self):
        """
        Prints a formatted string containing all of the package's information.
        """
        return f"{self.ID}, {self.addr}, {self.city}, {self.state}, {self.zip}, \
                 {self.deadline}, {self.weight}, {self.status}"
    
    def convert_deadline(self, dl):
        """
        Converts the package's deadlien from a string of format 'HH:MM A/PM' to
        an integer formatted in military time.
        
        :param dl: The package's deadline, formated as a string 'HH:MM A/PM'.
        """
        if dl == "EOD":
            return 2400
        else:
            split_dl = dl.split(':')
            # Make sure to remove any whitespace
            split_dl[1] = split_dl[1].strip()

            # Handle 12:00 PM and 12:00 AM edge cases
            if split_dl[1][-2:] == "PM" and split_dl[0] != "12":
                split_dl[0] = str(int(split_dl[0]) + 12)
            elif split_dl[1][-2:] == "AM" and split_dl[0] == "12":
                split_dl[0] = "0"
            
            if len(split_dl[0]) == 1:
                split_dl[0] = "0" + split_dl[0]
            
            hours = split_dl[0]
            mins = split_dl[1][0:2]
            military = hours + mins

            return int(military)
