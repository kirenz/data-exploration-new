"""Load loans dataset from GitHub repository."""
import pandas as pd
import altair as alt

ROOT = "https://raw.githubusercontent.com/kirenz/datasets/master/"
DATA = "loans.csv"
df = pd.read_csv(ROOT + DATA)

# aCme
plot = alt.Chart(df).mark_bar().encode(
    x='homeownership',
    y='count(homeownership)'
)

plot.save("bar_plot.html")