class Package:
    def __init__(self, ID, addr, deadline, city, zip, weight, note, status = "At the Hub"):
        self.ID = ID
        self.addr = addr
        self.deadline = deadline
        self.city = city
        self.zip = zip
        self.weight = weight
        self.note = note
        self.status = status
        self.delivery_time = None
        self.deadline_military = self.convert_deadline(self.deadline)
    
    def __str__(self):
        return f"{self.ID}, {self.addr}, {self.city}, {self.zip}, {self.deadline}, \
                 {self.weight}, {self.status}"
    
    def convert_deadline(self, dl):
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
