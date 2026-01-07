def convert_from_military_time(time):
    """
    Converts military time to HH:MM AM/PM format.
    
    :param time: Time to be converted, expressed in military time.

    Returns: A formatted string that expresses the specified time in 
    HH:MM AM/PM format.
    """
    hours = time // 100
    mins = time % 100

    hours_string = ""
    mins_string = ""
    am_or_pm = "AM"

    if hours == 0:
        hours_string = "12"
    elif hours == 12:
        hours_string = "12"
        am_or_pm = "PM"
    elif hours > 12:
        hours_string = str(hours - 12) 
        am_or_pm = "PM"
    else:
        hours_string = str(hours)

    if mins < 10: 
        mins_string = "0" + str(mins)
    else:
        mins_string = str(mins)        
    
    return f"{hours_string}:{mins_string} {am_or_pm}"
