import numpy as np

from src.core.satellite import Satellite
from src.core.time import SimulationClock
from src.dynamics.force_models.base import BaseForceModel

class NewtonianGravity(BaseForceModel):
    def __init__(self, sat: Satellite, clock: SimulationClock, mu=398600441800000):
        super().__init__(sat, clock, mu)

    def compute_acceleration(self):
        r = self.sat.x_ECI
        r_norm = np.linalg.norm(r)
        if r_norm == 0:
            raise ValueError("Satellite position vector cannot be zero.")
        
        a = -self.mu * r / r_norm**3
        return a
