'''
HERE YOU TAKE THE INPUT OF THE distanceNN and distanceNNRand and the time and the iterations total number
and basically take those inputs and create a matplotlib image and then we basically output that in a new folder
called "GraphDiff" or whatever you want to call it. Then we return back to main where we end the program.
'''

import os
import matplotlib.pyplot as plt
import numpy as np

def smooth(y, window_size=10):  #return a smoothed version of y using a moving average
    if len(y) < window_size:
        return y
    return np.convolve(y, np.ones(window_size)/window_size, mode='valid')

def createGraph(distanceNNRand,distanceNN,total_time,total_iterations,filename):
    output_folder = "GraphDiff"
    os.makedirs(output_folder,exist_ok = True)

    #assign values
    rand_distances = [d[0] for d in distanceNNRand]
    rand_iters = [d[1] for d in distanceNNRand]
    rand_times = [d[2] for d in distanceNNRand]

    normal_distances = [d[0] for d in distanceNN]
    normal_iters = [d[1] for d in distanceNN]
    normal_times = [d[2] for d in distanceNN]

    window_size = 40
    rand_distances_smooth = smooth(rand_distances, window_size)
    rand_times_smooth = rand_times[:len(rand_distances_smooth)]

    normal_distances_smooth = smooth(normal_distances, window_size)
    normal_times_smooth = normal_times[:len(normal_distances_smooth)]




    plt.figure(figsize = (10,6))
    plt.plot(rand_times_smooth,rand_distances_smooth,label = "Randomized NN", color ="orange")
    plt.plot(normal_times_smooth,normal_distances_smooth,label = "Normal NN", color ="blue")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Route Distance")
    plt.title("Comparison of Randomized vs. Normal NN")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    #save the plot
    base_name = os.path.splitext(os.path.basename(filename))[0]
    output_path = os.path.join(output_folder, f"{base_name}_NN_Comparison.png")
    plt.savefig(output_path)
    plt.close()

    print(f"[Graph saved]{output_path}")
    return output_path
