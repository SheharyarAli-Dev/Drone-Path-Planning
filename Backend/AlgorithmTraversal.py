import numpy as np
import heapq

def heuristic(current_x, current_y, end_x, end_y):
    return np.abs(current_x - end_x) + np.abs(current_y - end_y)

def PathFindingAlgorithmImplementation(grid, rows, cols, start_x, start_y, end_x, end_y):
    
    costGrid = np.full((rows, cols), np.inf)
    costGrid[start_x, start_y] = 0

    queue = []
    heapq.heappush(queue, (0, (start_x, start_y)))

    parent = {}
    parent[(start_x, start_y)] = None

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:

        currentCost, (current_x, current_y) = heapq.heappop(queue)

        if current_x == end_x and current_y == end_y:
            break

        for dx, dy in directions:
            neighbor_x = current_x + dx
            neighbor_y = current_y + dy

            if neighbor_x < 0 or neighbor_x >= rows:
                continue
            if neighbor_y < 0 or neighbor_y >= cols:
                continue

            if grid[neighbor_x, neighbor_y] == 1:
                continue

            new_cost = currentCost + 1
            if new_cost < costGrid[neighbor_x, neighbor_y]:

                costGrid[neighbor_x, neighbor_y] = new_cost
                
                h = heuristic(neighbor_x, neighbor_y, end_x, end_y)
                heapq.heappush(queue, (new_cost+h, (neighbor_x, neighbor_y)))

                parent[(neighbor_x, neighbor_y)] = (current_x, current_y)

    path = []
    current = (end_x, end_y)

    if current not in parent:
        return None, costGrid

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, costGrid

        
        
        
        
        
    

