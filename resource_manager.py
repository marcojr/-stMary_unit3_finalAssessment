# resource_manager.py

class ResourceManager:
    """Manages the list of emergency resources."""

    def __init__(self):
        self.resources = []

    def add_resource(self, resource):
        """Add a new resource to the list."""
        self.resources.append(resource)

    def update_resource(self, resource_id, **kwargs):
        """Update resource attributes by ID."""
        for resource in self.resources:
            if resource.id == resource_id:
                for key, value in kwargs.items():
                    if hasattr(resource, key):
                        setattr(resource, key, value)

    def get_available_resources(self, resource_type=None, location=None):
        """Get a list of available resources, filtered by type and/or location."""
        filtered = [r for r in self.resources if r.available]

        if resource_type:
            filtered = [r for r in filtered if r.type == resource_type]

        if location:
            filtered = [r for r in filtered if r.location == location]

        return filtered
