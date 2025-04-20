# allocator.py

class Allocator:
    """Handles the allocation of resources to incidents."""

    def __init__(self, resource_manager, incident_manager):
        self.resource_manager = resource_manager
        self.incident_manager = incident_manager

    def allocate_resources(self):
        sorted_incidents = self.incident_manager.get_sorted_incidents()

        for incident in sorted_incidents:
            print(f"\n[ALLOCATOR] INCIDENT {incident.id}")
            print(f"  PRIORITY: {incident.priority}")
            print(f"  STATUS: {incident.status}")
            print(f"  REQUIRED RESOURCES: {incident.required_resources}")


            if incident.status != "Pending":
                continue

            assigned_resources = []
            success = True

            for required_type in incident.required_resources:
                available = self.resource_manager.get_available_resources(
                    resource_type=required_type
                )

                if not available:
                    success = False
                    break

                resource = available[0]
                resource.assign()
                assigned_resources.append(resource)

            if success:
                incident.update_status("Assigned")
                print(f"  Incident {incident.id} successfully assigned.")

            else:
                for res in assigned_resources:
                    res.release()
                print(f"  Incident {incident.id} could not be fully assigned.")





    def reallocate_resources(self):
        """Reassign resources from low-priority incidents to high-priority pending ones."""
        sorted_incidents = self.incident_manager.get_sorted_incidents()

        for incident in sorted_incidents:
            if incident.status != "Pending":
                continue

            assigned = []
            success = True

            for r_type in incident.required_resources:
                available = self.resource_manager.get_available_resources(r_type)

                if available:
                    resource = available[0]
                    resource.assign()
                    assigned.append(resource)
                else:
                    # Tenta liberar recursos já alocados de incidentes de prioridade inferior
                    for other_incident in self.incident_manager.incidents:
                        if other_incident.status == "Assigned" and self._is_lower_priority(other_incident, incident):
                            for res in self.resource_manager.resources:
                                if not res.available and res.type == r_type:
                                    res.release()
                                    res.assign()
                                    assigned.append(res)
                                    break
                    if not any(res.type == r_type for res in assigned):
                        success = False
                        break

            if success:
                incident.update_status("Assigned")
            else:
                for res in assigned:
                    res.release()

    def _is_lower_priority(self, incident_a, incident_b):
        """Returns True if incident_a has lower priority than incident_b."""
        priority_map = {"High": 1, "Medium": 2, "Low": 3}
        return priority_map.get(incident_a.priority, 4) > priority_map.get(incident_b.priority, 4)
