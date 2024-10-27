import streamlit as st
import os
from google.cloud import aiplatform
from google.oauth2 import service_account

# Set up Streamlit page configuration
st.set_page_config(page_title="AI Meal Plan Generator", page_icon="🍲", layout="centered")

# Define the path to the Google Cloud credentials and initialize Vertex AI
SERVICE_ACCOUNT_FILE = r"C:\Users\engpr.ASUS2022\OneDrive\Documents\AIATL_PROJECT_PREPPER\service_account_key.json"
PROJECT_ID = "windy-star-439722-m2"
MODEL_NAME = "projects/windy-star-439722-m2/locations/us-central1/models/text-bison@001"
LOCATION = "us-central1"
ENDPOINT_ID = "your_endpoint_id"

# Test loading the credentials
try:
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
    st.write("Credentials loaded successfully!")
except Exception as e:
    st.error(f"Error loading credentials: {e}")

# Load credentials and initialize Vertex AI
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
aiplatform.init(credentials=credentials, project=PROJECT_ID, location="us-central1")

# Custom CSS for background shapes and warm theme
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #F1D9BC, #E6C2A5); font-family: "Arial", sans-serif; }
    .title { font-size: 28px; color: #333; font-weight: bold; margin-bottom: 15px; text-align: center; }
    .box { background-color: #FFFFFF; padding: 25px; border-radius: 15px; box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.15); margin-bottom: 20px; }
    .stButton button { color: white; background-color: #D2785F; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# App title and instruction box
st.title("Google AI-Powered Meal Plan Generator")
st.text_area("Meal Plan Details",
             value="Enter ingredients or dietary preferences below to generate a custom meal plan.", height=100,
             disabled=True)

# User input for ingredients or preferences
user_input = st.text_input("Enter ingredients or dietary preferences:")

# Button to trigger meal plan generation
if st.button("Generate Meal Plan"):
    if user_input:
        with st.spinner("Generating meal plan..."):
            try:
                # Load the text generation model from Vertex AI Model Garden
                model = aiplatform.TextGenerationModel.from_pretrained(MODEL_NAME)

                # Generate the meal plan
                response = model.predict(
                    f"Generate a meal plan based on these ingredients and preferences: {user_input}")

                # Display the meal plan if generated successfully
                meal_plan = response.text.strip()
                st.subheader("Your AI-Generated Meal Plan:")
                st.write(meal_plan)
            except Exception as e:
                st.error(f"An error occurred while generating the meal plan: {e}")
    else:
        st.warning("Please enter ingredients or preferences to generate a meal plan.")
