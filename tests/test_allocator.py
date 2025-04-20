import unittest
import sys
from allocator import Allocator
from resource import Ambulance, FireTruck
from incident import Incident
from incident_manager import IncidentManager
from resource_manager import ResourceManager

def setUpModule():
    sys.stdout = sys.__stdout__


class TestAllocator(unittest.TestCase):
    def setUp(self):
        self.resource_manager = ResourceManager()
        self.incident_manager = IncidentManager()
        self.allocator = Allocator(self.resource_manager, self.incident_manager)

        # Recursos disponíveis
        self.ambulance1 = Ambulance(1, "Zone A")
        self.truck1 = FireTruck(2, "Zone A")

        self.resource_manager.add_resource(self.ambulance1)
        self.resource_manager.add_resource(self.truck1)

        # Incidentes
        self.incident1 = Incident(
            incident_id=1,
            location="Zone A",
            emergency_type="Accident",
            priority="High",
            required_resources=["ambulance"]
        )

        self.incident2 = Incident(
            incident_id=2,
            location="Zone A",
            emergency_type="Fire",
            priority="Low",
            required_resources=["fire_truck"]
        )

        self.incident_manager.add_incident(self.incident1)
        self.incident_manager.add_incident(self.incident2)

    def test_allocate_resources(self):
        self.allocator.allocate_resources()
        self.assertEqual(self.incident1.status, "Assigned")
        self.assertFalse(self.ambulance1.available)

    def test_reallocate_resources(self):
        # Primeiro, força o incidente 1 (baixa prioridade) a ser alocado
        self.incident1.priority = "Low"
        self.incident2.priority = "High"
        self.allocator.allocate_resources()

        # Neste ponto, ambos podem ser atribuídos porque temos 2 recursos disponíveis
        self.assertEqual(self.incident1.status, "Assigned")
        self.assertEqual(self.incident2.status, "Assigned")

        # Agora simula que o recurso de incident1 foi liberado (ex: prioridade trocada, recurso tomado de volta)
        self.incident1.status = "Pending"
        self.ambulance1.release()
        self.truck1.assign()  # simula que o caminhão está ocupado com outra coisa

        # Executa realocação
        self.allocator.reallocate_resources()

        # Espera que incident2 continue como "Assigned"
        self.assertEqual(self.incident2.status, "Assigned")

        # E o recurso truck1 ainda está ocupado
        self.assertFalse(self.truck1.available)

