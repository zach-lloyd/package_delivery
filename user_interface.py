from convert_to_military_time import convert_to_military_time

def user_interface(hash_table):
    """
    Runs the user interface, which allows users to specify a time and receive
    a snapshot of each package's status at the specified time.
    
    :param hash_table: A hash table containing each of the packages.
    """
    while True:
        try:
            user_time = input("Please enter a time to check status of package(s) "
                              "(HH:MM AM/PM) or 'exit': ")
            
            if user_time == "exit":
                break

            # Convert time to military time, because that is the format expected
            # by each package's get_status_at_time() function
            converted_time = convert_to_military_time(user_time)

            print(f"\nStatus of all packages at {user_time}:")
            print("-" * 100)
            print(f"{'ID':<4} {'Status':<36} {'Address':<40} {'Deadline':<10} {'Truck':<10}")
            print("-" * 100)

            for id in range(1, 41):
                package = hash_table.lookup(id)
                package_status_at_time = package.get_status_at_time(converted_time)
                # If a package hasn't been assigned to a truck (e.g if it is an
                # overflow package) it is listed as "Unassigned"
                t_id = "Unassigned"

                if package.truck_id is not None:
                    t_id = package.truck_id
                
                print(f"{package.ID:<4} {package_status_at_time:<12} \
                        {package.addr:<40} {package.deadline:<10} {t_id}")

        # Handle situation where the user does not enter the time in the expected
        # format      
        except (ValueError, IndexError):
            print("Invalid entry. Please enter time in the format 'HH:MM AM/PM' "
                  "(e.g. 10:30 AM or 1:30 PM).")
            