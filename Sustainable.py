import streamlit as st
import google.generativeai as genai

# HARDCODED KEY (Replace with your actual key)
api_key = st.secrets["GEMINI_API_KEY"]

# Component: Eco-friendly alternatives database
ECO_DATABASE = [
    "Polyester",
    "Cotton",
    "Leather",
    "Silk",
    "Wool",
    "Nylon",
]


# =====================================================
# MAIN FUNCTION (for StyleSense)
# =====================================================

def main():
    run_sustainability_module()


# =====================================================
# SUSTAINABILITY MODULE
# =====================================================

def run_sustainability_module():

    st.header("🌿 Sustainable Fashion Insights")
    st.write("Explore eco-friendly alternatives to traditional textile materials.")

    # Configuration
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    # Component: Sustainable fashion data collection
    fabric = st.selectbox(
        "Select a fabric to find a sustainable alternative:",
        list(ECO_DATABASE)
    )

    if st.button("Analyze Eco-Impact"):

        prompt = (
            f"Act as a sustainability expert. Give alternatives for {fabric} in a fun format which grabs the user attention. "
            f"Keep the alternatives to one or two words. "
            f"Provide only 2 alternatives which are available in markets. "
            f"Provide a very brief analysis of environmental impact and why a user "
            f"should prefer the alternative. "
            f"Include how much the user is saving the environment by choosing the alternative. "
            f"Keep the response concise, focused on key eco-benefits and in simple, easy to understand language."
        )

        with st.spinner("Fetching environmental data..."):

            try:
                response = model.generate_content(prompt)

                st.success(f"Found Alternatives for {fabric}!!")

                st.markdown(response.text)

            except Exception as e:
                st.error(f"Error connecting to Gemini: {e}")


# =====================================================
# STANDALONE RUN
# =====================================================

if __name__ == "__main__":
    main()
