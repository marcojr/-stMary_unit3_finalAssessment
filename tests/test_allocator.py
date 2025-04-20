import unittest
import sys
from allocator import Allocator
from resource import Ambulance, FireTruck
from incident import Incident
from incident_manager import IncidentManager
from resource_manager import ResourceManager

def setUpModule():
    sys.stdout = sys.__stdout__


class TestAllocator(unittest.TestCase):
    def setUp(self):
        self.resource_manager = ResourceManager()
        self.incident_manager = IncidentManager()
        self.allocator = Allocator(self.resource_manager, self.incident_manager)

        # Available resources
        self.ambulance1 = Ambulance(1, "Zone A")
        self.truck1 = FireTruck(2, "Zone A")

        self.resource_manager.add_resource(self.ambulance1)
        self.resource_manager.add_resource(self.truck1)

        # Incidents
        self.incident1 = Incident(
            incident_id=1,
            location="Zone A",
            emergency_type="Accident",
            priority="High",
            required_resources=["ambulance"]
        )

        self.incident2 = Incident(
            incident_id=2,
            location="Zone A",
            emergency_type="Fire",
            priority="Low",
            required_resources=["fire_truck"]
        )

        self.incident_manager.add_incident(self.incident1)
        self.incident_manager.add_incident(self.incident2)

    def test_allocate_resources(self):
        self.allocator.allocate_resources()
        self.assertEqual(self.incident1.status, "Assigned")
        self.assertFalse(self.ambulance1.available)

    def test_reallocate_resources(self):
         # 1st, force incident1 (low priority) to be allocated
        self.incident1.priority = "Low"
        self.incident2.priority = "High"
        self.allocator.allocate_resources()

        # At this point, both can be assigned because we have 2 resources available
        self.assertEqual(self.incident1.status, "Assigned")
        self.assertEqual(self.incident2.status, "Assigned")

         # Now simulate that the resource from incident1 was released
        self.incident1.status = "Pending"
        self.ambulance1.release()
        self.truck1.assign()  # simula que o caminhão está ocupado com outra coisa

        # Perform reallocation
        self.allocator.reallocate_resources()

        # Expect incident2 to remain as "Assigned"
        self.assertEqual(self.incident2.status, "Assigned")

         # And the truck1 resource is still occupied
        self.assertFalse(self.truck1.available)

