import streamlit as st

# 1. Page Definitions (The only place where filenames are linked)
home_page = st.Page("homepage.py", title="Home", icon="🏠", default=True)
assistant_page = st.Page("virtual_fashion_assistant.py", title="AI Assistant", icon="🤖")
styling_page = st.Page("personalStyling.py", title="Personal Styling", icon="✨")
sustainability_page = st.Page("Sustainable.py", title="Sustainability", icon="🌿")
trends_page = st.Page("trend_forecasting.py", title="Trend Forecasting", icon="📈")



# 2. Global Configuration (Set it here ONCE)
st.set_page_config(page_title="StyleSense AI", page_icon="🧥", layout="wide")

# 3. Initialize Navigation
pg = st.navigation([home_page, trends_page, assistant_page, styling_page, sustainability_page])

# 4. Run the app
pg.run()