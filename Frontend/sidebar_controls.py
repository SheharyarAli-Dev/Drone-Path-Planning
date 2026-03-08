"""
sidebar_controls.py  —  Clean sidebar inputs, light theme.
"""
import streamlit as st


def _sec(text):
    st.markdown(f'<div class="sb-section">{text}</div>', unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div class="sb-brand">🛸 Path Planner</div>
        <div class="sb-brand-sub">Autonomous Drone Navigation</div>
        """, unsafe_allow_html=True)

        _sec("Grid Size")
        c1, c2 = st.columns(2)
        rows = c1.number_input("Rows", min_value=3, max_value=50, value=10, step=1)
        cols = c2.number_input("Cols", min_value=3, max_value=50, value=10, step=1)

        _sec("Start Position")
        c3, c4 = st.columns(2)
        start_x = c3.number_input("Row (X)", min_value=0, max_value=int(rows)-1, value=0,           step=1, key="sx")
        start_y = c4.number_input("Col (Y)", min_value=0, max_value=int(cols)-1, value=0,           step=1, key="sy")

        _sec("End Position")
        c5, c6 = st.columns(2)
        end_x = c5.number_input("Row (X)", min_value=0, max_value=int(rows)-1, value=int(rows)-1,  step=1, key="ex")
        end_y = c6.number_input("Col (Y)", min_value=0, max_value=int(cols)-1, value=int(cols)-1,  step=1, key="ey")

        _sec("Obstacle Density")
        occupied = st.slider("Obstacle %", 0, 80, 25, 5)
        st.caption(f"{occupied}% of cells will be blocked as obstacles")

        error = None
        if (start_x, start_y) == (end_x, end_y):
            error = "Start and End positions must be different."
        if error:
            st.error(f"⚠ {error}")

        st.markdown("<br>", unsafe_allow_html=True)
        run = st.button("▶  Compute Path", use_container_width=True)

        st.markdown("""
        <div class="sb-info">
            <b>Algorithm</b><br>
            A* with Manhattan heuristic<br><br>
            <b>Movement</b><br>
            4-directional (up, down, left, right)<br><br>
            <b>Guarantee</b><br>
            Always finds the shortest path if one exists.
        </div>
        """, unsafe_allow_html=True)

    if error:
        return None, False
    return {
        "rows": int(rows), "cols": int(cols),
        "start_x": int(start_x), "start_y": int(start_y),
        "end_x": int(end_x),     "end_y": int(end_y),
        "occupied": int(occupied),
    }, run