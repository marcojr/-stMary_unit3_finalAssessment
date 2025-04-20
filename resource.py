# resource.py

class Resource:
    """Base class for all emergency resources."""

    def __init__(self, resource_id: int, resource_type: str, location: str):
        self.id = resource_id
        self.type = resource_type
        self.location = location
        self.available = True

    def assign(self):
        """Mark the resource as assigned."""
        self.available = False

    def release(self):
        """Mark the resource as available."""
        self.available = True


class Ambulance(Resource):
    """Represents an ambulance resource."""
    def __init__(self, resource_id: int, location: str):
        super().__init__(resource_id, "ambulance", location)


class FireTruck(Resource):
    """Represents a fire truck resource."""
    def __init__(self, resource_id: int, location: str):
        super().__init__(resource_id, "fire_truck", location)


class MedicalTeam(Resource):
    """Represents a medical team resource."""
    def __init__(self, resource_id: int, location: str):
        super().__init__(resource_id, "medical_team", location)
