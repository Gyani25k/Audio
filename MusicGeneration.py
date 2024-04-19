import os
import replicate
import streamlit as st


API_TOKEN = 'r8_I8pXU6NNDCtG1ryedtFiIU1TtZpIyay2wKHnr'

api = replicate.Client(api_token=API_TOKEN)

tool_description = "This tool is a simple and controllable model for music generation. "

st.title("Music Generation Tool",help=tool_description)

prompt_example = (
        "Describe the type of music you wish to generate. For instance:\n"

        "1. A vibrant pop song from the 80s featuring prominent drums and synthesized pads.\n"
        "2. A lively country tune characterized by acoustic guitar melodies.\n"
        "3. A rock anthem from the 90s showcasing electric guitar riffs and powerful drum beats.\n"
        "4. An upbeat EDM track with rhythmic drums, ethereal pads, and intense emotions.\n"
        "5. A relaxed electro-chill piece with a low BPM and organic sound samples."
)

# User inputs
prompt = st.text_input("Enter your prompt:", "A vibrant pop song from the 80s featuring prominent drums and synthesized pads.",help=prompt_example)

model_options = ["small", "melody", "large"]

model_example = (
    "Select the model for music generation based on requirements.\n"

    "1. Small: Designed as an entry-level model, it contains 300 million parameters, making it powerful for its size. It's great for music generation experiments due to its efficient single-pass codebook generation, requiring only 50 auto-regressive steps per second of audio, ideal for beginners exploring audio synthesis.\n"
    "2. Melody:Tailored for melody creation, the specialized model with 1.5 billion parameters emphasizes melodic composition, ideal for music creators prioritizing melody expression. It’s recommended for users focused on generating music with rich, melodic content, especially when semantic representation is not required. \n"
    "3. Large: Ideal for those seeking top-tier performance, the Large model boasts 3.3 billion parameters, excelling in high-quality music generation. It’s perfect for advanced users or professionals requiring intricate musical complexity and sophistication in their generated samples."

)

model = st.selectbox("Select Model:", model_options, index=0,help=model_example)

strategy_example = (
        "Select the strategy for normalizing audio.\n"

        "1. Loudness: Use when you want to balance the perceived volume of different audio tracks or segments within a project.\n"
        "2. Clip: Address clipping when you need to prevent distortion caused by signal peaks exceeding the maximum limit of the audio system.\n"
        "3. Peak: Monitor peaks to ensure that audio levels do not exceed acceptable limits, especially in digital audio processing to avoid digital clipping.\n"
)

strategy_options = ["loudness", "clip", "peak"]

strategy = st.selectbox("Select Normalization Strategy:", strategy_options, index=0,help=strategy_example)

duration = st.slider("Select Duration (in seconds):", min_value=1, max_value=300, value=8,help="Select the length of the audio generated based on your needs in seconds.")

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
