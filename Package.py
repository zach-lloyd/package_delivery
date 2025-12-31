class Package:
    def __init__(self, addr, deadline, city, zip, weight, note, status = "At the Hub"):
        self.addr = addr
        self.deadline = deadline
        self.city = city
        self.zip = zip
        self.weight = weight
        self.note = note
        self.status = status
