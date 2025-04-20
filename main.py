# main.py

from resource_manager import ResourceManager
from incident_manager import IncidentManager
from allocator import Allocator
from console_ui import ConsoleUI

def main():
    resource_manager = ResourceManager()
    incident_manager = IncidentManager()
    allocator = Allocator(resource_manager, incident_manager)
    ui = ConsoleUI(resource_manager, incident_manager, allocator)
    ui.run()

if __name__ == "__main__":
    main()
