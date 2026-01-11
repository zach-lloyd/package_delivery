# Package Delivery Route Optimizer

A package delivery simulator that loads package + distance data from CSV files, plans truck routes, simulates delivery progression over time, and lets you query package status.

This project emphasizes **data structures**, **routing heuristics**, and **time-based state simulation** (e.g., "in transit to the hub" → "at hub" → "en route" → "delivered").

---

## Features

- **Fast package lookup** via a custom hash table
- **Route planning helper** to choose the next delivery stop (greedy / nearest-stop style heuristic)
- **Delivery simulation** with timestamps, mileage tracking, and per-truck state
- **Interactive CLI** to view results and check package statuses at a specific time

---

## Tech Stack

- **Python** (no external dependencies)
- CSV inputs for:
  - package data
  - distance table

---

## Project Structure

Key modules/files:

- `main.py` — entry point / orchestration
- `user_interface.py` — CLI menu + user prompts
- `CustomHashTable.py` — custom hash table implementation for packages
- `Package.py`, `Truck.py` — core domain models
- `Find_Closest_Package.py` — routing helper (selects next stop)
- `import_packages.py`, `import_distances.py` — CSV loaders
- `load_trucks.py` — assigns packages to trucks
- `check_packages.py` — time-based status checking
- `print_final_information.py` — summary output (mileage, delivery completion, etc.)
- `WGUPS Package File.csv`, `WGUPS Distance Table.csv` — input datasets

---

## How It Works (High Level)

1. **Load data**
   - Packages are loaded from CSV into a hash table for quick access. The hash table is implemented via a custom HashTable class.
   - Distances are loaded into a structure that supports distance lookups between stops.

2. **Assign packages to trucks**
   - Packages are grouped/assigned based on constraints (capacity, timing rules, etc.).

3. **Plan routes**
   - For each truck, the next stop is chosen using a greedy “closest next stop” approach.
   - As stops are visited, mileage and time advance.

4. **Simulate delivery**
   - Each package’s status transitions as the simulation time progresses:
   - The CLI can query package status at any time-of-day input.

---

## Getting Started

### Prerequisites
- Python 3.x installed

### Run
From the repo root:

```bash```
python main.py

---

## Example Usage

Actions you can perform using the CLI:
- Print a final delivery report, which describes the miles travelled by each truck, the total
number of miles travelled, and the number of packages delivered on time, late, or not delivered at all.
- Check the status of all packages at a specified time.

---

## Notes

- Currently, this is a heuristic route planner intended for a constrained delivery scenario, not a guaranteed
global optimum like TSP solvers. However, the code is modular and designed to be easily extended to other scenarios.
- The focus is on delivering all packages on time while balancing algorithmic efficiency with the need to minimize
the total number of miles travelled.

---

## Areas for Improvement

- Add unit tests for the algorithm's main functions.
- Experiment with possible solutions for making constraint handling more general. For example, consider the possible
use of AI to parse package notes and adjust truck assignments based on constraints identified in the notes.

---

## Screenshots of CLI
---

## License

No license file is currently present. Treat this as all rights reserved unless a license is added. If you plan to fork/distribute, please open an issue to discuss.

