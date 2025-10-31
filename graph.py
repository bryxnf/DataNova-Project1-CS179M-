'''
HERE YOU TAKE THE INPUT OF THE distanceNN and distanceNNRand and the time and the iterations total number
and basically take those inputs and create a matplotlib image and then we basically output that in a new folder
called "GraphDiff" or whatever you want to call it. Then we return back to main where we end the program.
'''

import os
import matplotlib.pyplot as plt

def createGraph(distanceNNRand,distanceNN,total_time,total_iterations):
    output_folder = "GraphDiff"
    os.makedirs(output_folder,exist_ok = True)

    #assign values
    rand_distances = [d[0] for d in distanceNNRand]
    rand_iters = [d[1] for d in distanceNNRand]
    rand_times = [d[2] for d in distanceNNRand]

    normal_distances = [d[0] for d in distanceNN]
    normal_iters = [d[1] for d in distanceNN]
    normal_times = [d[2] for d in distanceNN]

    plt.figure(figsize = (10,6))
    plt.plot(rand_times,rand_distances,label = "Randomized NN", color ="orange")
    plt.plot(normal_times,normal_distances,label = "Normal NN", color ="blue")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Route Distance")
    plt.title("Comparison of Randomized vs. Normal NN")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    #save the plot
    output_path = os.path.join(output_folder, " NN_Comparison.png")
    plt.savefig(output_path)
    plt.close()

    print(f"[Graph saved]{output_path}")
    return output_path
