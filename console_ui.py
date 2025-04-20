# console_ui.py

from incident_manager import IncidentManager
from resource_manager import ResourceManager
from allocator import Allocator
from resource import Ambulance, FireTruck, MedicalTeam
from incident import Incident
from locations import LOCATIONS, get_location_name_by_id


def print_menu():
    print("\n=== Emergency Resource Allocation System ===")
    print("1. Add Resource")
    print("2. Add Incident")
    print("3. View Resources")
    print("4. View Incidents")
    print("5. Allocate Resources")
    print("6. Reallocate Resources")
    print("0. Exit")

def print_resources(resources):
    print("\n--- Resources ---")
    print(f"{'ID':<4} {'Type':<12} {'Location':<12} {'Status':<10}")
    print("-" * 40)
    for r in resources:
        status = "Available" if r.available else "Assigned"
        print(f"{r.id:<4} {r.type:<12} {r.location:<12} {status:<10}")


def print_incidents(incidents):
    print("\n--- Incidents ---")
    print(f"{'ID':<4} {'Type':<12} {'Priority':<8} {'Location':<12} {'Status':<10} {'Required Resources'}")
    print("-" * 80)
    for i in incidents:
        required = ', '.join(i.required_resources)
        print(f"{i.id:<4} {i.emergency_type:<12} {i.priority:<8} {i.location:<12} {i.status:<10} {required}")


def resource_type_menu():
    while True:
        print("1 - Ambulance")
        print("2 - Fire Truck")
        print("3 - Medical Team")
        option = input("Select resource type: ").strip()
        types = {
            "1": "ambulance",
            "2": "fire_truck",
            "3": "medical_team"
        }
        if option in types:
            return types[option]
        else:
            print("Invalid selection. Try again.")


def main():
    incident_manager = IncidentManager()
    resource_manager = ResourceManager()
    allocator = Allocator(resource_manager, incident_manager)

    while True:
        print_menu()
        choice = input("Select an option: ")

        if choice == "1":
            print("\nAdd Resource")
            r_type_str = resource_type_menu()
            if not r_type_str:
                print("Invalid selection.")
                continue

            try:
                r_id = int(input("ID: "))
            except ValueError:
                print("Invalid ID. Must be a number.")
                continue

            print("\nSelect resource location:")
            for key, value in LOCATIONS.items():
                print(f"{key} - {value['name']} ({value['distance']} miles from Chelmsford)")

            while True:
                try:
                    loc_choice = int(input("Enter location number: "))
                    if loc_choice not in LOCATIONS:
                        raise ValueError
                    location = get_location_name_by_id(loc_choice)
                    break
                except ValueError:
                    print("Invalid location. Please enter a valid number from the list.")


            if r_type_str == "ambulance":
                resource = Ambulance(r_id, location)
            elif r_type_str == "fire_truck":
                resource = FireTruck(r_id, location)
            elif r_type_str == "medical_team":
                resource = MedicalTeam(r_id, location)

            resource_manager.add_resource(resource)
            print("Resource added.")


        elif choice == "2":
            print("\nAdd Incident")
            try:
                i_id = int(input("Incident ID: "))
            except ValueError:
                print("Invalid ID. Must be a number.")
                continue

            print("\nSelect incident location:")
            for key, value in LOCATIONS.items():
                print(f"{key} - {value['name']} ({value['distance']} miles from Chelmsford)")

            while True:
                try:
                    loc_choice = int(input("Enter location number: "))
                    if loc_choice not in LOCATIONS:
                        raise ValueError
                    location = get_location_name_by_id(loc_choice)
                    break  
                except ValueError:
                    print("Invalid location. Please enter a valid number from the list.")



            e_type = input("Emergency Type: ")
            priority = input("Priority (High/Medium/Low): ").capitalize()
            if priority not in ["High", "Medium", "Low"]:
                print("Invalid priority. Must be High, Medium, or Low.")
                continue


            required_list = []
            while True:
                print("\nSelect required resources (one at a time):")
                r_type = resource_type_menu()
                if r_type:
                    required_list.append(r_type)
                else:
                    print("Invalid option.")
                    continue
                more = input("Add another? (y/n): ").strip().lower()
                if more != "y":
                    break

            incident = Incident(i_id, location, e_type, priority, required_list)
            incident_manager.add_incident(incident)
            print("Incident added.")

        elif choice == "3":
            print_resources(resource_manager.resources)

        elif choice == "4":
            print_incidents(incident_manager.incidents)

        elif choice == "5":
            allocator.allocate_resources()
            print("Allocation complete.")

        elif choice == "6":
            allocator.reallocate_resources()
            print("Reallocation complete.")

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
