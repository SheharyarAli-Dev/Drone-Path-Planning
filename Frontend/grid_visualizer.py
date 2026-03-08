"""
grid_visualizer.py  —  Path map only, light professional style.
Removed: cost heatmap, text grid view.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import matplotlib.patheffects as pe
import streamlit as st


# ── Palette (light, professional) ────────────────────────────────────────────
BG_FIG    = "#ffffff"
BG_AX     = "#f8f9fc"
C_FREE    = "#f1f5f9"       # light slate — open cell
C_FREE_ED = "#e2e8f0"       # cell border
C_WALL    = "#334155"       # dark slate — obstacle (clean, not harsh red)
C_PATH_LN = "#2563eb"       # blue path line
C_PATH_DOT= "#3b82f6"       # intermediate waypoints
C_START   = "#16a34a"       # green start
C_END     = "#d97706"       # amber end
C_SHADOW  = "#94a3b8"       # subtle shadow colour


def render_grid_figure(grid, path, start_x, start_y, end_x, end_y):
    rows, cols = grid.shape

    cell_px   = 52          # pixel size per cell (before DPI scaling)
    fig_w     = max(7, cols * cell_px / 96)
    fig_h     = max(5, rows * cell_px / 96)

    fig, ax = plt.subplots(figsize=(fig_w, fig_h), facecolor=BG_FIG)
    ax.set_facecolor(BG_AX)
    ax.set_aspect("equal")

    # ── Draw cells ────────────────────────────────────────────────────────────
    for r in range(rows):
        for c in range(cols):
            is_wall = (grid[r, c] == 1)
            fc = C_WALL if is_wall else C_FREE
            ec = "#475569" if is_wall else C_FREE_ED
            lw = 0.0 if is_wall else 0.6

            rect = mpatches.FancyBboxPatch(
                (c + 0.05, r + 0.05), 0.9, 0.9,
                boxstyle="round,pad=0.04",
                facecolor=fc, edgecolor=ec,
                linewidth=lw, zorder=1
            )
            ax.add_patch(rect)

    # ── Path trail (gradient-like via alpha segments) ─────────────────────────
    if path and len(path) > 1:
        n = len(path)
        for i in range(n - 1):
            x0, y0 = path[i][1] + 0.5,   path[i][0] + 0.5
            x1, y1 = path[i+1][1] + 0.5, path[i+1][0] + 0.5
            progress = i / max(n - 2, 1)
            alpha = 0.35 + 0.65 * progress   # fade in toward destination
            ax.plot([x0, x1], [y0, y1],
                    color=C_PATH_LN, linewidth=3.5,
                    alpha=alpha, solid_capstyle="round",
                    solid_joinstyle="round", zorder=3)

        # Intermediate waypoint dots
        for i, (px, py) in enumerate(path[1:-1], 1):
            progress = i / max(n - 2, 1)
            ax.plot(py + 0.5, px + 0.5, "o",
                    color=C_PATH_DOT, markersize=5,
                    alpha=0.5 + 0.4 * progress,
                    markeredgecolor="white",
                    markeredgewidth=0.8, zorder=4)

    # ── Start marker ─────────────────────────────────────────────────────────
    ax.add_patch(mpatches.FancyBboxPatch(
        (start_y + 0.1, start_x + 0.1), 0.8, 0.8,
        boxstyle="round,pad=0.06",
        facecolor=C_START, edgecolor="white",
        linewidth=1.5, zorder=5
    ))
    ax.text(start_y + 0.5, start_x + 0.5, "S",
            ha="center", va="center",
            fontsize=max(7, min(13, 130 // max(rows, cols))),
            fontweight="bold", color="white", zorder=6,
            path_effects=[pe.withStroke(linewidth=2, foreground=C_START)])

    # ── End marker ────────────────────────────────────────────────────────────
    ax.add_patch(mpatches.FancyBboxPatch(
        (end_y + 0.1, end_x + 0.1), 0.8, 0.8,
        boxstyle="round,pad=0.06",
        facecolor=C_END, edgecolor="white",
        linewidth=1.5, zorder=5
    ))
    ax.text(end_y + 0.5, end_x + 0.5, "E",
            ha="center", va="center",
            fontsize=max(7, min(13, 130 // max(rows, cols))),
            fontweight="bold", color="white", zorder=6,
            path_effects=[pe.withStroke(linewidth=2, foreground=C_END)])

    # ── Axes cleanup ──────────────────────────────────────────────────────────
    ax.set_xlim(0, cols)
    ax.set_ylim(rows, 0)

    # Row / col tick labels
    ax.set_xticks(np.arange(0.5, cols, 1))
    ax.set_xticklabels(range(cols), fontsize=7, color="#9ca3af",
                       fontfamily="monospace")
    ax.set_yticks(np.arange(0.5, rows, 1))
    ax.set_yticklabels(range(rows), fontsize=7, color="#9ca3af",
                       fontfamily="monospace")
    ax.tick_params(length=0, pad=4)

    for sp in ax.spines.values():
        sp.set_edgecolor("#e5e7eb")
        sp.set_linewidth(1)

    # ── Legend ────────────────────────────────────────────────────────────────
    legend_items = [
        mpatches.Patch(facecolor=C_START, edgecolor="white", label="Start (S)"),
        mpatches.Patch(facecolor=C_END,   edgecolor="white", label="End (E)"),
        mpatches.Patch(facecolor=C_PATH_LN, label="Path"),
        mpatches.Patch(facecolor=C_WALL,  label="Obstacle"),
        mpatches.Patch(facecolor=C_FREE,  edgecolor=C_FREE_ED, label="Free cell"),
    ]
    leg = ax.legend(
        handles=legend_items,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.06),
        ncol=5,
        fontsize=8,
        frameon=True,
        facecolor="white",
        edgecolor="#e5e7eb",
        labelcolor="#374151",
        handlelength=1.1,
        handleheight=0.9,
        borderpad=0.7,
        columnspacing=1.2,
    )
    leg.get_frame().set_linewidth(0.8)

    fig.tight_layout(rect=[0, 0.06, 1, 1])
    return fig


# ── Stats ─────────────────────────────────────────────────────────────────────
def render_path_stats(path, costGrid, rows, cols, attempts, elapsed):
    if path is None:
        st.markdown("""
        <div class="banner-err">
            ✖ &nbsp; No path found — try reducing obstacle density or enlarging the grid.
        </div>
        """, unsafe_allow_html=True)
        return

    total = rows * cols
    free  = int(np.sum(np.isfinite(costGrid)))
    obs   = total - free
    cost  = int(costGrid[path[-1][0], path[-1][1]])

    st.markdown(f"""
    <div class="banner-ok">
        ✔ &nbsp; Path found in <b>{attempts}</b> attempt(s) &nbsp;·&nbsp; computed in <b>{elapsed*1000:.0f} ms</b>
    </div>

    <div class="stat-grid">
        <div class="stat-card">
            <div class="stat-val sv-blue">{len(path)}</div>
            <div class="stat-lbl">Steps</div>
        </div>
        <div class="stat-card">
            <div class="stat-val sv-gray">{cost}</div>
            <div class="stat-lbl">Path Cost</div>
        </div>
        <div class="stat-card">
            <div class="stat-val sv-red">{obs}</div>
            <div class="stat-lbl">Obstacles</div>
        </div>
        <div class="stat-card">
            <div class="stat-val sv-green">{free}</div>
            <div class="stat-lbl">Free Cells</div>
        </div>
        <div class="stat-card">
            <div class="stat-val sv-amber">{attempts}</div>
            <div class="stat-lbl">Attempts</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Waypoints ─────────────────────────────────────────────────────────────────
def render_path_table(path):
    if not path:
        return
    with st.expander(f"View all {len(path)} waypoints"):
        html = ""
        for i, (px, py) in enumerate(path):
            if i == 0:
                cls, lbl = "start", "Start"
            elif i == len(path) - 1:
                cls, lbl = "end", "End"
            else:
                cls, lbl = "", f"#{i}"
            html += f"""
            <div class="wp-chip {cls}">
                <div class="wp-coord">({px}, {py})</div>
                <div class="wp-label">{lbl}</div>
            </div>"""
        st.markdown(f'<div style="display:flex;flex-wrap:wrap;gap:0.2rem;">{html}</div>',
                    unsafe_allow_html=True)