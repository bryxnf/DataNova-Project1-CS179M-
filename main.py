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
    best_route, total_distance = run_algorithm(file_path) #assigns local variable to the returned tupleand the total distance
    results = run_algorithm(file_path)

    if results is None: #incase algorithm fails
        raise RuntimeError("Genetic algorithm failed to produce a result.")
    best_route, total_distance = results

    print(f"Algorithm completed. Distance traveled: {total_distance:.2f}")



if __name__ == "__main__":
    main()

