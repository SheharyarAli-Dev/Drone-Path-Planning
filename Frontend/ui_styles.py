"""
ui_styles.py  —  Light, professional theme.
"""

def inject_custom_css():
    import streamlit as st
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

    /* ── Base ── */
    html, body,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background: #f8f9fc !important;
        color: #111827 !important;
        font-family: 'Geist', 'Inter', sans-serif;
    }
    [data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 1px solid #e5e7eb !important;
    }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1080px;
    }

    /* ── Page header ── */
    .page-title {
        font-size: 2rem;
        font-weight: 700;
        color: #0f172a;
        letter-spacing: -0.03em;
        line-height: 1.2;
        margin-bottom: 0.3rem;
    }
    .page-sub {
        font-size: 1rem;
        color: #6b7280;
        font-weight: 400;
        margin-bottom: 2rem;
    }
    .page-divider {
        height: 1px;
        background: #e5e7eb;
        margin: 1.5rem 0 2rem;
    }

    /* ── Sidebar labels ── */
    .sb-section {
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #9ca3af;
        margin: 1.4rem 0 0.4rem;
    }
    .sb-brand {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0f172a;
        letter-spacing: -0.02em;
        padding: 0.2rem 0 0.1rem;
    }
    .sb-brand-sub {
        font-size: 0.78rem;
        color: #9ca3af;
        margin-bottom: 1.2rem;
        padding-bottom: 1.2rem;
        border-bottom: 1px solid #f3f4f6;
    }
    .sb-info {
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 0.9rem 1rem;
        font-size: 0.8rem;
        color: #6b7280;
        line-height: 1.7;
        margin-top: 1.5rem;
    }
    .sb-info b { color: #374151; }

    /* ── Inputs ── */
    [data-testid="stNumberInput"] input {
        background: #ffffff !important;
        border: 1.5px solid #e5e7eb !important;
        border-radius: 8px !important;
        color: #111827 !important;
        font-family: 'Geist Mono', monospace !important;
        font-size: 0.9rem !important;
        padding: 0.45rem 0.7rem !important;
        transition: border-color 0.2s, box-shadow 0.2s;
    }
    [data-testid="stNumberInput"] input:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59,130,246,0.12) !important;
        outline: none !important;
    }
    label, .stSlider label {
        color: #374151 !important;
        font-size: 0.83rem !important;
        font-weight: 500 !important;
    }
    [data-testid="stSlider"] > div > div > div {
        background: #2563eb !important;
    }

    /* ── Primary Button ── */
    .stButton > button {
        width: 100%;
        background: #1d4ed8 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        font-family: 'Geist', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        padding: 0.72rem 1.4rem !important;
        letter-spacing: -0.01em;
        transition: background 0.18s, box-shadow 0.18s, transform 0.15s !important;
        box-shadow: 0 1px 3px rgba(29,78,216,0.25), 0 4px 12px rgba(29,78,216,0.15) !important;
    }
    .stButton > button:hover {
        background: #1e40af !important;
        box-shadow: 0 2px 6px rgba(29,78,216,0.3), 0 8px 20px rgba(29,78,216,0.2) !important;
        transform: translateY(-1px) !important;
    }
    .stButton > button:active {
        transform: translateY(0) !important;
        box-shadow: 0 1px 3px rgba(29,78,216,0.2) !important;
    }

    /* ── Stat cards ── */
    .stat-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 0.75rem;
        margin: 1.2rem 0 1.8rem;
    }
    .stat-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1rem 0.8rem;
        text-align: center;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04);
        transition: box-shadow 0.2s;
    }
    .stat-card:hover { box-shadow: 0 4px 16px rgba(0,0,0,0.08); }
    .stat-val {
        font-size: 1.9rem;
        font-weight: 700;
        letter-spacing: -0.04em;
        line-height: 1;
        margin-bottom: 0.3rem;
    }
    .stat-lbl {
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: #9ca3af;
    }
    .sv-blue  { color: #2563eb; }
    .sv-green { color: #059669; }
    .sv-red   { color: #dc2626; }
    .sv-gray  { color: #374151; }
    .sv-amber { color: #d97706; }

    /* ── Status banner ── */
    .banner-ok {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-left: 4px solid #16a34a;
        border-radius: 10px;
        padding: 0.85rem 1.2rem;
        font-size: 0.92rem;
        font-weight: 500;
        color: #15803d;
        margin-bottom: 0.5rem;
    }
    .banner-err {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        background: #fff1f2;
        border: 1px solid #fecdd3;
        border-left: 4px solid #dc2626;
        border-radius: 10px;
        padding: 0.85rem 1.2rem;
        font-size: 0.92rem;
        font-weight: 500;
        color: #b91c1c;
        margin-bottom: 0.5rem;
    }

    /* ── Section heading ── */
    .section-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: #111827;
        letter-spacing: -0.02em;
        margin-bottom: 0.8rem;
    }

    /* ── Map card wrapper ── */
    .map-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 1.4rem;
        box-shadow: 0 1px 6px rgba(0,0,0,0.05);
    }

    /* ── Expander ── */
    .streamlit-expanderHeader {
        font-size: 0.88rem !important;
        font-weight: 500 !important;
        color: #374151 !important;
    }

    /* ── Waypoint chips ── */
    .wp-chip {
        display: inline-flex;
        flex-direction: column;
        align-items: center;
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 0.4rem 0.7rem;
        margin: 0.2rem;
        font-family: 'Geist Mono', monospace;
    }
    .wp-coord { font-size: 0.82rem; font-weight: 500; color: #111827; }
    .wp-label { font-size: 0.62rem; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 0.1rem; }
    .wp-chip.start { background: #f0fdf4; border-color: #86efac; }
    .wp-chip.start .wp-coord { color: #16a34a; }
    .wp-chip.end   { background: #fffbeb; border-color: #fde68a; }
    .wp-chip.end   .wp-coord { color: #d97706; }

    /* ── Empty state ── */
    .empty-state {
        text-align: center;
        padding: 5rem 2rem;
        color: #d1d5db;
    }
    .empty-state svg { margin-bottom: 1.5rem; }
    .empty-state h3 { font-size: 1.15rem; font-weight: 600; color: #6b7280; margin-bottom: 0.4rem; }
    .empty-state p  { font-size: 0.9rem; color: #9ca3af; }
    .empty-state code {
        background: #f3f4f6;
        color: #2563eb;
        padding: 0.1rem 0.45rem;
        border-radius: 5px;
        font-size: 0.85rem;
    }
    </style>
    """, unsafe_allow_html=True)


def page_header():
    import streamlit as st
    st.markdown("""
    <div class="page-title">Drone Path Planner</div>
    <div class="page-sub">Autonomous navigation using A* algorithm with Manhattan heuristic</div>
    <div class="page-divider"></div>
    """, unsafe_allow_html=True)