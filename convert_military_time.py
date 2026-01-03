def convert_military_time(time):
    """
    Converts military time to HH:MM A/P.M. format.
    
    :param time: Time to be converted, expressed in military time.

    Returns: A formatted string that expresses the specified time in 
    HH:MM A/P.M. format.
    """
    hours = time // 100
    mins = time % 100
    am_or_pm = "A.M."

    if hours == 0:
        hours = 12
    elif hours > 12:
        am_or_pm = "P.M."
        hours -= 12
    
    return f"{str(hours)}:{str(mins)} {am_or_pm}"
