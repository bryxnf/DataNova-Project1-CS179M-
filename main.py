import os
import time
import numpy as np
import threading

from GeneticAlgorithm import solveTSPNN, buildDistanceMatrix, nearestNeigborOrderRand, solveTSPNNRand, tourLengthFromPoints, displayRouteIndicies
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

    points = np.loadtxt(file_path)

    print("\nRunning optimization using solveTSPNN...(Press ENTER to stop)\n")

    best_distance = float('inf')
    best_route = None
    iteration = 0

    listener = threading.Thread(target = enterPressed, daemon = True)
    listener.start()

    while not inputEntered:
        iteration += 1
        
        route_indices = solveTSPNN(points)
        distance = tourLengthFromPoints(route_indices)

        if distance < best_distance:
            best_distance = distance
            best_route = route_indices
            print(f"New best distance found: {best_distance:.2f} on iteration {iteration}")
            
        time.sleep(0.5)  # small delay
        
    print("\nOptimization stopped by user.\n")

    nodeCount = len(points)
    if nodeCount > 256:
        print(f"Warning: Solution is {best_distance}, greater than the 6000-meter constraint.")

    print(f"Indicies of the best route is: {displayRouteIndicies(points,best_route)}")

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