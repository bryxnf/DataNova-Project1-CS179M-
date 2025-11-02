import os
from math import ceil
from GeneticAlgorithm import displayRouteIndicies

def routeFileCreator(points, path, inputBasename, D):

    routeNodes = displayRouteIndicies(points, path)
    distanceTraveled = ceil(D)                                        #rounding D up because D may have decimals
    filename = f"{inputBasename}_SOLUTION_{distanceTraveled}.txt"
    output_folder = os.path.join(os.getcwd(), "RouteTextFiles")
    os.makedirs(output_folder, exist_ok = True) 
    filepath = os.path.join(output_folder, filename)

    with open(filepath, "w") as pathTextFile:                           #creating the textfile
        for nodeNumber in routeNodes:
            pathTextFile.write(f"{nodeNumber}\n")

    print(f"Route written to disk as {inputBasename}_SOLUTION_{distanceTraveled}.txt")
    return filepath