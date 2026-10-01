import streamlit as st
import pandas as pd
import plotly.express as px

# Page Setup
st.set_page_config(page_title="Lanthanide Chemistry Dashboard", layout="wide")

st.title("🧪 Lanthanide Chemistry: Trends, Colors, Geometries & Extraction")
st.markdown("""
An interactive dashboard modeling core lanthanide principles: **periodic contraction, basicity trends, ion colors, coordination geometry, and industrial extraction from ore.**
""")

# Create 3 Tabs
tab1, tab2, tab3 = st.tabs(["📊 Sizes, Basicity & Trends", "🎨 Ion Colors & Coordination Geometries", "⛏️ Ore Processing & Extraction"])

# --- TAB 1: SIZES, BASICITY & TRENDS ---
with tab1:
    st.subheader("1. Lanthanide Contraction & Basicity Trend")
    st.markdown("""
    Due to poor shielding by $4f$ electrons, effective nuclear charge increases across the series, causing a steady decrease in atomic and ionic radii (**Lanthanide Contraction**).
    * **Basicity Rule:** As ionic radius decreases ($\text{La}^{3+} \\rightarrow \text{Lu}^{3+}$), charge density increases, covalent character of $\text{M--OH}$ bonds increases, and **basicity decreases**.
    * **Most Basic Hydroxide:** $\text{La(OH)}_3$ (largest radius, most ionic)
    * **Least Basic Hydroxide:** $\text{Lu(OH)}_3$ (smallest radius, most covalent)
    """)

    data = {
        "Element": ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"],
        "Atomic Number": list(range(57, 72)),
        "Ionic Radius 3+ (pm)": [103.2, 101.0, 99.0, 98.3, 97.0, 95.8, 94.7, 93.8, 92.3, 91.2, 90.1, 89.0, 88.0, 86.8, 86.1],
        "Relative Basicity": ["Highest", "High", "High", "Moderate", "Moderate", "Moderate", "Moderate", "Moderate", "Low", "Low", "Low", "Low", "Low", "Very Low", "Lowest"]
    }
    df = pd.DataFrame(data)

    fig = px.line(
        df, 
        x="Element", 
        y="Ionic Radius 3+ (pm)", 
        markers=True, 
        text="Ionic Radius 3+ (pm)",
        title="Ionic Radius Contraction (pm) across La3+ to Lu3+",
        hover_data=["Relative Basicity"]
    )
    fig.update_traces(textposition="top center", line_color="#2b5c8f", marker=dict(size=8))
    st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: ION COLORS & COORDINATION GEOMETRIES ---
with tab2:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎨 Lanthanide Ion Colors (3+ Aqueous)")
        st.markdown("Colors arise from parity-forbidden **$f\text{--}f$ transitions**. Ions with $f^0$ ($\text{La}^{3+}$), $f^7$ ($\text{Gd}^{3+}$), or $f^{14}$ ($\text{Lu}^{3+}$) configuration are colorless.")
        
        color_data = {
            "Ion": ["La3+", "Ce3+", "Pr3+", "Nd3+", "Sm3+", "Eu3+", "Gd3+", "Tb3+", "Dy3+", "Ho3+", "Er3+", "Tm3+", "Yb3+", "Lu3+"],
            "f-config": ["4f0", "4f1", "4f2", "4f3", "4f5", "4f6", "4f7", "4f8", "4f9", "4f10", "4f11", "4f12", "4f13", "4f14"],
            "Observed Color": ["Colorless", "Colorless/UV", "Green", "Pink / Lilac", "Pale Yellow", "Pale Pink", "Colorless", "Pale Pink", "Pale Yellow", "Yellow", "Pink", "Pale Blue", "Colorless", "Colorless"]
        }
        st.dataframe(pd.DataFrame(color_data), use_container_width=True)

    with col2:
        st.subheader("📐 High Coordination Numbers & Shapes")
        st.markdown("Due to large ionic radii and non-directional $f$-orbitals, lanthanides prefer **high coordination numbers (CN 8 to 12)** governed by steric factors rather than orbital hybridization.")
        
        st.markdown("""
        * **CN = 6:** Octahedral (rare, restricted sterically by bulky ligands).
        * **CN = 8:** Square Antiprismatic or Dodecahedral (e.g., $[\text{Eu}(\text{acac})_3(\text{phen})]$).
        * **CN = 9:** Tricapped Trigonal Prismatic (e.g., aqua ions $[\text{Ln}(\text{H}_2\text{O})_9]^{3+}$ for light lanthanides).
        * **CN = 12:** Icosahedral (e.g., nitrate complexes $[\text{Ce}(\text{NO}_3)_6]^{3-}$ in ceric ammonium nitrate).
        """)

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
