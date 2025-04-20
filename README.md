# Emergency Resource Allocation System

This is a console-based Python application developed for the final assessment of Unit 3 at St. Mary. It simulates emergency resource management, allowing users to register incidents and resources, assign them based on availability and priority, and reallocate resources when necessary.

---

## 🚀 Features

- Register incidents (location, type, priority, required resources)
- Manage emergency resources (ambulances, fire trucks, medical teams)
- Assign resources automatically based on urgency and availability
- Reallocate resources to higher priority incidents when needed
- Console-based interface
- Fully unit tested (with edge case coverage)
- Object-oriented and modular design

---

## 🧩 Technologies

- Python 3.10+
- Standard Library only (no external dependencies)
- `unittest` for test automation

---

## ⚙️ How to Run the Application

1. Clone the repository:

```bash
git clone https://github.com/marcojr/-stMary_unit3_finalAssessment.git
cd -stMary_unit3_finalAssessment
```

2. Run the console interface:

```bash
python console_ui.py
```

---

## 🧪 How to Run the Tests

To execute all unit tests:

```bash
python -m unittest discover -v tests
```

Or to run a specific test file (e.g., allocator):

```bash
python run_allocator_tests.py
```

---

## 📝 Manual Test Instructions

Once running `console_ui.py`, follow this step-by-step guide to test the system manually:

### 1. Add Resources
- Option `1` → Add an ambulance with ID `1`, London
- Option `1` again → Add a fire truck with ID `2`, Manchester

### 2. Add Incidents
- Option `2` → Add Incident ID `1`, location `London`, type `Accident`, priority `High`, requires `Ambulance`
- Option `2` again → Add Incident ID `2`, location `Manchester`, type `Fire`, priority `Low`, requires `Fire Truck`

### 3. View Resources & Incidents
- Option `3` to list all resources
- Option `4` to list all incidents and their current status (should be "Pending")

### 4. Allocate Resources
- Option `5` → Resources will be assigned automatically

### 5. Reallocate (if needed)
- Option `2` → Add a new high-priority incident requiring an already assigned resource
- Option `6` → System will try to reassign from a lower-priority incident

### 6. Exit
- Option `0` to safely exit the application

---

## 📁 Project Structure

```
.
├── allocator.py
├── console_ui.py
├── incident.py
├── incident_manager.py
├── resource.py
├── resource_manager.py
├── run_allocator_tests.py
├── tests/
│   ├── __init__.py
│   ├── test_allocator.py
│   ├── test_incident.py
│   ├── test_incident_manager.py
│   ├── test_resource.py
│   └── test_resource_manager.py
```

---


