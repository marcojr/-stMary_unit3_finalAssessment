# console_ui.py

from incident_manager import IncidentManager
from resource_manager import ResourceManager
from allocator import Allocator
from resource import Ambulance, FireTruck, MedicalTeam
from incident import Incident

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
    for r in resources:
        status = "Available" if r.available else "Assigned"
        print(f"ID: {r.id} | Type: {r.type} | Location: {r.location} | Status: {status}")

def print_incidents(incidents):
    print("\n--- Incidents ---")
    for i in incidents:
        print(f"ID: {i.id} | Type: {i.emergency_type} | Priority: {i.priority} | Location: {i.location} | Status: {i.status} | Required: {i.required_resources}")

def resource_type_menu():
    print("1 - Ambulance")
    print("2 - Fire Truck")
    print("3 - Medical Team")
    option = input("Select resource type: ").strip()
    types = {
        "1": "ambulance",
        "2": "fire_truck",
        "3": "medical_team"
    }
    return types.get(option)

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
            r_id = int(input("ID: "))
            location = input("Location (e.g. London, Colchester, Ipswich): ")

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
            i_id = int(input("Incident ID: "))
            location = input("Location: ")
            e_type = input("Emergency Type: ")
            priority = input("Priority (High/Medium/Low): ").capitalize()

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
