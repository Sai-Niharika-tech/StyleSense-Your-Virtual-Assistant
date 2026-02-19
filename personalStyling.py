import streamlit as st
import google.generativeai as genai

# HARDCODED KEY (Replace with your actual key)
api_key = st.secrets["GEMINI_API_KEY"]

# Unified Styling Database
STYLE_CONFIG = {
    "BODY_TYPES": {
        "Pear": "Balance wider hips by adding volume and structure to the upper body.",
        "Apple": "Create vertical lines with V-necks and empire waists to elongate the torso.",
        "Hourglass": "Accentuate the natural waistline and maintain balanced proportions.",
        "Rectangle": "Create the illusion of curves using belts, peplums, and layered textures.",
        "Inverted Triangle": "Balance broad shoulders with wide-leg trousers or A-line skirts.",
        "Athletic": "Soften a muscular silhouette with draping and feminine necklines.",
        "Petite": "Focus on vertical integrity and high-waisted cuts to elongate the frame."
    },
    "AESTHETICS": [
        "Minimalist (Clean lines, neutrals)", 
        "Old Money (Classic, tailored, high-quality)", 
        "Streetwear (Oversized, comfortable, edgy)", 
        "Bohemian (Flowy, patterns, relaxed)", 
        "Avant-Garde (Experimental, bold shapes)",
        "Dark Academia (Preppy, moody, intellectual)"
    ],
    "SENSORY_NEEDS": [
        "No specific needs",
        "Sensory Friendly (Seamless, tagless, soft)",
        "Hypoallergenic (Organic cotton/silk only)",
        "Breathability Focused (Avoid synthetics)",
        "No Heavy Fabrics (Lightweight only)"
    ]
}


# =====================================================
# MAIN FUNCTION (for StyleSense)
# =====================================================

def main():
    run_styling_module()


# =====================================================
# STYLING MODULE
# =====================================================

def run_styling_module():

    st.header("✨DressMeAI: Personalized AI Styling Guide")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    # --- SECTION 1: Body & Comfort ---
    st.subheader("🧬 Body & Comfort")

    c1, c2 = st.columns(2)

    with c1:
        selected_body = st.selectbox(
            "Body Type:",
            list(STYLE_CONFIG["BODY_TYPES"].keys())
        )

    with c2:
        selected_sensory = st.selectbox(
            "Sensory & Fabric Needs:",
            STYLE_CONFIG["SENSORY_NEEDS"]
        )

    # --- SECTION 2: Identity & Vibe ---
    st.subheader("🎨 Visual Identity")

    c3, c4 = st.columns(2)

    with c3:
        selected_aesthetic = st.selectbox(
            "Aesthetic Style:",
            STYLE_CONFIG["AESTHETICS"]
        )

    with c4:
        fit_pref = st.select_slider(
            "Preferred Silhouette:",
            options=["Tight", "Fitted", "Relaxed", "Oversized"]
        )

    # --- SECTION 3: Occasion ---
    st.subheader("📅 Context")

    occasion = st.text_input(
        "What is the occasion?",
        placeholder="e.g., A rainy day at the office"
    )

    extra_notes = st.text_area(
        "Specific Requests:",
        placeholder="e.g., 'I want to hide my midsection' or 'I love gold accents'"
    )

    if st.button("Generate My Styling Guide"):

        base_rule = STYLE_CONFIG["BODY_TYPES"][selected_body]

        prompt = (
            f"You are a professional AI Personal Stylist. Provide a detailed outfit guide for a {selected_body} body type. "
            f"Rule to follow: {base_rule}. "
            f"Context: Occasion is {occasion}. "
            f"Aesthetic: {selected_aesthetic} with a {fit_pref} fit. "
            f"Special Consideration: User has sensory needs: {selected_sensory}. "
            f"Additional user notes: {extra_notes}. "
            f"Suggest a full outfit (top, bottom, shoes) and explain why these pieces work. "
            f"Keep the advice concise and simple."
        )

        with st.spinner("Analyzing style rules and comfort data..."):

            try:
                response = model.generate_content(prompt)

                st.divider()

                st.success(f"**Stylist's Core Principle:** {base_rule}")

                st.markdown(response.text)

            except Exception as e:
                st.error(f"Error connecting to Gemini: {e}")


# =====================================================
# STANDALONE RUN
# =====================================================

if __name__ == "__main__":
    main()
