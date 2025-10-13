import os
from math import ceil

def routeFileCreator(path, input_basename, D, out_dir):

    distance_traveled = ceil(D)                                        #rounding D up because D may have decimals
    filename = f"{input_basename}_SOLUTION_{distance_traveled}.txt"
    filepath = os.path.join(out_dir, filename)

    with open(filepath, "w") as pathTextFile:                           #creating the textfile
        for nodeNumber in path:
            pathTextFile.write(f"{nodeNumber}\n")

    return filepath