# tests/test_resource.py

import unittest
from resource import Ambulance, FireTruck, MedicalTeam

class TestResources(unittest.TestCase):
    def test_ambulance_creation(self):
        amb = Ambulance(1, "Zone 1")
        self.assertEqual(amb.id, 1)
        self.assertEqual(amb.type, "ambulance")
        self.assertEqual(amb.location, "Zone 1")
        self.assertTrue(amb.available)

    def test_firetruck_creation(self):
        truck = FireTruck(2, "Zone 2")
        self.assertEqual(truck.type, "fire_truck")

    def test_medical_team_creation(self):
        team = MedicalTeam(3, "Zone 3")
        self.assertEqual(team.type, "medical_team")

    def test_assign_and_release(self):
        team = MedicalTeam(4, "Zone 4")
        team.assign()
        self.assertFalse(team.available)
        team.release()
        self.assertTrue(team.available)
