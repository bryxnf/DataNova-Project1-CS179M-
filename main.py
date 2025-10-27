import os
import time
import numpy as np
import threading

from GeneticAlgorithm import solveTSPNN, buildDistanceMatrix, tourLength
from tspOutputFileMaker import routeFileCreator
from DataVis import routeDisplay

inputEntered = False

def enterPressed():
    global inputEntered
    input()
    inputEntered = True

def main():
    global inputEntered
    print("===Drone Route Optimization Program===")
    filename = input("Enter the name of the input file: ").strip()

    input_folder = "InputCordsFolder"
    file_path = os.path.join(input_folder, filename)

    if not os.path.exists(file_path): #incase file doesnt exist
        print(f"[ERROR] '{file_path}' not found.")
        return

    #print(f"Drop locations found within input file: {file_path}")

    #print("Running Genetic Algorithm...")
    points = np.loadtxt(file_path)

    print("\nRunning optimization using solveTSPNN...(Press ENTER to stop)\n")

    best_distance = float('inf')
    best_route = None
    iteration = 0
    D = buildDistanceMatrix(points)

    listener = threading.Thread(target = enterPressed, daemon = True)
    listener.start()

    while not inputEntered:
        iteration += 1
        
        route_indices = solveTSPNN(points, start = 0, returnPoints = False)
        distance = tourLength(route_indices, D)

        if distance < best_distance:
            best_distance = distance
            best_route = points[route_indices]
            print(f"New best distance found: {best_distance:.2f} on iteration {iteration}")
            
        time.sleep(0.5)  # small delay
        
    print("\nOptimization stopped by user.\n")

    if best_route is not None:
        print(f"Best distance after optimization: {best_distance:.2f}")

        routeFileCreator(best_route, os.path.splitext(filename)[0], best_distance)
        print("Route file created.")

        routeDisplay(best_route, os.path.splitext(filename)[0], best_distance)
        print("Route displayed.")

    else:
        print("No valid route found.")


if __name__ == "__main__":
    main()