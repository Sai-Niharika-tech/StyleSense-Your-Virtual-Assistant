import streamlit as st

st.title(" StyleSense: Your Virtual Fashion Assistant")
st.markdown("### Your All-in-One AI Fashion Ecosystem")
st.divider()

# --- Feature Grid (2x2 Layout) ---
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("💬 StyleGPT")
        st.write("Our Personal AI Stylist: Suggesting Outfits, Shoes, and Accessories.")
        if st.button("Open Assistant", key="va"):
            st.switch_page("virtual_fashion_assistant.py")

with col2:
    with st.container(border=True):
        st.subheader("📈  What's Trending?")
        st.write("Visualize current popularity and predicte future fashion waves.")
        if st.button("View Trends", key="tf"):
            st.switch_page("trend_forecasting.py")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.subheader("✨DressMeAI: Personalized AI Styling Guide")
        st.write("Tailored recommendations based on your unique body type and aesthetic identity.")
        if st.button("Get Styled", key="ps"):
            st.switch_page("personalStyling.py")

with col4:
    with st.container(border=True):
        st.subheader("🌿 Sustainable Styling")
        st.write("Find eco-friendly fabric alternatives and sustainable fashion insights.")
        if st.button("Explore Eco-Style", key="ss"):
            st.switch_page("Sustainable.py")

# --- App Analytics / Style Pulse ---
st.divider()
st.subheader("📊 Your Style Pulse")
c1, c2, c3 = st.columns(3)
c1.metric("Sustainability Score", "85%", "+5%")
c2.metric("Wardrobe Diversity", "Classic/Boho", "New!")
c3.metric("Trend Alignment", "High", "Winter '26")