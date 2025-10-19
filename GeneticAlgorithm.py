from __future__ import annotations
import math
import random
import numpy as np

def buildDistanceMatrix(points):
    X = np.asarray(points, dtype=float)
    diff = X[:,None,:] - X[None,:,:]
    return np.sqrt(np.sum(diff * diff, axis=2, dtype=float))

def tourLength(order, D, closed=True):
    a = order
    b = np.roll(order, -1) if closed else order[1:]
    if not closed:
        a = a[:-1]
    return float(np.sum(D[a,b]))

def nearestNeigborOrder(points=None,D=None,start=0):
    if (points is None) == (D is None):
        raise ValueError("Provide exactly one of points= or D=.")
    
    if D is None:
        D = buildDistanceMatrix(points)
    else:
        D = np.asarray(D, dtype=float)

    n = D.shape[0]
    order = np.empty(n, dtype=int)
    visited = np.zeros(n, dtype=bool)

    cur = int(start) % n
    order[0] = cur
    visited[cur] = True

    for i in range(1, n):
        drow = np.where(visited, np.inf, D[cur])
        nxt = int(np.argmin(drow))
        order[i] = nxt
        visited[nxt] = True
        cur = nxt

    return order