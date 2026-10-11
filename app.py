
    import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page Setup
st.set_page_config(page_title="Lanthanide Chemistry Suite", layout="wide")

st.title("🧪 Advanced Lanthanide Chemistry Dashboard")
st.markdown("""
An interactive platform modeling core $4f$ principles: **periodic contraction, basicity trends, optical color palettes, 3D coordination polyhedra, and industrial hydrometallurgical ore extraction.**
""")

# Create 3 Tabs matching the overhauled layout
tab1, tab2, tab3 = st.tabs([
    "🧩 Periodic Grid & Size/Basicity", 
    "🎨 Optical Colors & 3D Coordination Geometries", 
    "⛏️ Ore Processing & Extraction Pipeline"
])

# --- DATASET ---
data = {
    "Element": ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"],
    "Name": ["Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium"],
    "Z": list(range(57, 72)),
    "Config": ["4f⁰", "4f¹", "4f²", "4f³", "4f⁴", "4f⁵", "4f⁶", "4f⁷", "4f⁸", "4f⁹", "4f¹⁰", "4f¹¹", "4f¹²", "4f¹³", "4f¹⁴"],
    "Radius": [103.2, 101.0, 99.0, 98.3, 97.0, 95.8, 94.7, 93.8, 92.3, 91.2, 90.1, 89.0, 88.0, 86.8, 86.1],
    "pH": [8.35, 7.60, 7.35, 7.00, 6.85, 6.75, 6.60, 6.55, 6.50, 6.40, 6.35, 6.30, 6.25, 6.20, 6.15],
    "Basicity": ["Most Basic", "Very High", "High", "High", "Moderate", "Moderate", "Moderate", "Moderate", "Low", "Low", "Low", "Low", "Very Low", "Very Low", "Least Basic"],
    "Color": ["Colorless", "Colorless", "Green", "Purple / Lilac", "Pink", "Yellow", "Pale Pink", "Colorless", "Pale Pink", "Pale Yellow", "Pink", "Pink", "Pale Blue", "Colorless", "Colorless"]
}
df = pd.DataFrame(data)

