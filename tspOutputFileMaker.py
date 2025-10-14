import os
from math import ceil

def routeFileCreator(path, inputBasename, D, outDir):

    distanceTraveled = ceil(D)                                        #rounding D up because D may have decimals
    filename = f"{inputBasename}_SOLUTION_{distanceTraveled}.txt"
    filepath = os.path.join(outDir, filename)

    with open(filepath, "w") as pathTextFile:                           #creating the textfile
        for nodeNumber in path:
            pathTextFile.write(f"{nodeNumber}\n")

    return filepath