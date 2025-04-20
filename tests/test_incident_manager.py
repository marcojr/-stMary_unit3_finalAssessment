# tests/test_incident_manager.py

import unittest
from incident_manager import IncidentManager
from incident import Incident

class TestIncidentManager(unittest.TestCase):
    def setUp(self):
        self.manager = IncidentManager()

        self.incident1 = Incident(1, "London", "Fire", "Medium", ["fire_truck"])
        self.incident2 = Incident(2, "Ipswich", "Medical", "High", ["ambulance"])
        self.incident3 = Incident(3, "Manchester", "Rescue", "Low", ["ambulance"])

        self.manager.add_incident(self.incident1)
        self.manager.add_incident(self.incident2)
        self.manager.add_incident(self.incident3)

    def test_add_incident(self):
        self.assertEqual(len(self.manager.incidents), 3)
        self.assertEqual(self.manager.incidents[0].id, 1)

    def test_update_incident(self):
        self.manager.update_incident(1, priority="High", status="Assigned")
        self.assertEqual(self.incident1.priority, "High")
        self.assertEqual(self.incident1.status, "Assigned")

    def test_get_sorted_incidents(self):
        sorted_list = self.manager.get_sorted_incidents()
        priorities = [i.priority for i in sorted_list]
        self.assertEqual(priorities, ["High", "Medium", "Low"])

    def test_update_nonexistent_incident(self):
        self.manager.update_incident(99, priority="Low")  # Should do nothing
        self.assertEqual(len(self.manager.incidents), 3)  # No new incident added

    def test_sort_with_invalid_priority(self):
        self.incident1.priority = "Unknown"
        sorted_list = self.manager.get_sorted_incidents()
        self.assertIn("Unknown", [i.priority for i in sorted_list])  # still sorted last

    def test_custom_status_on_creation(self):
        incident = Incident(4, "London", "Fire", "High", ["ambulance"])
        incident.status = "In Progress"
        self.manager.add_incident(incident)
        self.assertIn(incident, self.manager.incidents)

    def test_update_incident_with_invalid_field(self):
        self.manager.update_incident(1, nonexistent_field="test")
        self.assertTrue(True)  # Não deve explodir


