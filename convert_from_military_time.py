def convert_from_military_time(time):
    """
    Converts military time to HH:MM AM/PM format.
    
    :param time: Time to be converted, expressed in military time.

    Returns: A formatted string that expresses the specified time in 
    HH:MM AM/PM format.
    """
    hours = time // 100
    mins = time % 100
    am_or_pm = "AM"

    if hours == 0:
        hours = 12
    elif hours == 12:
        am_or_pm = "PM"
    elif hours > 12:
        am_or_pm = "PM"
        hours -= 12
    
    return f"{str(hours)}:{str(mins)} {am_or_pm}"
