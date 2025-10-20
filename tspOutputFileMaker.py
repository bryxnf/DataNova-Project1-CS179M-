import os
from math import ceil

def routeFileCreator(path, inputBasename, D):

    distanceTraveled = ceil(D)                                        #rounding D up because D may have decimals
    filename = f"{inputBasename}_SOLUTION_{distanceTraveled}.txt"
    desktop = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
    filepath = os.path.join(desktop, filename)

    with open(filepath, "w") as pathTextFile:                           #creating the textfile
        for nodeNumber in path:
            pathTextFile.write(f"{nodeNumber}\n")

    print(f"Route written to disk as {inputBasename}_SOLUTION_{distanceTraveled}.txt")
    return filepath