# --- TAB 1: PERIODIC GRID & SIZE / BASICITY ---
with tab1:
    st.subheader("1. The $4f$ Lanthanide Series ($Z = 57$ to $71$)")
    
    # Top Governing Factor Arrow Banner
    st.markdown("""
    <div style="background-color: #f0f2f6; border-left: 5px solid #1f77b4; padding: 12px; border-radius: 4px; margin-bottom: 20px;">
        <strong>Governing Trend Principle:</strong> 
        Lanthanide Contraction $\longrightarrow$ Increased Charge Density $\longrightarrow$ Decreased Basicity & Increased Covalent Character $\longrightarrow$ Lower Precipitation $\text{pH}$[cite: 19]
    </div>
    """, unsafe_allow_html=True)

    st.markdown("##### Click or Select an Element to Inspect Properties:")
    
    # Interactive Element Selection (Pills / Radio layout)
    selected_elem = st.pills("Elements", df["Element"].tolist(), default="La", label_visibility="collapsed")
    
    # Render 15 Element Squares Horizontally
    cols = st.columns(15)
    for idx, row in df.iterrows():
        with cols[idx]:
            val_norm = (row['Radius'] - 86.1) / (103.2 - 86.1)
            is_selected = (row['Element'] == selected_elem)
            bg_color = "rgba(31, 119, 180, 0.35)" if is_selected else f"rgba({int(40 + 180 * (1 - val_norm))}, {int(100 + 50 * val_norm)}, {int(200 + 55 * val_norm)}, 0.15)"
            border_color = "#ff7f0e" if is_selected else f"rgb({int(40 + 180 * (1 - val_norm))}, 120, 220)"
            
            st.markdown(f"""
            <div style="
                border: 2px solid {border_color}; 
                border-radius: 8px; 
                padding: 6px 2px; 
                text-align: center; 
                background-color: {bg_color};
                margin-bottom: 5px;">
                <span style="font-size: 9px; color: #888;">{row['Z']}</span><br/>
                <strong style="font-size: 16px;">{row['Element']}</strong><br/>
                <span style="font-size: 10px; color: #555;">{row['Radius']} pm</span>
            </div>
            """, unsafe_allow_html=True)

    # Display Selected Element Deep Dive Card
    elem_data = df[df["Element"] == selected_elem].iloc[0]
    
    st.markdown("---")
    col_card1, col_card2 = st.columns([1, 1])
    with col_card1:
        st.markdown(f"""
        ### 🔍 Element Profile: {elem_data['Name']} ({elem_data['Element']})
        * **Atomic Number ($Z$):** {elem_data['Z']}
        * **$4f$ Electronic Configuration:** [{elem_data['Config']}]
        * **Ionic Radius ($\text{{Ln}}^{{3+}}$):** {elem_data['Radius']} pm
        * **Hydroxide Precipitation $\text{{pH}}$:** {elem_data['pH']}[cite: 19]
        * **Basicity Category:** **{elem_data['Basicity']}**[cite: 19]
        """)
    with col_card2:
        st.markdown("""
        ### 📉 Visual Size Contraction Comparison
        Below is the relative proportional size representation of the lanthanide ions shrinking across the series from $\text{La}^{3+}$ to $\text{Lu}^{3+}$:
        """)
        # Proportional Visual Orbs representation
        orbs_html = "<div style='display: flex; align-items: center; gap: 4px; overflow-x: auto; padding: 10px 0;'>"
        for _, r in df.iterrows():
            size_px = int(max(14, (r['Radius'] / 103.2) * 35))
            highlight = "border: 2px solid #ff7f0e;" if r['Element'] == selected_elem else "border: 1px solid #ccc;"
            orbs_html += f"""
            <div style="text-align: center; min-width: 32px;">
                <div style="width: {size_px}px; height: {size_px}px; background: linear-gradient(135deg, #4682b4, #191970); border-radius: 50%; margin: 0 auto; {highlight}"></div>
                <span style="font-size: 9px; display: block; margin-top: 4px;">{r['Element']}</span>
            </div>
            """
        orbs_html += "</div>"
        st.markdown(orbs_html, unsafe_allow_html=True)

