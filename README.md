#  Autonomous Drone Path Planner

A grid-based autonomous path planning simulator built with Python. Uses the **A\* algorithm** with Manhattan heuristic to find the optimal route for a drone navigating through obstacle-filled environments — with a clean, professional Streamlit frontend.

---
## Preview
<img width="1919" height="908" alt="image" src="https://github.com/user-attachments/assets/8ea609d8-09b8-49e6-ad4a-d245ca3763ba" />

---
##  Overview

Application Deployed on streamlit, Visit: https://drone-path-planning.streamlit.app/
The application generates a random grid environment with configurable obstacle density, then computes the shortest path from a user-defined start position to an end position. The result is displayed on an interactive visual map showing the path, obstacles, and key statistics.

---

##  Project Structure

```
project/
│
├── Backend/
│   ├── AlgorithmTraversal.py     # A* pathfinding implementation
│   ├── InitialPhase_Setup.py     # Grid generation & environment setup
│   ├── GridDisplay.py            # Terminal grid display (ASCII)
│   └── main.py                   # CLI entry point
│
└── Frontend/
    ├── app.py                    # Streamlit app entry point
    ├── ui_styles.py              # CSS theme & page components
    ├── sidebar_controls.py       # User input controls
    └── grid_visualizer.py        # Path map & stats rendering
```

---

##  How It Works

### Algorithm — A\* with Manhattan Heuristic

The pathfinder uses the **A\* search algorithm**, which combines:

- **g(n)** — the actual cost from start to the current node
- **h(n)** — the heuristic estimate (Manhattan distance) to the goal
- **f(n) = g(n) + h(n)** — the priority used to explore nodes

Movement is **4-directional** (up, down, left, right). The algorithm is guaranteed to find the **shortest possible path** if one exists.

### Grid Generation

The environment is randomly generated with a configurable obstacle percentage (0–80%). The generator re-runs until it produces a grid where a valid path exists between the start and end points.

| Cell Value | Meaning       |
|:----------:|---------------|
| `0`        | Free cell     |
| `1`        | Obstacle      |
| `2`        | Start point   |
| `3`        | End point     |

---

##  Running the Application

### Prerequisites

- Python 3.8+
- pip

### Install Dependencies

```bash
pip install streamlit numpy matplotlib
```

### Run the Streamlit Frontend

```bash
streamlit run Frontend/app.py
```

### Run the CLI Backend (Terminal)

```bash
cd Backend
python main.py
```

---

##  Configuration Options

All parameters are set via the sidebar in the frontend (or prompted interactively in the CLI):

| Parameter         | Description                                      | Range         |
|-------------------|--------------------------------------------------|---------------|
| Rows              | Number of rows in the grid                       | 3 – 50        |
| Cols              | Number of columns in the grid                    | 3 – 50        |
| Start X / Y       | Row and column of the drone's start position     | Within grid   |
| End X / Y         | Row and column of the target destination         | Within grid   |
| Obstacle %        | Percentage of cells blocked by obstacles         | 0% – 80%      |

---

##  Output

After computing, the frontend displays:

- **Status banner** — path found / not found, compute time, and attempts
- **Stat cards** — steps taken, path cost, obstacle count, free cells, generation attempts
- **Path map** — visual grid with colour-coded cells, animated path trail, start (S) and end (E) markers
- **Waypoint list** — expandable list of every coordinate along the path

---

##  Backend Module Reference

### `AlgorithmTraversal.py`
Contains the core A\* implementation.

```python
PathFindingAlgorithmImplementation(grid, rows, cols, start_x, start_y, end_x, end_y)
# Returns: (path, costGrid)
# path     → list of (row, col) tuples from start to end, or None if no path exists
# costGrid → numpy array of g-costs for every visited cell
```

### `InitialPhase_Setup.py`
Contains the `GridEnvironment` class.

```python
env = GridEnvironment()
env.getUserInput()                  # Interactive CLI input with validation
env.generateValidEnvironment(...)   # Generates grid, retries until path exists
```

### `GridDisplay.py`
Terminal rendering of the solved grid.

```python
showGridWithPath(grid, path, start_x, start_y, end_x, end_y)
# Prints ASCII grid:  S = Start, E = End, # = Obstacle, * = Path, . = Free
```

---

##  Frontend Module Reference

| File | Responsibility |
|------|----------------|
| `app.py` | Page config, session state, orchestrates all modules |
| `ui_styles.py` | Global CSS, page header, reusable HTML components |
| `sidebar_controls.py` | Sidebar inputs with live validation |
| `grid_visualizer.py` | Matplotlib path map, stat cards, waypoint expander |

---

##  Notes

- The grid generator will retry automatically if the randomly placed obstacles block all routes between start and end.
- Obstacle density above 60% may require many retries to find a valid environment.
- The frontend preserves results in session state — changing sidebar values won't clear the map until **Compute Path** is pressed again.

---

##  License

This project is for demonstration purposes.
