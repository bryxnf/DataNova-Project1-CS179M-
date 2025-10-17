# geneticAlg.py
import numpy as np
import random

def run_algorithm(coords, config):
    """
    Temporary stand-in for the real Genetic Algorithm.
    Returns a fake 'route' and total distance D.
    """
    print("[geneticAlg] Running mock genetic algorithm...")

    N = len(coords)
    route_indices = list(range(N))
    random.shuffle(route_indices)

    # Make it a loop: start and end at index 0
    route_indices = [0] + route_indices + [0]

    # Convert route indices to coordinate pairs
    route_coords = [tuple(coords[i]) for i in route_indices]

    # Fake total distance (sum of straight lines)
    D = 0.0
    for i in range(len(route_coords) - 1):
        D += np.linalg.norm(np.array(route_coords[i+1]) - np.array(route_coords[i]))

    print(f"[geneticAlg] Mock route complete. Total distance ≈ {D:.2f}")
    return route_coords, D
