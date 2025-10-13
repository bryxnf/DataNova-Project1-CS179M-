import matplotlib.pyplot as plt
import numpy as np
from math import ceil
import os

def routeDisplay(route, input_basename, D):     #route are the corrodinates in an array ex: [(1,2), (2, 4)]
    
    distance_traveled = ceil(D)   
    x_coordinates = [nodeCoordinates[0] for nodeCoordinates in route]
    y_coordinates = [nodeCoordinates[1] for nodeCoordinates in route]

    plt.figure(facecolor = 'lightblue')
    plt.plot(x_coordinates, y_coordinates, marker = "o")
    plt.scatter(x_coordinates[0], y_coordinates[0], color = 'red')   #the start and the end nodes of the line graph
    plt.title("Optimal Drone Route")
    plt.savefig(f"{input_basename}_SOLUTION_{distance_traveled}.jpg")