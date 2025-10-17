import os

from geneticAlg import run_algorithm
from tspOutputFileMaker import routeFileCreator
from DataVis import routeDisplay

def main():
    print("===Drone Route Optimization Program===")
    filename = input("Enter the name of the input file: ").strip()

    input_folder = "InputCordsFolder"
    file_path = os.path.join(input_folder, filename)

    if not os.path.exists(file_path):
        print(f"[ERROR] '{file_path}' not found.")
        return

    print(f"[Info] Found input file: {file_path}")



if __name__ == "__main__":
    main()

