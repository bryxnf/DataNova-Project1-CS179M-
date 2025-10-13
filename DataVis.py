import matplotlib.pyplot as plt
import numpy as np
from math import ceil
import os

def routeDisplay(route, input_basename, D):     #route are the corrodinates in an array ex: [(1,2), (2, 4)]
    
    distance_traveled = ceil(D)   
    x_coordinates = [nodeCoordinates[0] for nodeCoordinates in route]
    y_coordinates = [nodeCoordinates[1] for nodeCoordinates in route]
    xAxisMin, xAxisMax = min(x_coordinates), max(x_coordinates)
    yAxisMin, yAxisMax = min(y_coordinates), max(y_coordinates)

    plt.figure(facecolor = 'lightblue')                                #background
    plt.plot(x_coordinates, y_coordinates, marker = "o")               
    plt.scatter(x_coordinates[0], y_coordinates[0], color = 'red')     #the start and the end nodes of the line graph
    plt.title("Optimal Drone Route")    
    plt.xlim(xAxisMin - 10, xAxisMax + 10)                             #adding 10 pixel buffer between any point and the edges
    plt.ylim(yAxisMin - 10, yAxisMax + 10)        
    plt.savefig(f"{input_basename}_SOLUTION_{distance_traveled}.jpg")   #saving it as a jpeg file