import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page Setup
st.set_page_config(page_title="Lanthanide Chemistry Dashboard", layout="wide")

st.title("🧪 Interactive Lanthanide Chemistry Suite")
st.markdown("""
An interactive platform modeling core $4f$ principles: **periodic contraction, basicity trends, ion colors, 3D coordination polyhedra, and industrial extraction from ore.**
""")

# Create 3 Tabs
tab1, tab2, tab3 = st.tabs(["🧩 Periodic Grid & Basicity", "🎨 Colors & 3D Coordination Shapes", "⛏️ Ore Processing & Extraction"])

# --- TAB 1: INTERACTIVE PERIODIC TABLE GRID & BASICITY ---
with tab1:
    st.subheader("1. Periodic Table Grid: Lanthanide Contraction & Basicity")
    st.markdown("""
    Explore the $4f$ series below. Color shading reflects **ionic radius contraction** across $\text{La}^{3+} \\rightarrow \text{Lu}^{3+}$.
    """)

    data = {
        "Element": ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"],
        "Name": ["Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium"],
        "Z": list(range(57, 72)),
        "Config": ["4f⁰", "4f¹", "4f²", "4f³", "4f⁴", "4f⁵", "4f⁶", "4f⁷", "4f⁸", "4f⁹", "4f¹⁰", "4f¹¹", "4f¹²", "4f¹³", "4f¹⁴"],
        "Radius": [103.2, 101.0, 99.0, 98.3, 97.0, 95.8, 94.7, 93.8, 92.3, 91.2, 90.1, 89.0, 88.0, 86.8, 86.1],
        "pH": [8.35, 7.60, 7.35, 7.00, 6.85, 6.75, 6.60, 6.55, 6.50, 6.40, 6.35, 6.30, 6.25, 6.20, 6.15],
        "Basicity": ["Most Basic", "Very High", "High", "High", "Moderate", "Moderate", "Moderate", "Moderate", "Low", "Low", "Low", "Low", "Very Low", "Very Low", "Least Basic"]
    }
    df = pd.DataFrame(data)

    # Render Periodic Table Row as Grid Cards using Columns
    st.markdown("### ⚛️ The $4f$ Lanthanide Series ($Z = 57$ to $71$):")
    
    # Render 15 Element Squares horizontally in a styled responsive layout
    cols = st.columns(15)
    for idx, row in df.iterrows():
        with cols[idx]:
            # Heatmap color scale calculation (Blue to Purple)
            val_norm = (row['Radius'] - 86.1) / (103.2 - 86.1)
            bg_color = f"rgba({int(40 + 180 * (1 - val_norm))}, {int(100 + 50 * val_norm)}, {int(200 + 55 * val_norm)}, 0.25)"
            border_color = f"rgb({int(40 + 180 * (1 - val_norm))}, 120, 220)"
            
            st.markdown(f"""
            <div style="
                border: 2px solid {border_color}; 
                border-radius: 8px; 
                padding: 6px; 
                text-align: center; 
                background-color: {bg_color};
                margin-bottom: 10px;">
                <span style="font-size: 10px; color: #888;">{row['Z']}</span><br/>
                <strong style="font-size: 18px;">{row['Element']}</strong><br/>
                <span style="font-size: 11px; color: #555;">{row['Radius']} pm</span><br/>
                <span style="font-size: 9px; color: #888;">{row['Config']}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Interactive Detail Inspector
    col_left, col_right = st.columns([1, 2])

    with col_left:
        selected_elem = st.selectbox("🔍 Select an element to inspect its properties:", df["Element"], index=0)
        elem_data = df[df["Element"] == selected_elem].iloc[0]

        st.info(f"""
        **Element Details: {elem_data['Name']} ({elem_data['Element']})**
        * **Atomic Number ($Z$):** {elem_data['Z']}
        * **$4f$ Electronic Config:** [{elem_data['Config']}]
        * **Ionic Radius ($\text{{Ln}}^{{3+}}$):** {elem_data['Radius']} pm
        * **Hydroxide Precipitation $\text{{pH}}$:** {elem_data['pH']}
        * **Relative Basicity:** {elem_data['Basicity']}
        """)

    with col_right:
        # Styled Visual Comparison Chart for Radius & Basicity pH
        fig_bar = go.Figure()
        
        # Highlight selected element in the bar chart
        colors = ['#1f77b4' if elem != selected_elem else '#ff7f0e' for elem in df["Element"]]
        
        fig_bar.add_trace(go.Bar(
            x=df["Element"],
            y=df["Radius"],
            name="Ionic Radius (pm)",
            marker_color=colors,
            text=df["Radius"],
            textposition="auto"
        ))

        fig_bar.update_layout(
            title="Ionic Radius Contraction Across $4f$ Series (Selected Element Highlighted)",
            xaxis_title="Lanthanide Element",
            yaxis_title="Ionic Radius (pm)",
            yaxis=dict(range=[80, 110]),
            height=350,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")
    st.markdown("""
    💡 **Basicity Trend Rule:** Larger light lanthanides ($\text{La}^{3+}$) have higher ionic character and form the most basic hydroxides ($\text{pH} \\approx 8.35$). 
    Smaller heavy lanthanides ($\text{Lu}^{3+}$) have higher charge density, increased covalent bond character, and lower basicity ($\text{pH} \\approx 6.15$).
    """)

# --- TAB 2: COLORS & 3D COORDINATION SHAPES ---
with tab2:
    st.subheader("🎨 Lanthanide Colors & 3D Coordination Geometries")
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### Aqueous Ion Colors ($3+$)")
        st.markdown("Colors arise from parity-forbidden **$f\\text{--}f$ transitions**. Ions with $f^0$ ($\text{La}^{3+}$), $f^7$ ($\text{Gd}^{3+}$), or $f^{14}$ ($\text{Lu}^{3+}$) configuration are colorless.")
        
        color_data = {
            "Ion": ["La3+", "Ce3+", "Pr3+", "Nd3+", "Sm3+", "Eu3+", "Gd3+", "Tb3+", "Dy3+", "Ho3+", "Er3+", "Tm3+", "Yb3+", "Lu3+"],
            "f-config": ["4f0", "4f1", "4f2", "4f3", "4f5", "4f6", "4f7", "4f8", "4f9", "4f10", "4f11", "4f12", "4f13", "4f14"],
            "Observed Color": ["Colorless", "Colorless/UV", "Green", "Pink / Lilac", "Pale Yellow", "Pale Pink", "Colorless", "Pale Pink", "Pale Yellow", "Yellow", "Pink", "Pale Blue", "Colorless", "Colorless"]
        }
        st.dataframe(pd.DataFrame(color_data), height=400, use_container_width=True)

    with col2:
        st.markdown("### Interactive 3D Coordination Polyhedra Viewer")
        st.markdown("Select a coordination number ($\text{CN}$) to rotate and inspect the 3D geometric polyhedra commonly adopted by lanthanide complexes:")
        
        shape_choice = st.selectbox(
            "Select Coordination Number (CN) & Geometry:",
            ["CN = 6: Octahedron", "CN = 8: Square Antiprism", "CN = 9: Tricapped Trigonal Prism", "CN = 12: Icosahedron"]
        )

        def generate_3d_shape(shape):
            fig_3d = go.Figure()
            # Central Metal Ion
            fig_3d.add_trace(go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers+text',
                marker=dict(size=14, color='gold'),
                name='Ln3+ Metal Center',
                text=['Ln3+'], textposition='top center'
            ))
            
            coords = []
            shape_title = ""
            
            if "CN = 6" in shape:
                shape_title = "CN = 6: Octahedral Geometry"
                coords = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]
            elif "CN = 8" in shape:
                shape_title = "CN = 8: Square Antiprism Geometry"
                coords = [
                    [1,1,0.7], [-1,1,0.7], [-1,-1,0.7], [1,-1,0.7],
                    [1.4,0,-0.7], [0,1.4,-0.7], [-1.4,0,-0.7], [0,-1.4,-0.7]
                ]
            elif "CN = 9" in shape:
                shape_title = "CN = 9: Tricapped Trigonal Prism"
                coords = [
                    [0.8, 0, 1], [-0.4, 0.7, 1], [-0.4, -0.7, 1],
                    [0.8, 0, -1], [-0.4, 0.7, -1], [-0.4, -0.7, -1],
                    [1.1, 0, 0], [-0.6, 1.0, 0], [-0.6, -1.0, 0]
                ]
            elif "CN = 12" in shape:
                shape_title = "CN = 12: Icosahedron Geometry"
                phi = (1 + 5**0.5) / 2
                coords = [
                    [-1, phi, 0], [1, phi, 0], [-1, -phi, 0], [1, -phi, 0],
                    [0, -1, phi], [0, 1, phi], [0, -1, -phi], [0, 1, -phi],
                    [phi, 0, -1], [phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1]
                ]

            coords = np.array(coords)
            
            fig_3d.add_trace(go.Scatter3d(
                x=coords[:,0], y=coords[:,1], z=coords[:,2],
                mode='markers',
                marker=dict(size=8, color='deepskyblue'),
                name='Ligands (L)'
            ))

            for c in coords:
                fig_3d.add_trace(go.Scatter3d(
                    x=[0, c[0]], y=[0, c[1]], z=[0, c[2]],
                    mode='lines',
                    line=dict(color='gray', width=3),
                    showlegend=False
                ))

            fig_3d.update_layout(
                title=shape_title,
                scene=dict(
                    xaxis=dict(visible=False),
                    yaxis=dict(visible=False),
                    zaxis=dict(visible=False)
                ),
                margin=dict(l=0, r=0, b=0, t=30),
                height=450
            )
            return fig_3d

        st.plotly_chart(generate_3d_shape(shape_choice), use_container_width=True)

# --- TAB 3: ORE PROCESSING & EXTRACTION ---
with tab3:
    st.subheader("⛏️ Extraction Methods from Major Ores")
    
    st.markdown("""
    ### 1. Primary Ores
    * **Bastnäsite ($\text{LnFCO}_3$):** Fluorocarbonate ore, rich in light lanthanides ($\text{Ce}, \text{La}, \text{Nd}$).
    * **Monazite ($\text{LnPO}_4$):** Phosphate ore containing thorium ($\text{Th}$), rich in light lanthanides.
    * **Xenotime ($\text{YPO}_4$):** Phosphate ore, rich in heavy lanthanides ($\text{Dy}, \text{Yb}, \text{Lu}$) and Yttrium.

    ---
    ### 2. Ore Cracking & Digestion
    * **Acid Digestion:** Concentrated $\text{H}_2\text{SO}_4$ treatment at 200°C converts phosphate ores into water-soluble sulfate salts.
    * **Alkali Leaching:** Hot concentrated $\text{NaOH}$ converts phosphate ores into hydroxides $\text{Ln(OH)}_3$, removing soluble sodium phosphate ($\text{Na}_3\text{PO}_4$).

    ---
    ### 3. Separation Techniques
    1. **Selective Oxidation/Reduction:** 
       * Oxidizing $\text{Ce}^{3+} \\rightarrow \text{Ce}^{4+}$ allows easy precipitation as $\text{CeO}_2$ or insoluble hydroxides away from trivalent ions.
       * Reducing $\text{Eu}^{3+} \\rightarrow \text{Eu}^{2+}$ allows selective precipitation as insoluble sulfate ($\text{EuSO}_4$).
    2. **Liquid-Liquid Solvent Extraction:** Continuous counter-current extraction using organophosphorus extractants (e.g., **D2EHPA**, **PC88A**) separating ions based on small differences in complex stability driven by ionic contraction.
    """)
