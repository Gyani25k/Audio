import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def main():
    st.title("Music Generation")

    # Get user input
    user_input = st.text_area("Enter music preferences (e.g., liquid drum and bass, atmospheric synths, airy sounds):")

    if st.button("Generate Music"):
        if user_input:
            st.info("Generating music... Please wait.")
            payload = {"inputs": user_input}
            audio_bytes = query(payload)
            st.audio(audio_bytes, format="audio/wav")
        else:
            st.warning("Please enter music preferences before generating.")

if __name__ == "__main__":
    main()

