import streamlit as st
st.write("STREAMLIT IS RUNNING")
import pandas as pd
import streamlit as st
import plotly.express as px

st.header("Used Car Market Dashboard")

st.write(
    "This dashboard explores pricing patterns in the U.S. used car market, "
    "focusing on relationships between price, mileage, and model year."
)

# Load dataset
df = pd.read_csv("vehicles_us.csv")

# Checkbox interaction
filter_prices = st.checkbox("Exclude listings over $100,000")

if filter_prices:
    df = df[df["price"] < 100000]

# Histogram
fig_hist = px.histogram(
    df,
    x="price",
    nbins=50,
    title="Distribution of Used Car Prices",
    labels={
        "price": "Price (USD)"
    }
)

fig_hist.update_layout(
    yaxis_title="Number of Listings"
)

st.plotly_chart(fig_hist)

# Scatter plot
fig_scatter = px.scatter(
    df,
    x="odometer",
    y="price",
    title="Price vs Odometer",
    labels={
        "odometer": "Odometer (Miles)",
        "price": "Price (USD)"
    },
    opacity=0.6
)

st.plotly_chart(fig_scatter)

fig_scatter_year = px.scatter(
    df,
    x="model_year",
    y="price",
    title="Price vs Model Year",
    labels={
        "model_year": "Model Year",
        "price": "Price (USD)"
    },
    opacity=0.6
)

st.plotly_chart(fig_scatter_year)
