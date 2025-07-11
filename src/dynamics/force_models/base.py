from abc import ABC, abstractmethod
from src.core.satellite import Satellite
from src.core.time import SimulationClock

class BaseForceModel(ABC):
    def __init__(self, sat: Satellite, clock: SimulationClock, mu=3.986004418e14):
        self.sat = sat
        self.clock = clock
        self.mu = mu

    @abstractmethod
    def compute_acceleration(self):
        pass
