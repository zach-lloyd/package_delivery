import pandas as pd
import Package.py

# Skip the first 7 rows because they are the title rows.
df = pd.read_csv("WGUPS Package File.xlsx - Sheet1.csv", skiprows = 7)
# Clean up column names.
df.columns = [
    "ID", "Address", "City", "State", "Zip", "Deadline", "Weight", "Notes"
]

class HashTable:
    def __init__(self):
        self.hash_table = {}
    
    def insert_package(self, id):
        components = df[df["ID"] == id]
        pkg = Package(
            components["Address"], 
            components["Deadline"],
            components["City"],
            components["Zip"],
            components["Weight"],
            components["Notes"]
        )
        self.hash_table[id] = pkg
    
    def lookup(self, id):
        return self.hash_table[id]


    