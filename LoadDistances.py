import csv

def load_distances(filename):
    """
    Loads the data from the distances file into a nested dictionary.
    
    :param filename: Name of the distances file.
    """
    distances = {}

    with open(filename, encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        # The first 7 rows are not part of the table
        header_row = rows[7]
        addresses = []

        # Slice [2:] because this function will get the addresses from the column
        # headers, not the rows. The column headers of the first two rows do not
        # contain addresses, so we don't need them
        for raw_addr in header_row[2:]:

            # Each column header has multiple lines. The first line is the name
            # of the hub and the second line is the address. The second line is
            # what we want
            clean_addr = raw_addr.split("\n")[1].strip()

            # The header for the Hub actually has three lines, and the address
            # line actually ends with a comma. This removes that
            if clean_addr.endswith(","): 
                clean_addr = clean_addr[:-1]

            addresses.append(clean_addr)
        
        # Initialize the top-level keys in the dictionary
        for addr in addresses:
            distances[addr] = {}
        
        for i, row in enumerate(rows[8:]):
            if i >= len(addresses): # Safety break if there are extra empty rows
                break

            row_addr = addresses[i]
        
            # The spreadsheet is a triangle matrix, so only iterate up to i
            for j in range(i + 1):
                col_addr = addresses[j]
                # Distances start in the third column, so add 2 to j to get the
                # correct distance to map
                dist_str = row[2 + j]
                    
                # Convert to float (handle empty strings if necessary)
                distance = float(dist_str) if dist_str.strip() else 0.0
                    
                # Distance A -> B is the same as B -> A
                distances[row_addr][col_addr] = distance
                distances[col_addr][row_addr] = distance
    
    return distances

