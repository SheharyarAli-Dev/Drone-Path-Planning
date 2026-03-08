"""
app.py  —  Main Streamlit entry point.

Run:
    streamlit run Frontend/app.py

Layout:
    project/
    ├── Backend/
    │   ├── AlgorithmTraversal.py
    │   ├── GridDisplay.py
    │   ├── InitialPhase_Setup.py
    │   └── main.py
    └── Frontend/
        ├── app.py
        ├── ui_styles.py
        ├── sidebar_controls.py
        └── grid_visualizer.py
"""

import sys, os, time
import numpy as np
import streamlit as st

# ── Backend path ──────────────────────────────────────────────────────────────
BACKEND_PATH = os.path.join(os.path.dirname(__file__), "..", "Backend")
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

from AlgorithmTraversal import PathFindingAlgorithmImplementation

# ── Frontend modules ──────────────────────────────────────────────────────────
from ui_styles        import inject_custom_css, page_header
from sidebar_controls import render_sidebar
from grid_visualizer  import render_grid_figure, render_path_stats, render_path_table

# ── Page config  (must be first Streamlit call) ───────────────────────────────
st.set_page_config(
    page_title="Drone Path Planner",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_custom_css()

# ── Session state ─────────────────────────────────────────────────────────────
for k, v in {"grid": None, "path": None, "costGrid": None,
             "params": None, "attempts": 0, "elapsed": 0,
             "computed": False}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Sidebar ───────────────────────────────────────────────────────────────────
result = render_sidebar()
params, run = (None, False) if result is None else result

# ── Header ────────────────────────────────────────────────────────────────────
page_header()

# ── Compute ───────────────────────────────────────────────────────────────────
if run and params is not None:
    with st.spinner("Computing optimal path…"):
        counter = {"n": 0}

        def _generate(rows, cols, sx, sy, ex, ey, occ):
            counter["n"] = 0
            while True:
                counter["n"] += 1
                grid = np.zeros((rows, cols), dtype=int)
                rng  = np.random.random((rows, cols))
                grid[rng < (occ / 100)] = 1
                grid[sx, sy] = 0
                grid[ex, ey] = 0
                path, costGrid = PathFindingAlgorithmImplementation(
                    grid, rows, cols, sx, sy, ex, ey)
                if path is not None:
                    grid[sx, sy] = 2
                    grid[ex, ey] = 3
                    return grid, path, costGrid

        t0 = time.perf_counter()
        grid, path, costGrid = _generate(
            params["rows"], params["cols"],
            params["start_x"], params["start_y"],
            params["end_x"],   params["end_y"],
            params["occupied"],
        )
        elapsed = time.perf_counter() - t0

        st.session_state.update({
            "grid": grid, "path": path, "costGrid": costGrid,
            "params": params, "attempts": counter["n"],
            "elapsed": elapsed, "computed": True,
        })

# ── Results ───────────────────────────────────────────────────────────────────
if st.session_state.computed and st.session_state.grid is not None:
    p       = st.session_state.params
    grid    = st.session_state.grid
    path    = st.session_state.path
    cost    = st.session_state.costGrid
    att     = st.session_state.attempts
    elapsed = st.session_state.elapsed
    sx, sy  = p["start_x"], p["start_y"]
    ex, ey  = p["end_x"],   p["end_y"]

    # Stats + status banner
    render_path_stats(path, cost, p["rows"], p["cols"], att, elapsed)

    # Path map (full width)
    st.markdown('<div class="section-title">Path Map</div>', unsafe_allow_html=True)
    st.markdown('<div class="map-card">', unsafe_allow_html=True)
    fig = render_grid_figure(grid, path, sx, sy, ex, ey)
    st.pyplot(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Waypoints
    st.markdown("<br>", unsafe_allow_html=True)
    render_path_table(path)

else:
    # Empty / welcome state
    st.markdown("""
    <div class="empty-state">
        <svg width="56" height="56" viewBox="0 0 24 24" fill="none"
             stroke="#d1d5db" stroke-width="1.4" stroke-linecap="round">
            <circle cx="12" cy="12" r="10"/>
            <path d="M12 8v4l3 3"/>
        </svg>
        <h3>No results yet</h3>
        <p>Configure the grid in the sidebar and press <code>▶ Compute Path</code> to start.</p>
    </div>
    """, unsafe_allow_html=True)