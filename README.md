# 🚨 Emergency Resource Allocation System

This project is a small console-based Python app made for the final assessment of Unit 3 at St. Mary.  
It helps simulate how emergency resources (like ambulances, fire trucks, etc.) are managed, assigned and reallocated based on incident urgency and location distance.

---

## ✨ What it does

- Register incidents with details like location, type, priority and what kind of resources are needed  
- Register and manage emergency resources (ambulances, fire trucks, medical teams)  
- Assign resources automatically – it chooses the **closest available one**  
- If something urgent comes up, the system will try to **reallocate from less important stuff**  
- Clean text interface with menu  
- Covers edge cases and real scenarios with unit tests  
- Fully built with OOP and nice modular files

---

## 🛠 Tech Stuff

- Python 3.10+  
- Just standard Python (no fancy libraries needed)  
- Uses `unittest` for test coverage

---

## ▶️ How to Run It

1. Clone this repo to your machine:

```bash
git clone https://github.com/marcojr/-stMary_unit3_finalAssessment.git
cd -stMary_unit3_finalAssessment
```

2. Run the app:

```bash
python console_ui.py
```

That’s it! You’ll see a menu with options to play with.

---

## ✅ How to Run the Tests

To run **all** the tests (they live in the `tests/` folder):

```bash
python -m unittest discover -v tests
```

Or to run just the allocator tests:

```bash
python run_allocator_tests.py
```

---

## 🧪 Manual Testing (Step by Step)

After launching `console_ui.py`, you can do this:

### 1. Add Some Resources
- Choose `1` to add an Ambulance (ID: 1, location: London)  
- Then `1` again to add a Fire Truck (ID: 2, location: Manchester)

### 2. Add Some Incidents
- Choose `2`, add incident ID: 1, location: London, type: Accident, priority: High, needs Ambulance  
- Choose `2` again, incident ID: 2, location: Manchester, type: Fire, priority: Low, needs Fire Truck

### 3. View What’s There
- Press `3` to see all resources  
- Press `4` to see all incidents – they should be marked as `Pending` initially

### 4. Let the System Assign Resources
- Press `5` to allocate. The system will pick the best fit based on priority + location.

### 5. Reallocation Test
- Add another incident (e.g. ID: 3, London, High priority) needing something already assigned  
- Then press `6` to see if it reassigns things smartly

### 6. Exit
- Just hit `0` to close the program

---

## 📦 Project Layout

```
.
├── allocator.py
├── console_ui.py
├── incident.py
├── incident_manager.py
├── locations.py
├── resource.py
├── resource_manager.py
├── run_allocator_tests.py
├── tests/
│   ├── test_allocator.py
│   ├── test_incident.py
│   ├── test_incident_manager.py
│   ├── test_resource.py
│   └── test_resource_manager.py
```

---


---

## 📄 SDLC Documentation

### 1. Requirements Analysis
- **Key Requirements**: Manage resources (ambulances, fire trucks, medical teams), assign based on proximity, and reallocate for high-priority incidents. It must be a console application using object-oriented principles.

### 2. Design Phase
- **System Components**: The system has separate components for managing incidents, resources, and allocation logic.
  - **Incident Manager**: Manages all incidents, updates, and sorting.
  - **Resource Manager**: Manages available resources and their assignment.
  - **Allocator**: The algorithm that assigns or reallocates resources.
  - **Console UI**: Allows user interaction through a simple menu.

### 3. Implementation
- The code is structured with classes for each resource type (ambulance, fire truck), incidents, and manager classes for handling resources and incidents. It uses Python's standard library without external dependencies.

### 4. Testing
- **Unit Testing**: Tests ensure that resources are assigned based on proximity and priority. Unit tests also verify that resources are reassigned from lower-priority incidents.
- **Edge Case Handling**: Tests for scenarios like unavailable resources or incidents with conflicting priorities.

### 5. Deployment
- The app runs in the console and doesn't require complex deployment. It can be executed with Python 3.10+.

### 6. Maintenance
- The modular design ensures that new resources, incident types, or even a database integration can be easily added.


## 📄 SDLC Documentation

### 1. Requirements Analysis
- **Key Requirements**: Manage resources (ambulances, fire trucks, medical teams), assign based on proximity, and reallocate for high-priority incidents. It must be a console application using object-oriented principles.

### 2. Design Phase
- **System Components**: The system has separate components for managing incidents, resources, and allocation logic.
  - **Incident Manager**: Manages all incidents, updates, and sorting.
  - **Resource Manager**: Manages available resources and their assignment.
  - **Allocator**: The algorithm that assigns or reallocates resources.
  - **Console UI**: Allows user interaction through a simple menu.

### 3. Implementation
- The code is structured with classes for each resource type (ambulance, fire truck), incidents, and manager classes for handling resources and incidents. It uses Python's standard library without external dependencies.

### 4. Testing
- **Unit Testing**: Tests ensure that resources are assigned based on proximity and priority. Unit tests also verify that resources are reassigned from lower-priority incidents.
- **Edge Case Handling**: Tests for scenarios like unavailable resources or incidents with conflicting priorities.

### 5. Deployment
- The app runs in the console and doesn't require complex deployment. It can be executed with Python 3.10+.

### 6. Maintenance
- The modular design ensures that new resources, incident types, or even a database integration can be easily added.



## ✍️ Note from the author

This was built as part of my end of unity acessment, but I tried to make it clean, modular and a bit realistic.  
Not everything is perfect – there's no database or GUI – but it does the job it's supposed to do.

Thanks for reading! 😄
