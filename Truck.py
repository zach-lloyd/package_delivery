from Find_Closest_Package import find_closest_package

class Truck:
    def __init__(self, capacity, departure_time, mph):
        self.capacity = capacity
        self.departure_time = departure_time # Military time
        self.current_time = departure_time # Military time
        self.packages = []
        self.mph = mph
        self.miles_travelled = 0
        # Every truck starts out at the Hub
        self.current_location = "4001 South 700 East" 
    
    def update_time(self, dist):
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
        if len(self.packages) < self.capacity:
            self.packages.append(p)
            return True
        else:
            return False
        
    def deliver_next_package(self, distances):
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
        distance = distances[self.current_location]["4001 South 700 East"]
        self.update_time(distance)
        self.current_location = "4001 South 700 East"



