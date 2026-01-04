from convert_to_military_time import convert_to_military_time

def user_interface(hash_table):
    while True:
        try:
            user_time = input("Please enter a time to check status of package(s) "
                              "(HH:MM AM/PM) or 'exit': ")
            
            if user_time == "exit":
                break

            converted_time = convert_to_military_time(user_time)

            print(f"\nStatus of all packages at {converted_time}:")
            print("-" * 60)
            print(f"{'ID':<4} {'Status':<12} {'Address':<40} {'Deadline':<10}")
            print("-" * 60)

            for id in range(1, 41):
                package = hash_table.lookup(id)
                package_status_at_time = package.get_status_at_time(converted_time)
                
                # Print row
                print(f"{package.ID:<4} {package_status_at_time:<12} \
                        {package.addr:<40} {package.deadline:<10}")
                
        except (ValueError, IndexError):
            print("Invalid entry. Please enter time in the format 'HH:MM AM/PM' "
                  "(e.g. 10:30 AM or 1:30 PM).")
            