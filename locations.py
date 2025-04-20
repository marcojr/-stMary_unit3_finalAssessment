# locations.py

LOCATIONS = {
    1: {"name": "London", "distance": 30},
    2: {"name": "Ipswich", "distance": 37},
    3: {"name": "Manchester", "distance": 166}
}

def get_location_name_by_id(location_id):
    return LOCATIONS.get(location_id, {}).get("name")

def get_location_distance_by_name(name):
    for loc in LOCATIONS.values():
        if loc["name"] == name:
            return loc["distance"]
    return None
