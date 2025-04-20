# tests/test_resource_manager.py

import unittest
from resource_manager import ResourceManager
from resource import Ambulance, FireTruck, MedicalTeam

class TestResourceManager(unittest.TestCase):
    def setUp(self):
        self.manager = ResourceManager()
        self.amb = Ambulance(1, "Zone 1")
        self.truck = FireTruck(2, "Zone 2")
        self.team = MedicalTeam(3, "Zone 3")

    def test_add_resource(self):
        self.manager.add_resource(self.amb)
        self.assertEqual(len(self.manager.resources), 1)

    def test_update_resource(self):
        self.manager.add_resource(self.truck)
        self.manager.update_resource(2, location="Zone 5")
        self.assertEqual(self.truck.location, "Zone 5")

    def test_get_available_resources(self):
        self.manager.add_resource(self.amb)
        self.manager.add_resource(self.team)
        available = self.manager.get_available_resources(resource_type="ambulance")
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].type, "ambulance")

