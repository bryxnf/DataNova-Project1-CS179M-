import matplotlib.pyplot as plt
from math import ceil
import os

def routeDisplay(route, inputBasename, D):     #route are the corrodinates in an array ex: [(1,2), (2, 4)]
    
    distanceTraveled = ceil(D)   
    xCoordinates = [nodeCoordinates[0] for nodeCoordinates in route]
    yCoordinates = [nodeCoordinates[1] for nodeCoordinates in route]
    xAxisMin, xAxisMax = min(xCoordinates), max(xCoordinates)
    yAxisMin, yAxisMax = min(yCoordinates), max(yCoordinates)
    xAxisRange, yAxisRange = xAxisMax - xAxisMin + 20, yAxisMax - yAxisMin + 20   #the length of x and y edges
    rangeRatio = xAxisRange / yAxisRange

    if rangeRatio >= 1:                                   #calculating which side is smaller
        height = 1920
        width = int(height * rangeRatio)
    else:
        width = 1920  
        height = int(width / rangeRatio)  

    widthConversion = width / 300                          #converting pixels to inches
    heightConversion = height / 300
    
    plt.figure(facecolor = "lightblue", figsize = (widthConversion, heightConversion))                                #background
    plt.plot(xCoordinates, yCoordinates, marker = "o", color = "black")               
    plt.scatter(xCoordinates[0], yCoordinates[0], color = "red")                               #the start and the end nodes of the line graph
    plt.title("Optimal Drone Route")    
    plt.xlim(xAxisMin - 10, xAxisMax + 10)                                                     #adding 10 pixel buffer between any point and the edges
    plt.ylim(yAxisMin - 10, yAxisMax + 10)        

    plt.savefig(f"{inputBasename}_SOLUTION_{distanceTraveled}.jpg", format = "jpeg", dpi = 300)   #saving it as a jpeg file