import os
import streamlit as st
from dotenv import load_dotenv
import aisuite as ai

# Load API keys from .env file
load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set API keys as environment variables
os.environ['ANTHROPIC_API_KEY'] = ANTHROPIC_API_KEY
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
os.environ['GROQ_API_KEY'] = GROQ_API_KEY

# Initialize AI client
client = ai.Client()

# Title for the Streamlit app
st.title("⚓ Talk to a Pirate AI Bot in Pirate Language! 🏴‍☠️")

# Dropdown for selecting a model
models = ["groq:llama-3.1-8b-instant", "openai:gpt-4o-mini", "anthropic:claude-3-5-sonnet-20240620"]
selected_model = st.selectbox("Choose yer AI model, matey:", models)

# Text input for the user's question
query = st.text_input("Ask the Pirate AI somethin', ye landlubber!")

if st.button("⚓ Get Pirate Response"):
    if query:
        try:
            # Prepare messages
            messages = [
                {"role": "system", "content": "Respond in Pirate English."},
                {"role": "user", "content": query},
            ]

            # Call the AI API with the selected model
            response = client.chat.completions.create(
                model=selected_model,
                messages=messages,
            )

            # Extract and style the AI response
            pirate_response = response.choices[0].message.content
            st.markdown(
                f"""
                <div style="
                    background-color: #FFF9C4; 
                    color: #7C3AED; 
                    padding: 20px; 
                    border-radius: 10px; 
                    font-family: 'Courier New', monospace; 
                    font-size: 18px; 
                    font-weight: bold; 
                    text-align: center;">
                    🏴‍☠️ <b>Pirate AI says:</b><br><br>{pirate_response}
                </div>
                """,
                unsafe_allow_html=True,
            )
        except Exception as e:
            st.error(f"Arrr! Somethin' went wrong: {e}")
    else:
        st.warning("Ask somethin' first, ye scallywag!")
