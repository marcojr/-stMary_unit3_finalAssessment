# allocator.py

from locations import get_location_distance_by_name


class Allocator:
    """
    This class is responsible for matching resources to incidents.

    It looks at pending incidents, check what resources are needed (like ambulance, fire truck, etc),
    and try to assign the closest available ones.

    If everything needed is found and assigned, the incident becomes "Assigned".
    If something's missing, nothing is assigned and it stays "Pending".
    """

    def __init__(self, resource_manager, incident_manager):
        self.resource_manager = resource_manager
        self.incident_manager = incident_manager

    def _get_sorted_resources_by_distance(self, resources, incident_location):
        """
        Internal helper to sort list of resources by how close they are to the incident.

        Uses the location distances (in miles from Chelmsford).
        So if an ambulance is in London and the incident is in Ipswich, we compare their distances.
        The lowest difference wins.
        """
        return sorted(
            resources,
            key=lambda r: abs(
                get_location_distance_by_name(r.location) - get_location_distance_by_name(incident_location)
            )
        )


    def allocate_resources(self):
        """
        Goes through all pending incidents (sorted by priority),
        and try to allocate the closest available resources.

        If all required resources are found and assigned, the incident is marked as "Assigned".
        Otherwise, nothing is assigned.
        """
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

                sorted_available = self._get_sorted_resources_by_distance(available, incident.location)
                resource = sorted_available[0]

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
        """
        This is like a second-chance allocation.

        If a new high-priority incident appears, and the resources are busy with low-priority incidents,
        this method will try to grab the resource from the less important case and reassign it.

        It never steals from incidents that have same or higher priority.
        """
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
        """
        Just a helper to compare two incidents and see if a is lower priority than b.

        "High" is 1, "Medium" is 2, "Low" is 3.
        """
        priority_map = {"High": 1, "Medium": 2, "Low": 3}
        return priority_map.get(incident_a.priority, 4) > priority_map.get(incident_b.priority, 4)
