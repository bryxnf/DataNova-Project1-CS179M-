'''
Goal is to copy the entire main file
then run the program where you have a count time which calculates the time
and then when the user presses the ENTER button save that time total
also keep that distance array stored not THE BEST DISTANCE so we can show
the iterations of how the distance falls as more iterations happen
next once the first ENTER BUTTON is pressed we basically run the OTHER ALGORITHM
aka the Nearest Neighbour algorithm without the (RANDOMIZATION) here and run it until
that count time ends so we have an even time difference shown how both algorithms work
and once that timer ends we take the distance array of both one called distanceNN distanceNNRand
and basically send this to graph.py which will create the visualization and return it

NOTE:
distanceNN is a 2D array where it stores [[distance,iteration], [[550,42]]] or
distanceNN is a 3D array where it stores [[distance,iteration,time], [550,42,0:13:15]] something like that
'''
import os
import time
import numpy as np
import threading
import graph

from GeneticAlgorithm import solveTSPNN, buildDistanceMatrix, nearestNeigborOrderRand, solveTSPNNRand, tourLengthFromPoints, displayRouteIndicies
from tspOutputFileMaker import routeFileCreator
from DataVis import routeDisplay


inputEntered = False

def enterPressed():
    global inputEntered
    input()
    inputEntered = True

#create algorithm with timer, user will stop this function
def algorithm_with_timer(points, use_random = True):
    global inputEntered
    inputEntered = False

    best_distance = float('inf')
    best_route = None
    iteration = 0
    distance_log = [] # this will store my [distance, iteration, timestamp]

    start_time = time.time()
    listener = threading.Thread(target = enterPressed, daemon = True)
    listener.start()

    print(f"\nRunning{'Randomized' if use_random else 'Normal'} NN optimization...(Press ENTER to stop)\n")

    while not inputEntered:
        iteration +=1
        if use_random:
            route_indices = solveTSPNNRand(points)
        else:
            route_indices = solveTSPNN(points)
        
        distance = tourLengthFromPoints(route_indices)
        elapsed = time.time() - start_time

        distance_log.append([distance,iteration,elapsed])

        if distance < best_distance:
            best_distance = distance
            best_route = route_indices
            print(f"New best distance found: {best_distance:.2f} on iteration {iteration}")

        time.sleep(0.5)  # small delay

    total_time = time.time() - start_time
    print(f"\nStopped after {iteration} iterations and {total_time:.2f} seconds.")

    return best_route,best_distance,distance_log,total_time,iteration


    

def main():
    print("===Drone Route Optimization Program===")
    filename = input("Enter the name of the input file: ").strip()

    input_folder = "InputCordsFolder"
    file_path = os.path.join(input_folder, filename)

    if not os.path.exists(file_path): #incase file doesnt exist
        print(f"[ERROR] '{file_path}' not found.")
        return

    points = np.loadtxt(file_path)

    #call randomized alorthm first and assign the values that are returned
    routeRand, bestDistRand, distanceNNRand, total_time, total_iterations = algorithm_with_timer(points,use_random = True)

    print("\nNow running Nearest Neighbor (non-randomized) for equal time..\n")
    start_time = time.time()
    distanceNN = []
    bestDist = float('inf')
    bestRoute = None
    iteration = 0

    while (time.time()-start_time)< total_time:
        iteration +=1
        route_indices = solveTSPNN(points)
        distance = tourLengthFromPoints(route_indices)
        elapsed = time.time()-start_time

        #save all of the new data
        distanceNN.append([distance, iteration, elapsed])

        if distance < bestDist:
            bestDist = distance
            bestRoute = route_indices
            print(f"New best distance found: {bestDist:.2f} on iteration {iteration}")
        
        time.sleep(0.5)

    #need to save new results to graph.py
    print("\nCreating comparative performance graph...")
    graph.createGraph(distanceNNRand,distanceNN,total_time,total_iterations,filename)

    if bestRoute is not None:
        routeFileCreator(bestRoute,os.path.splitext(filename)[0],bestDist)
        routeDisplay(bestRoute, os.path.splitext(filename)[0], bestDist)
        print("\nRoute visualization complete.\n")

    print("===Program Finished===")

if __name__ == "__main__":
    main()