import os
from math import ceil

def routeFileCreator(path, inputBasename, D):

    distanceTraveled = ceil(D)                                        #rounding D up because D may have decimals
    filename = f"{inputBasename}_SOLUTION_{distanceTraveled}.txt"
    output_folder = os.path.join(os.getcwd(), "RouteTextFiles")
    os.makedirs(output_folder, exist_ok = True) 
    filepath = os.path.join(output_folder, filename)

    with open(filepath, "w") as pathTextFile:                           #creating the textfile
        for nodeNumber in path:
            pathTextFile.write(f"{nodeNumber}\n")

    print(f"Route written to disk as {inputBasename}_SOLUTION_{distanceTraveled}.txt")
    return filepath