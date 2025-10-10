import numpy as np, random, operator, pandas as pd
# import matplotlib.pyplot as plt

def distance(i,j):
    '''
    Method calculate distance between two points if coordinates are passed
    i =(x,y) coordinates of first point
    j =(x,y) coordinates of second point
    '''
    #returning distance of points i and j 
    return np.sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2)