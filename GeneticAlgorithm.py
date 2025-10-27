from __future__ import annotations
import math
import random
import numpy as np

# Computes the distance between points and returns it
def buildDistanceMatrix(points):
    # Converting the input points into a numpy array as float points
    pointsArr = np.asarray(points, dtype=float)
    # Computing the full pairwise Euclidean distance matrix between all points using NumPy broadcasting
    return np.linalg.norm(pointsArr[:,None,:] - pointsArr[None,:,:], axis = 2)

# Computing the total distance of a closed tour path through a set of points that returns to the start point always
def tourLength(pointsOrder, distanceMatrix):
    # Represents the start index of each leg of the tour
    a = pointsOrder
    # Destination index of each leg being calculated wrapping back to first node
    b = np.roll(pointsOrder, -1)
    # Returning the total tour length in float
    return float(np.sum(distanceMatrix[a,b]))


def nearestNeigborOrder(points=None,distanceMatrix=None):

    # Checking if one input is atleast given which is points or the distanceMatrix 
    if (points is None) == (distanceMatrix is None):
        raise ValueError("Provide exactly one of points= or distanceMatrix=.")
    
    # Computes the distance between points if we dont have one
    if distanceMatrix is None:
        distanceMatrix = buildDistanceMatrix(points)
    else:
        distanceMatrix = np.asarray(distanceMatrix, dtype=float)

    # Getting the total number of points we have from the file
    totalRows = distanceMatrix.shape[0]
    # Initalizing arrays to track the order of points and visited nodes
    order = np.empty(totalRows, dtype=int)
    visited = np.zeros(totalRows, dtype=bool)

    cur = 0
    order[0] = cur
    visited[cur] = True

    # Iterating over all the nodes
    for i in range(1, totalRows):
        # Finding the distance from current point to rest of the point and if 
        # visited then we set it to infinity to ignore it
        drow = np.where(visited, np.inf, distanceMatrix[cur])

        # Calculating the number of univisted points left
        remainingNodes = totalRows - np.sum(visited)
        # Random selection done between 3 or fewer nodes left
        numNodeRandSelect = min(3, remainingNodes)
        # Partially rearranging the 3 closest nodes and returning it without fully sorting all the distances
        candIdx = np.argpartition(drow, numNodeRandSelect-1)[:numNodeRandSelect]

        actualDistance = drow[candIdx].astype(float)
        # Calculating the inverse distance weights aka higher weight means closer
        w = 1.0/ (actualDistance + 1.e-12)
        # Setting the visited infinity nodes weights to 0
        w[np.isinf(w)] = 0.0
        # Calculating the total weight
        totalWeight = w.sum()

        # If total weight is 0 then we fall back to uniform random choice
        if totalWeight == 0.0:
            w = np.ones_like(w) / len(w)
        else:
            # Normalizing the weights to sum to 1
            w = w / totalWeight

        # Randomly chooses one next point from the candidates.
        nxt = int(random.choices(list(candIdx), weights=list(w), k=1)[0])
        order[i] = nxt
        visited[nxt] = True
        cur = nxt
        
    return order

def solveTSPNN(points, returnPoints = False):

    points = np.asarray(points, dtype=float)
    distanceMatrix = buildDistanceMatrix(points)

    # Force start at the first input point (index 0)
    order = nearestNeigborOrder(distanceMatrix=distanceMatrix)

    # Explicitly return to start in the output
    order_closed = np.concatenate([order, order[:1]])

    return (points[order_closed] if returnPoints else order_closed)