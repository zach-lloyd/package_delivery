def convert_to_military_time(time):
        """
        Converts time from 'HH:MM A/PM' format to an integer formatted in 
        military time.
        
        :param time: The time to be converted, formated as a string 'HH:MM A/PM'.

        Returns: The time converted to military time.
        """
        if time == "EOD":
            return 2400
        else:
            split_time = time.split(":")
            # Make sure to remove any whitespace
            split_time[1] = split_time[1].strip()

            # Handle 12:00 PM and 12:00 AM edge cases
            if split_time[1][-2:] == "PM" and split_time[0] != "12":
                split_time[0] = str(int(split_time[0]) + 12)
            elif split_time[1][-2:] == "AM" and split_time[0] == "12":
                split_time[0] = "0"
            
            if len(split_time[0]) == 1:
                split_time[0] = "0" + split_time[0]
            
            hours = split_time[0]
            mins = split_time[1][0:2]
            military = hours + mins

            return int(military)
        