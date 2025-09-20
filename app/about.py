import streamlit as st

markdown = """## X-Ray maps

This notebooks has simple workflows with chemical X-ray data obtained with an electron probe microanalyzer (EMPA), with both EDS (energy-dispersive) and WDS (wavelength-dispersive) spectometers. 

Data is from a high-grade _crd-grt granulite with spl-sill_ from the **Araçuaí Orogen**, SE Brazil. Full description of this sample is described by Schiavetti _et al._ (2025).

Worklows are:
* load and display individual X-ray maps
* train a machine-learning model to classify minerals
* load mineral chemistry standards and use a cluster algorithm to classify all pixels

Classes
* XrayMap

---

to do
* read and review
* setup analysis"""

st.markdown(markdown)