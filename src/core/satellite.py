import numpy as np

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

        self._x_ECI = np.array(x_ECI, dtype=np.float64).reshape(3)
        self._v_ECI = np.array(v_ECI, dtype=np.float64).reshape(3)

        self._q_ECI = np.array(q_ECI, dtype=np.float64).reshape(4)
        self._w_body = np.array(w_body, dtype=np.float64).reshape(3)

    def get_x_ECI(self) -> np.ndarray:
        return self._x_ECI
    
    def get_v_ECI(self) -> np.ndarray:
        return self._v_ECI
    
    def get_q_ECI(self) -> np.ndarray:
        return self._q_ECI
    
    def get_w_body(self) -> np.ndarray:
        return self._w_body

    def get_state(self) -> np.ndarray:
        return np.concatenate((self._x_ECI, self._v_ECI, self._q_ECI, self._w_body))
    
    def set_state(self, state: np.ndarray):
        assert state.shape == (13,)
        self._x_ECI = state[:3]
        self._v_ECI = state[3:6]
        self._q_ECI = state[6:10]
        self._w_body = state[10:13]