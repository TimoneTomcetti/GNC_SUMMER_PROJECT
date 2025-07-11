import numpy as np

from src.utils import transformations

class Satellite:
    def __init__(
            self,
            sat_id: str,
            x_ECI: np.ndarray,
            v_ECI: np.ndarray,
            q_ECI: np.ndarray,
            w_body: np.ndarray,
    ):
        self.sat_id = sat_id

        self.x_ECI = np.array(x_ECI, dtype=np.float64).reshape(3)
        self.v_ECI = np.array(v_ECI, dtype=np.float64).reshape(3)

        self.q_ECI = transformations.check_unit_quaternion(np.array(q_ECI, dtype=np.float64).reshape(4))
        self.w_body = np.array(w_body, dtype=np.float64).reshape(3)

    def get_state(self) -> np.ndarray:
        return np.concatenate((self.x_ECI, self.v_ECI, self.q_ECI, self.w_body))
    
    def set_state(self, state: np.ndarray):
        assert state.shape == (13,)
        self.x_ECI = state[:3]
        self.v_ECI = state[3:6]
        self.q_ECI = state[6:10]
        self.w_body = state[10:13]