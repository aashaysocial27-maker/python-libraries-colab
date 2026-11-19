import numpy as np, pandas as pd
import streamlit as st

st.set_page_config(page_title="ShopEasy sales", layout="wide")

@st.cache_data
def load():
    rng = np.random.default_rng(42)
    n = 600
    df = pd.DataFrame({
        "date": pd.Timestamp("2026-01-01") + pd.to_timedelta(rng.integers(0, 90, n), unit="D"),
        "city": rng.choice(["Mumbai", "Delhi", "Pune", "Bengaluru"], n),
        "category": rng.choice(["Books", "Electronics", "Clothing", "Home"], n),
        "revenue": rng.integers(199, 9000, n),
    })
    return df

df = load()
st.title("ShopEasy sales dashboard")
city = st.selectbox("City", ["All"] + sorted(df["city"].unique()))
cats = st.multiselect("Categories", sorted(df["category"].unique()), default=sorted(df["category"].unique()))

view = df[df["category"].isin(cats)]
if city != "All":
    view = view[view["city"] == city]

c1, c2, c3 = st.columns(3)
c1.metric("Orders", f"{len(view):,}")
c2.metric("Revenue", f"Rs.{view['revenue'].sum():,}")
c3.metric("Average order", f"Rs.{view['revenue'].mean():,.0f}" if len(view) else "-")

st.line_chart(view.groupby("date")["revenue"].sum())
st.dataframe(view.sort_values("revenue", ascending=False).head(20), width="stretch")