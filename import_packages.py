import csv
from Package import Package

def import_packages(filename, hash_table):
    """
    Loads the package data from the packages file into the hash table.
    
    :param filename: Name of the file with the packages data.
    :param hash_table: Hash table object for storing the packages.
    """
    with open(filename, encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        for i, row in enumerate(rows[5:]):
            if row[0] == "": # Safety break if there are extra empty rows
                break
            
            id = int(row[0]) # Convert to integer for hashing
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            weight = row[6]
            note = row[7]
            status = "In Transit to Hub" # Each package starts out in transit to the hub

            pkg = Package(id, address, deadline, city, state, zip, weight, note, status)
            hash_table.insert(id, pkg)
