import numpy as np

def check_unit_quaternion(q: np.ndarray, tol=1e-6):
    if q.shape != (4,):
        raise ValueError("Quaternion must be a 4-element array.")
    
    norm = np.linalg.norm(q)
    if abs(norm - 1.0) > tol:
        raise ValueError(f"Quaternion norm is not 1 (got {norm}).")
    
    return q