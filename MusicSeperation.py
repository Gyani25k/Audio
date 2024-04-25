import os
import replicate
import streamlit as st


API_TOKEN = 'REPLICATE-API-TOKEN'

api = replicate.Client(api_token=API_TOKEN)

st.title("Audio Separation Tool")

# App Description
st.write(
    "This app separate vocals and accompaniment from an audio file."
    " Enter the URL of the audio file, click 'Separate', and listen to the separated tracks."
)

# Get audio input from the user
audio_url = st.text_input("Enter the URL of the audio file:")
if not audio_url:
    st.warning("Please enter the URL of the audio file.")
    st.stop()

# Create a button to trigger the separation process
if st.button("Separate"):
    processing_message = st.empty()
    processing_message.info("Processing...")

    # Run Replicate API
    output = api.run(
        "soykertje/spleeter:cd128044253523c86abfd743dea680c88559ad975ccd72378c8433f067ab5d0a",
        input={
            "audio": audio_url
        }
    )

    processing_message.empty()
    st.success("Music seperated successfully!")

    # Display the original audio
    st.subheader("Original Audio")
    st.audio(audio_url, format='audio/mp3')

    # Display the audio player for accompaniment
    st.subheader("Accompaniment")
    accompaniment_audio = output.get('accompaniment', '')
    if accompaniment_audio:
        st.audio(accompaniment_audio, format='audio/mp3')

    # Display the audio player for vocals
    st.subheader("Vocals")
    vocals_audio = output.get('vocals', '')
    if vocals_audio:
        st.audio(vocals_audio, format='audio/mp3')
