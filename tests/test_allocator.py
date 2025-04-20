# tests/test_allocator.py

import unittest

from allocator import Allocator
from resource import Ambulance, FireTruck
from incident import Incident
from incident_manager import IncidentManager
from resource_manager import ResourceManager


class TestAllocator(unittest.TestCase):
    def setUp(self):
        self.resource_manager = ResourceManager()
        self.incident_manager = IncidentManager()
        self.allocator = Allocator(self.resource_manager, self.incident_manager)

        # Resources in diff cities
        self.ambulance_london = Ambulance(1, "London")      # 30 mi
        self.ambulance_manchester = Ambulance(2, "Manchester")  # 166 mi
        self.truck_ipswich = FireTruck(3, "Ipswich")        # 37 mi

        self.resource_manager.add_resource(self.ambulance_london)
        self.resource_manager.add_resource(self.ambulance_manchester)
        self.resource_manager.add_resource(self.truck_ipswich)

    def test_allocate_prefers_closest_resource(self):
        incident = Incident(1, "London", "Crash", "High", ["ambulance"])
        self.incident_manager.add_incident(incident)

        self.allocator.allocate_resources()

        self.assertEqual(incident.status, "Assigned")
        self.assertFalse(self.ambulance_london.available)
        self.assertTrue(self.ambulance_manchester.available)

    def test_allocate_resources_multiple_types(self):
        incident = Incident(2, "Ipswich", "Accident", "High", ["ambulance", "fire_truck"])
        self.incident_manager.add_incident(incident)

        self.allocator.allocate_resources()

        self.assertEqual(incident.status, "Assigned")
        self.assertFalse(self.truck_ipswich.available)
        self.assertFalse(self.truck_ipswich.available)
        self.assertTrue(
            not self.ambulance_london.available or not self.ambulance_manchester.available
        )


    def test_no_resources_available(self):
        self.ambulance_london.assign()
        self.ambulance_manchester.assign()
        self.truck_ipswich.assign()

        incident = Incident(3, "London", "Emergency", "High", ["ambulance"])
        self.incident_manager.add_incident(incident)

        self.allocator.allocate_resources()
        # Only one Ambulance!
        self.resource_manager.resources = [self.ambulance_london]


    def test_reallocate_resources_priority_switch(self):
        # Only one ambulance available
        self.resource_manager.resources = [self.ambulance_london]

        incident1 = Incident(4, "London", "Minor", "Low", ["ambulance"])
        incident2 = Incident(5, "London", "Critical", "High", ["ambulance"])

        self.incident_manager.add_incident(incident1)
        self.incident_manager.add_incident(incident2)

        self.allocator.allocate_resources()

        # Confirm first allocation
        self.assertEqual(incident1.status, "Pending")
        self.assertEqual(incident2.status, "Assigned")


        # Simulate change
        incident1.status = "Pending"
        self.ambulance_london.release()

        self.allocator.reallocate_resources()

        # After reallocation, incident2 should be assigned
        self.assertEqual(incident2.status, "Assigned")
        self.assertFalse(self.ambulance_london.available)



    def test_all_resources_too_far_but_still_assigned(self):
        # Incident in London, only ambulance is in Manchester
        self.resource_manager.resources = [self.ambulance_manchester]

        incident = Incident(6, "London", "Late Response", "High", ["ambulance"])
        self.incident_manager.add_incident(incident)

        self.allocator.allocate_resources()
        self.assertEqual(incident.status, "Assigned")
        self.assertFalse(self.ambulance_manchester.available)

