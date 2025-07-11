from abc import ABC, abstractmethod
import numpy as np
from src.core.satellite import Satellite
from src.core.time import SimulationClock

class BaseForceModel(ABC):
    def __init__(self, sat: Satellite, clock: SimulationClock):
        pass

    @abstractmethod
    def compute_acceleration(self):
        pass