import numpy as np

def load_and_validate_points(file_path, max_nodes=256, allow_negative=False):
    points = []
    with open(file_path, 'r') as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:               #when there is no line raise this Error
                raise ValueError(f"Line {i}: Empty line detected.")

            parts = line.split()
            if len(parts) != 2:            #if each line has more than 2 coords.
                raise ValueError(f"Line {i}: Expected 2 coordinates, got {len(parts)} -> {parts}")

            try:
                x, y = float(parts[0]), float(parts[1])
            except ValueError:          #checks to see if the coords are numbers
                raise ValueError(f"Line {i}: Non-numeric coordinate found -> {parts}")

            if not allow_negative and (x < 0 or y < 0):    #makes sure the coords are not negative
                raise ValueError(f"Line {i}: Negative coordinate detected ({x}, {y})")

            points.append([x, y])

    if len(points) < 2:
        raise ValueError(f"File contains only {len(points)} node(s). Need at least 2 points.")

    return np.array(points, dtype=float)
