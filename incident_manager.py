# incident_manager.py

class IncidentManager:
    def __init__(self):
        self.incidents = []

    def add_incident(self, incident):
        self.incidents.append(incident)  

    def update_incident(self, incident_id, **kwargs):
        for incident in self.incidents:
            if incident.id == incident_id:
                for key, value in kwargs.items():
                    if hasattr(incident, key):
                        setattr(incident, key, value)

    def get_sorted_incidents(self):
        priority_map = {"High": 1, "Medium": 2, "Low": 3}
        return sorted(self.incidents, key=lambda x: priority_map.get(x.priority, 4))

