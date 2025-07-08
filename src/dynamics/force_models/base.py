from abc import ABC, abstractmethod
import numpy as np
from src.core.time import SimulationClock

class BaseForceModel(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def compute_acceleration(self):
        pass