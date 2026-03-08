from InitialPhase_Setup import GridEnvironment
from GridDisplay import showGridWithPath
import numpy as np

if __name__ == "__main__":
    env = GridEnvironment()

    rows, cols, start_x, start_y, end_x, end_y, occupancy = env.getUserInput()

    grid, path, costGrid = env.generateValidEnvironment(rows, cols, start_x, start_y, end_x, end_y, occupancy)

    print("\nGenerated Grid (0=free, 1=obstacle, 2=start, 3=end):")
    for row in grid:
        print(*row)

    print("\nPath found! Steps:", len(path))
    print("Path (coordinates):", path)

    showGridWithPath(grid, path, start_x, start_y, end_x, end_y)