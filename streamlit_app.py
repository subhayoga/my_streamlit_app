from ucimlrepo import fetch_ucirepo
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header("Subha's App")


# fetch dataset
wine_quality = fetch_ucirepo(id=186)

# data (as pandas dataframes)
X = wine_quality.data.features
y = wine_quality.data.targets

# metadata
st.write(wine_quality.metadata)

# variable information
st.write(wine_quality.variables)
