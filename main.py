import os

from geneticAlg import run_algorithm
from tspOutputFileMaker import routeFileCreator
from DataVis import routeDisplay

def main():
    print("===Drone Route Optimization Program===")
    filename = input("Enter the name of the input file: ").strip()

    input_folder = "InputCordsFolder"
    file_path = os.path.join(input_folder, filename)

    if not os.path.exists(file_path): #incase file doesnt exist
        print(f"[ERROR] '{file_path}' not found.")
        return

    #print(f"Drop locations found within input file: {file_path}")

    print("Running Genetic Algorithm...")

    config= {} #empty config for now
    best_route, total_distance = run_algorithm(file_path, config) #assigns local variable to the returned tuple and the total distance

    if best_route is None or total_distance is None: #incase algorithm fails
        raise RuntimeError("Genetic algorithm failed to produce a result.")

    routeFileCreator(best_route, os.path.splitext(filename)[0], total_distance)

    routeDisplay(best_route, os.path.splitext(filename)[0], total_distance) 

    print(f"Algorithm completed. Distance traveled: {total_distance:.2f}")



if __name__ == "__main__":
    main()