# --- TAB 2: OPTICAL COLORS & 3D COORDINATION GEOMETRIES ---
with tab2:
    st.subheader("🎨 Optical Color Palette ($f\text{--}f$ Transitions) & Symmetry")
    st.markdown("Colors arise from parity-forbidden $f\text{--}f$ transitions within deeply shielded $4f$ orbitals[cite: 58]. Ions follow the **$f^n$ and $f^{14-n}$ symmetry rule**[cite: 59].")

    # Visual Color Palette Swatch Grid Cards
    swatch_cols = st.columns(7)
    palette_data = [
        ("La³⁺", "4f⁰", "Colorless", "#f0f2f6"), ("Ce³⁺", "4f¹", "Colorless", "#e2e8f0"),
        ("Pr³⁺", "4f²", "Green", "#a7f3d0"), ("Nd³⁺", "4f³", "Purple / Lilac", "#e9d5ff"),
        ("Pm³⁺", "4f⁴", "Pink", "#fbcfe8"), ("Sm³⁺", "4f⁵", "Yellow", "#fef08a"),
        ("Eu³⁺", "4f⁶", "Pale Pink", "#fce7f3"), ("Gd³⁺", "4f⁷", "Colorless", "#f0f2f6"),
        ("Tb³⁺", "4f⁸", "Pale Pink", "#fce7f3"), ("Dy³⁺", "4f⁹", "Pale Yellow", "#fef9c3"),
        ("Ho³⁺", "4f¹⁰", "Pink", "#fbcfe8"), ("Er³⁺", "4f¹¹", "Pink", "#fbcfe8"),
        ("Tm³⁺", "4f¹²", "Pale Blue", "#bae6fd"), ("Yb³⁺", "4f¹³", "Colorless", "#e2e8f0"),
        ("Lu³⁺", "4f¹⁴", "Colorless", "#f0f2f6")
    ]
    
    for i, (ion, cfg, col_name, bg_hex) in enumerate(palette_data):
        with swatch_cols[i % 7]:
            st.markdown(f"""
            <div style="background-color: {bg_hex}; border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px; text-align: center; margin-bottom: 8px;">
                <strong>{ion}</strong><br/>
                <span style="font-size: 10px; color: #64748b;">{cfg}</span><br/>
                <span style="font-size: 11px; font-weight: 500;">{col_name}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📐 Spread-Out 3D Coordination Polyhedra & Slide Examples")
    st.markdown("Because lanthanide cations are large with open coordination spheres, **high coordination numbers ($\text{CN} = 6 \text{ to } 12$)** are standard[cite: 36].")

    # Stacked, spread-out layout for 3D shapes and slide examples
    shape_selection = st.selectbox(
        "Select Coordination Geometry to Inspect in 3D:",
        [
            "CN = 6: Octahedron (e.g., La(acac)₃)",
            "CN = 7: Monocapped Trigonal Prism (e.g., Ln₂O₃ B-type)",
            "CN = 8: Square Antiprism (e.g., CeF₄, [Ce(acac)₄])",
            "CN = 9: Tricapped Trigonal Prism (e.g., [Ln(H₂O)₉]³⁺)",
            "CN = 10: Bicapped Square Antiprism (e.g., [La(EDTA)(H₂O)₄])",
            "CN = 12: Icosahedron (e.g., [Ce(NO₃)₆]²⁻)"
        ]
    )

    def generate_3d_polyhedron(shape_str):
        fig = go.Figure()
        fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], mode='markers+text', marker=dict(size=16, color='gold'), text=['Ln³⁺ Metal Center'], textposition='top center'))
        coords = []
        if "CN = 6" in shape_str:
            coords = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]
        elif "CN = 7" in shape_str:
            coords = [[0.8,0,1], [-0.4,0.7,1], [-0.4,-0.7,1], [0.8,0,-1], [-0.4,0.7,-1], [-0.4,-0.7,-1], [1.2,0,0]]
        elif "CN = 8" in shape_str:
            coords = [[1,1,0.7], [-1,1,0.7], [-1,-1,0.7], [1,-1,0.7], [1.4,0,-0.7], [0,1.4,-0.7], [-1.4,0,-0.7], [0,-1.4,-0.7]]
        elif "CN = 9" in shape_str:
            coords = [[0.8,0,1], [-0.4,0.7,1], [-0.4,-0.7,1], [0.8,0,-1], [-0.4,0.7,-1], [-0.4,-0.7,-1], [1.1,0,0], [-0.6,1.0,0], [-0.6,-1.0,0]]
        elif "CN = 10" in shape_str:
            coords = [[1,1,1], [-1,1,1], [-1,-1,1], [1,-1,1], [1,1,-1], [-1,1,-1], [-1,-1,-1], [1,-1,-1], [0,1.5,0], [0,-1.5,0]]
        elif "CN = 12" in shape_str:
            phi = (1 + 5**0.5) / 2
            coords = [[-1,phi,0], [1,phi,0], [-1,-phi,0], [1,-phi,0], [0,-1,phi], [0,1,phi], [0,-1,-phi], [0,1,-phi], [phi,0,-1], [phi,0,1], [-phi,0,-1], [-phi,0,1]]
        
        coords = np.array(coords)
        fig.add_trace(go.Scatter3d(x=coords[:,0], y=coords[:,1], z=coords[:,2], mode='markers', marker=dict(size=9, color='deepskyblue'), name='Ligand Atoms'))
        for c in coords:
            fig.add_trace(go.Scatter3d(x=[0, c[0]], y=[0, c[1]], z=[0, c[2]], mode='lines', line=dict(color='gray', width=3), showlegend=False))
        fig.update_layout(scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False)), margin=dict(l=0, r=0, b=0, t=10), height=480)
        return fig

    st.plotly_chart(generate_3d_polyhedron(shape_selection), use_container_width=True)

# --- TAB 3: ORE PROCESSING & EXTRACTION PIPELINE ---
with tab3:
    st.subheader("⛏️ Visual Hydrometallurgical Extraction Pipeline")
    st.markdown("Step-by-step industrial processing of economic lanthanide ores based on lecture slides[cite: 4, 6, 8]:")

    # Visual Flow / Pipeline Layout using Containers & Columns
    with st.container():
        st.markdown("#### Step 1: Economic Ores Selection[cite: 4]")
        col_ore1, col_ore2 = st.columns(2)
        with col_ore1:
            st.info("🟢 **Monazite ($\text{LnPO}_4$)**\n* Phosphate ore containing Ce & La orthophosphates.\n* Contains $20\text{--}30\%$ Thorium dioxide ($\text{ThO}_2$)[cite: 4].\n* Found in India, Brazil, South Africa, Australia[cite: 5].")
        with col_ore2:
            st.info("🔵 **Bastnäsite ($\text{LnFCO}_3$)**\n* Fluorocarbonate ore rich in La, Ce, Nd[cite: 5].\n* Found in California, Sweden, Madagascar[cite: 5].")

    st.markdown("---")
    with st.container():
        st.markdown("#### Step 2: Cracking & Digestion Methods[cite: 6]")
        col_dig1, col_dig2 = st.columns(2)
        with col_dig1:
            st.markdown("##### 🧪 Monazite Digestion")
            st.markdown("* **Acid Route:** Treated with concentrated $\text{H}_2\text{SO}_4$ ($98\%$) at $120\text{--}150^\circ\text{C}$[cite: 7].\n* **Alkali Route:** Treated with hot $\text{NaOH}$ ($73\%$ at $140^\circ\text{C}$) to form insoluble $\text{Ln(OH)}_3$[cite: 8].")
        with col_dig2:
            st.markdown("##### ⚡ Bastnäsite Digestion")
            st.markdown("* **Roasting:** Air + heat roasting to remove $\text{CO}_2$ and yield $\text{LnF}_3$ / $\text{CeO}_2$[cite: 10].")

    st.markdown("---")
    with st.container():
        st.markdown("#### Step 3: Advanced Separation & Redox Techniques[cite: 18]")
        col_sep1, col_sep2 = st.columns(2)
        with col_sep1:
            st.markdown("""
            * **Cerium Isolation ($+4$ State):** Oxidizing $\text{Ce}^{3+} \rightarrow \text{Ce}^{4+}$ using permanganate or bromate, precipitating as $\text{CeO}_2$ or extracting via Tributyl Phosphate (TBP)[cite: 11, 26].
            * **Europium Isolation ($+2$ State):** Reducing $\text{Eu}^{3+} \rightarrow \text{Eu}^{2+}$ using zinc amalgam, precipitating as insoluble $\text{EuSO}_4$[cite: 27, 88].
            """)
        with col_sep2:
            st.markdown("""
            * **Solvent Extraction (TBP):** Distributing $\text{Ln}^{3+}$ between aqueous $\text{HNO}_3$ and organic Tributyl Phosphate[cite: 23].
            * **Ion-Exchange Chromatography:** Cation-exchange resin columns with $-\text{SO}_3\text{H}$ groups and complexing eluants ($\text{EDTA}$, Citrate). Heavier ions ($\text{Lu}^{3+}$) elute first[cite: 28, 29, 31].
            """)
