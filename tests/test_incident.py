# tests/test_incident.py

import unittest
from incident import Incident

class TestIncident(unittest.TestCase):
    def setUp(self):
        self.incident = Incident(
            incident_id=1,
            location="Zone 5",
            emergency_type="Fire",
            priority="High",
            required_resources=["fire_truck"]
        )

    def test_incident_creation(self):
        self.assertEqual(self.incident.id, 1)
        self.assertEqual(self.incident.location, "Zone 5")
        self.assertEqual(self.incident.emergency_type, "Fire")
        self.assertEqual(self.incident.priority, "High")
        self.assertEqual(self.incident.status, "Pending")
        self.assertIn("fire_truck", self.incident.required_resources)

    def test_update_status(self):
        self.incident.update_status("Assigned")
        self.assertEqual(self.incident.status, "Assigned")

    def test_update_status_invalid(self):
        self.incident.update_status("Non-existent-status")
        self.assertEqual(self.incident.status, "Non-existent-status")  # Sem validação, aceita qualquer string
