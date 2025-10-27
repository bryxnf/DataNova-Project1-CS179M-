import matplotlib.pyplot as plt
from math import ceil
import os

def routeDisplay(route, inputBasename, D):     #route are the corrodinates in an array ex: [(1,2), (2, 4)]
    
    distanceTraveled = ceil(D)                 #rounding D up 
    xCoordinates = [nodeCoordinates[0] for nodeCoordinates in route]
    yCoordinates = [nodeCoordinates[1] for nodeCoordinates in route]
    xAxisMin, xAxisMax = min(xCoordinates), max(xCoordinates)
    yAxisMin, yAxisMax = min(yCoordinates), max(yCoordinates)
    xAxisRange, yAxisRange = xAxisMax - xAxisMin, yAxisMax - yAxisMin
    rangeRatio = xAxisRange / yAxisRange                                          #ratio to compare the sides of the jpg file

    if rangeRatio >= 1:                                   
        height = 1920
        width = ceil(rangeRatio * height)
    else:
        width = 1920  
        height = ceil(width / rangeRatio)

    widthConversion = width / 300                          #converting pixels to inches
    heightConversion = height / 300

    xBuffer = (xAxisRange / width) * 50                   #50 pixel buffers to fix edge problems
    yBuffer = (yAxisRange / height) * 50
    
    plt.figure(facecolor = "lightblue", figsize = (widthConversion, heightConversion))                                #background
    plt.axis("off")
    plt.plot(xCoordinates, yCoordinates, marker = "o", color = "black")               
    plt.scatter(xCoordinates[-1], yCoordinates[-1], s = 80, zorder = 5, color = "red")     #the start and the end nodes of the line graph
    plt.xlim(xAxisMin - xBuffer, xAxisMax + xBuffer)                                                     #adding 50 pixel buffer between any point and the edges
    plt.ylim(yAxisMin - yBuffer, yAxisMax + yBuffer)        

    output_folder = os.path.join(os.getcwd(), "OutputRoutes")
    os.makedirs(output_folder, exist_ok = True) 
    output_to_desktop = os.path.join(output_folder, f"{inputBasename}_SOLUTION_{distanceTraveled}.jpg")

    plt.savefig(output_to_desktop, format = "jpeg", dpi = 300)                     #saving it as a jpeg file
    plt.close()