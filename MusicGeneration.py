import os
import replicate
import streamlit as st


API_TOKEN = 'r8_BFVwl9hCJa18JvMYip5kGNsNglgUviQ3NNVV2'

api = replicate.Client(api_token=API_TOKEN)

st.title("Music Generation Tool")

# User inputs
prompt = st.text_input("Enter your prompt:", "Engergetic EDM")

model_options = ["small", "melody", "large"]

model = st.selectbox("Select Model:", model_options, index=0)

strategy_options = ["loudness", "clip", "peak", "rms"]

strategy = st.selectbox("Select Normalization Strategy:", strategy_options, index=0)

duration = st.slider("Select Duration (in seconds):", min_value=1, max_value=300, value=8)

# Create a button to generate music
if st.button("Generate Music"):
    processing_message = st.empty()
    processing_message.info("Generating...")

    # Run Replicate API
    output = api.run(
        "aussielabs/musicgen:11bbae94fb523ecaab2b87ec074fd5b668f20d2b84030c093ed5d5ba8f6f4df1",
        input={

            "prompt": prompt,
            "duration": duration,
            "model_version": model,
            "normalization_strategy": strategy,
        }
    )

    processing_message.empty()
    st.success("Music generated successfully!")

    # Display the generated audio
    st.subheader("Generated Audio")
    generated_audio = output
    if generated_audio:
        st.audio(generated_audio, format='audio/wav')
