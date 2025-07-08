from abc import ABC, abstractmethod
import numpy as np

class ForceModel(ABC):

    @abstractmethod
    def compute_acceleration(self):
        pass