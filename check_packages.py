def check_packages(packages):
    """
    Checks each package to determine what its status is.
    
    :param packages: Packages hash table.

    Returns: Thruple representing how many packages have been delivered on time,
    how many have been delivered late, and how many have not yet been delivered.
    """
    on_time = 0
    late = 0
    not_delivered = 0

    for p in packages:
        status = p.get_status()

        if status == "On time":
            on_time += 1
        elif status == "Late":
            late += 1
        elif status == "At the Hub" or status == "En Route":
            not_delivered += 1
    
    return on_time, late, not_delivered
