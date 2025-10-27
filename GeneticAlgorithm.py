from __future__ import annotations
import math
import random
import numpy as np

# Computes the distance between two points and returns it
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

def nearestNeigborOrder(points=None,D=None,start=0,*,randomStart=1,rng=None):
    if (points is None) == (D is None):
        raise ValueError("Provide exactly one of points= or D=.")
    
    if D is None:
        D = buildDistanceMatrix(points)
    else:
        D = np.asarray(D, dtype=float)

    rng = rng or random

    n = D.shape[0]
    order = np.empty(n, dtype=int)
    visited = np.zeros(n, dtype=bool)

    cur = int(start) % n
    order[0] = cur
    visited[cur] = True

    randomStart = max(1, min(int(randomStart),n))

    for i in range(1, n):
        drow = np.where(visited, np.inf, D[cur])
        if randomStart == 1:
            nxt = int(np.argmin(drow))
        else:
            remaning = np.sum(~visited)
            kk = min(randomStart, remaning)
            candIdx = np.argpartition(drow, kk-1)[:kk]
            dd = drow[candIdx].astype(float)
            w = 1.0/ (dd + 1.e-12)
            w[np.isinf(w)] = 0.0
            w = w/ w.sum()
            nxt = int(rng.choices(list(candIdx), weights=list(w), k=1)[0])
        order[i] = nxt
        visited[nxt] = True
        cur = nxt

    return order

def solveTSPNN(points, start= 0, returnPoints = False,*, randomStart=1, seed=None):
    rng = random.Random(seed)
    points = np.asarray(points, dtype=float)
    D = buildDistanceMatrix(points)

    # Force start at the first input point (index 0)
    order = nearestNeigborOrder(D=D, start=0, randomStart=randomStart, rng=rng)

    # Explicitly return to start in the output
    order_closed = np.concatenate([order, order[:1]])

    return (points[order_closed] if returnPoints else order_closed)