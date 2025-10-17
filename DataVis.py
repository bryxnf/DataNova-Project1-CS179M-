# DataVis.py
import matplotlib.pyplot as plt
from math import ceil

def routeDisplay(route, inputBasename, D):
    """
    Draws the route path and saves it as a JPEG image.
    """
    distanceTraveled = ceil(D)
    xCoordinates = [node[0] for node in route]
    yCoordinates = [node[1] for node in route]

    xAxisMin, xAxisMax = min(xCoordinates), max(xCoordinates)
    yAxisMin, yAxisMax = min(yCoordinates), max(yCoordinates)
    xAxisRange, yAxisRange = xAxisMax - xAxisMin + 20, yAxisMax - yAxisMin + 20
    rangeRatio = xAxisRange / yAxisRange
    height, width = yAxisRange, xAxisRange

    if rangeRatio >= 1:
        height = 1920
    else:
        width = 1920

    widthConversion = width / 300
    heightConversion = height / 300

    plt.figure(facecolor="lightblue", figsize=(widthConversion, heightConversion))
    plt.plot(xCoordinates, yCoordinates, marker="o", color="black")
    plt.scatter(xCoordinates[0], yCoordinates[0], color="red")
    plt.title("Optimal Drone Route")
    plt.xlim(xAxisMin - 10, xAxisMax + 10)
    plt.ylim(yAxisMin - 10, yAxisMax + 10)
    plt.savefig(f"{inputBasename}_SOLUTION_{distanceTraveled}.jpg", format="jpeg", dpi=300)
    plt.close()
    print(f"[DataVis] Visualization saved: {inputBasename}_SOLUTION_{distanceTraveled}.jpg")
