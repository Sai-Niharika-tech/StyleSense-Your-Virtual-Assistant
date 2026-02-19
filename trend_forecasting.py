import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import os

# -----------------------------
# 1. LOAD CSV DATA
# -----------------------------
FILE_PATH = "trend_data.csv"

if not os.path.exists(FILE_PATH):
    st.error(f"❌ '{FILE_PATH}' not found. Please ensure the CSV is in the root folder.")
else:
    # -----------------------------
    # 2. PAGE UI
    # -----------------------------
    st.title("📈 What's Trending?")
    st.write("Visualize current popularity and predicte future fashion waves.")

    trend_data = pd.read_csv(FILE_PATH)

    # Clean date columns
    if "date" in trend_data.columns:
        trend_data["date"] = pd.to_datetime(trend_data["date"])
        trend_data.set_index("date", inplace=True)

    trends = list(trend_data.columns)

    # -----------------------------
    # 3. FORECAST LOGIC
    # -----------------------------
    def forecast_trend(series):
        y = series.values
        x = np.arange(len(y)).reshape(-1, 1)
        model = LinearRegression()
        model.fit(x, y)
        future_x = np.array([[len(y) + 7]]) # Predict 7 days out
        prediction = model.predict(future_x)
        return float(prediction[0])

    forecast_scores = {trend: forecast_trend(trend_data[trend]) for trend in trends}

    # -----------------------------
    # 4. TREND GRAPH (Interactive Plotly)
    # -----------------------------
    st.subheader("Future Fashion Popularity")
    
    trend_names = list(forecast_scores.keys())
    scores = list(forecast_scores.values())

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=trend_names,
        y=scores,
        mode="lines+markers",
        marker=dict(size=12, color='royalblue'),
        line=dict(width=4)
    ))

    fig.update_layout(
        xaxis_title="Fashion Style",
        yaxis_title="Predicted Score",
        template="plotly_white",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # 5. IMAGE GALLERY
    # -----------------------------
    IMAGE_MAP = {
        "streetwear fashion": ["https://cdn.shopify.com/s/files/1/0305/7100/4043/files/Varsity_Jacket_Streetwear_Style_1024x1024.jpg?v=1662470430", "https://tse2.mm.bing.net/th/id/OIP._EuCWrJycbgwD08goJkvuwHaEO", "https://www.yellowbrick.co/wp-content/uploads/2023/02/Streetwear-style.jpg"],
        "vintage fashion": ["https://png.pngtree.com/background/20230606/original/pngtree-group-of-women-wearing-high-waist-jeans-picture-image_2877049.jpg", "https://tse4.mm.bing.net/th/id/OIP.4BcOCGqRjwguPi6N8oB_mAHaEb", "https://images.yourstory.com/cs/7/1da9ec3014cc11e9a1b2b928167b6c62/mensfashionbanner1572434751640png"],
        "athleisure fashion": ["https://cdn.mos.cms.futurecdn.net/teZDLKff8xYJoDEeZLv6iX-1024-80.jpg", "https://tse4.mm.bing.net/th/id/OIP.AbRqdADp-TLbCVtE-dVEOwHaEK", "https://cdn.mos.cms.futurecdn.net/HWcV5UPc22qW3ZeyFJw5ZT-1280-80.png"],
        "Y2K fashion": ["https://i.pinimg.com/originals/80/c6/78/80c67834f7fcd7223766c98d47f12231.jpg", "https://sveltemag.com/wp-content/uploads/2024/04/y2k-fashion.jpg", "https://content.api.news/v3/images/bin/ebad96f0d1217f7de17cbb3c67fe37cf"],
        "minimalist fashion": ["https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/index-2-1608755610.jpg", "https://wallpapers.com/images/hd/minimalist-fashion-1920-x-1080-wallpaper.jpg", "https://tse3.mm.bing.net/th/id/OIP._Rw_8sM-rXSrn0InhIjdkwHaDp"],
        "boho fashion": ["https://sveltemag.com/wp-content/uploads/2022/09/bohemian-fashion-style.jpg", "https://tse1.mm.bing.net/th/id/OIP.OkTRMm5-I_iohGd7IFhgBAHaEs", "https://vitruvianmagazine.com/wp-content/uploads/2018/04/Bohemian-style-guide-featured-pic.jpg"]
    }

    st.subheader("🖼 Style Inspiration")
    selected = st.selectbox("Select a Style to see inspiration", trends)

    if selected:
        images = IMAGE_MAP.get(selected, ["https://via.placeholder.com/300"]*3)
        cols = st.columns(3)
        for i in range(3):
            with cols[i]:
                st.image(images[i], use_container_width=True)
        
        st.success(f"🔥 **{selected.title()}** has a predicted trend score of **{round(forecast_scores[selected],2)}**")

    # -----------------------------
    # 6. RAW DATA TABLE
    # -----------------------------
    with st.expander("📊 View Raw Trend Data"):
        st.dataframe(trend_data.tail(10))