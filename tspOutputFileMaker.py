# tspOutputFileMaker.py
import os
from math import ceil

def routeFileCreator(route, input_basename, D, out_dir):
    """
    Temporary function to write the route to a text file.
    """
    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.join(out_dir, f"{input_basename}_SOLUTION_{ceil(D)}.txt")

    with open(filename, "w") as f:
        for i, coord in enumerate(route):
            f.write(f"{coord[0]:.2f}, {coord[1]:.2f}\n")

    print(f"[tspOutputFileMaker] Route saved to: {filename}")


