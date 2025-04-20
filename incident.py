# incident.py

class Incident:
    """Represents an emergency incident."""

    def __init__(self, incident_id: int, location: str, emergency_type: str,
                 priority: str, required_resources: list):
        self.id = incident_id
        self.location = location
        self.emergency_type = emergency_type
        self.priority = priority
        self.required_resources = required_resources
        self.status = "Pending"

    def update_status(self, new_status: str):
        """Update the incident status."""
        self.status = new_status

