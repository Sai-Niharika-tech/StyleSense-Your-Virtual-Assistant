import streamlit as st
import requests
import os
from groq import Groq
from dotenv import load_dotenv

def main():
    load_dotenv()
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

    if not GROQ_API_KEY:
        st.error("Please provide a GROQ_API_KEY in secrets or .env")
        return

    client = Groq(api_key=GROQ_API_KEY)

    st.title("🤖 StyleGPT")
    st.caption("Your Personal AI Stylist: Suggesting Outfits, Shoes, and Accessories.")

    # 1. NEW: Define the System Prompt to enforce styling rules
    SYSTEM_PROMPT = {
        "role": "system",
        "content": (
            "You are a professional fashion stylist. For every styling request, "
            "you must provide a complete look including: "
            "1) A specific Outfit (top and bottom/dress), "
            "2) Footwear (shoes/boots), and "
            "3) Accessories (jewelry, bags, belts, or hats). "
            "Focus on color coordination, fabric textures, and occasion appropriateness."
        )
    }

    # 2. Ensure messages are initialized with the system prompt
    if "messages" not in st.session_state:
        st.session_state.messages = [SYSTEM_PROMPT]

    # Display chat (skip the system prompt so the user doesn't see instructions)
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    user_prompt = st.chat_input("💬 Describe the event or 'vibe' you want...")

    if user_prompt:
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)

        try:
            # The AI now uses the SYSTEM_PROMPT instructions every time
            completion = client.chat.completions.create(
                messages=st.session_state.messages,
                model="llama-3.1-8b-instant",
                temperature=0.7,
            )
            ai_reply = completion.choices[0].message.content
            
            with st.chat_message("assistant"):
                st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        except Exception as e:
            st.error(f"API Error: {str(e)}")

if __name__ == "__main__":
    main()