from __future__ import annotations
import math
import random
import numpy as np


def euclideanDistance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))

