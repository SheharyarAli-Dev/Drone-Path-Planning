
def showGridWithPath(grid, path, start_x, start_y, end_x, end_y):
    """
    Displays the grid with:
    - S = Start
    - E = End
    - # = Obstacle
    - * = Path chosen
    - . = Free space
    """
    rows, cols = grid.shape
    
    display_grid = []

    for i in range(rows):
        row_display = []
        for j in range(cols):
            if i == start_x and j == start_y:
                row_display.append("S")
            elif i == end_x and j == end_y:
                row_display.append("E")
            elif grid[i, j] == 1:
                row_display.append("#")
            else:
                row_display.append(".")
        display_grid.append(row_display)

    if path:
        for x, y in path:
            if (x, y) != (start_x, start_y) and (x, y) != (end_x, end_y):
                display_grid[x][y] = "*"

    print("\nFinal Grid with Path:")
    for row in display_grid:
        print(" ".join(row))