# import streamlit as st

# # Custom CSS for background shapes and warm theme
# st.markdown("""
#     <style>
#     /* General styling */
#     .stApp {
#         background: linear-gradient(135deg, #F1D9BC, #E6C2A5); /* Lighter peach gradient background */
#         font-family: "Arial", sans-serif;
#     }

#     /* Sidebar styling */
#     .sidebar .sidebar-content {
#         background-color: #D9B79C;
#         padding: 20px;
#         border-radius: 15px;
#     }

#     /* Title styling */
#     .title {
#         font-size: 28px;
#         color: #333;
#         font-weight: bold;
#         margin-bottom: 15px;
#         text-align: center;
#     }

#     /* Box styling */
#     .box {
#         background-color: #FFFFFF;
#         padding: 25px;
#         border-radius: 15px;
#         box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.15); /* Darker shadow for more depth */
#         margin-bottom: 20px;
#     }

#     /* Button styling */
#     .stButton button {
#         color: white;
#         background-color: #D2785F; /* Darker coral color */
#         border: none;
#         padding: 10px 20px;
#         border-radius: 8px;
#         font-weight: bold;
#         box-shadow: 0px 4px 10px rgba(210, 120, 95, 0.4); /* Soft shadow for button */
#     }

#     /* Input box styling */
#     .stTextArea, .stSelectbox, .stTextInput {
#         background-color: #F3DEC2;
#         border-radius: 8px;
#         border: none;
#         padding: 10px;
#     }

#     /* Decorative background shapes */
#     .shape-container {
#         position: absolute;
#         top: 0;
#         left: 0;
#         height: 100%;
#         width: 100%;
#         z-index: -1;
#     }

#     .circle1 {
#         position: absolute;
#         top: 10%;
#         left: 5%;
#         width: 150px;
#         height: 150px;
#         background-color: #C59575; /* Slightly lighter shade for circle */
#         border-radius: 50%;
#         opacity: 0.8;
#     }

#     .circle2 {
#         position: absolute;
#         bottom: 15%;
#         right: 10%;
#         width: 200px;
#         height: 200px;
#         background-color: #B6866A; /* Slightly lighter shade */
#         border-radius: 50%;
#         opacity: 0.8;
#     }

#     .half-circle {
#         position: absolute;
#         top: 40%;
#         left: 70%;
#         width: 100px;
#         height: 50px;
#         background-color: #D2785F;
#         border-top-left-radius: 100px;
#         border-top-right-radius: 100px;
#     }

#     .triangle {
#         position: absolute;
#         bottom: 10%;
#         left: 20%;
#         width: 0;
#         height: 0;
#         border-left: 60px solid transparent;
#         border-right: 60px solid transparent;
#         border-bottom: 100px solid #C59575;
#     }

#     </style>
# """, unsafe_allow_html=True)

# # HTML to include background shapes
# st.markdown("""
#     <div class="shape-container">
#         <div class="circle1"></div>
#         <div class="circle2"></div>
#         <div class="half-circle"></div>
#         <div class="triangle"></div>
#     </div>
# """, unsafe_allow_html=True)

# # Initialize session state variables
# if "page" not in st.session_state:
#     st.session_state.page = "Dietary Preferences Page"
# if "dietary_preference" not in st.session_state:
#     st.session_state.dietary_preference = None
# if "ingredients" not in st.session_state:
#     st.session_state.ingredients = None
# if "meal_plan_generated" not in st.session_state:
#     st.session_state.meal_plan_generated = False

# # Define each page with new colors and shapes
# def dietary_preferences_page():
#     st.markdown('<div class="title">Dietary Preferences</div>', unsafe_allow_html=True)
#     st.markdown('<div class="box">Please select your dietary preferences to continue.</div>', unsafe_allow_html=True)
#     dietary_preference = st.selectbox("Choose a dietary preference:", ["None", "Vegan", "Vegetarian", "Keto", "Gluten-Free"])

#     # Update session state and navigate to next page
#     if st.button("Next"):
#         st.session_state.dietary_preference = dietary_preference
#         st.session_state.page = "Manual Entry Page"  # Move to the next page

# def manual_entry_page():
#     st.markdown('<div class="title">Manual Entry</div>', unsafe_allow_html=True)
#     st.markdown('<div class="box">Enter the ingredients you have available.</div>', unsafe_allow_html=True)
#     ingredients = st.text_area("Enter your ingredients (comma-separated):")

#     # Store ingredients and proceed to meal plan generation page
#     if st.button("Next"):
#         st.session_state.ingredients = ingredients
#         st.session_state.page = "Meal Plan Generation Page"

# def meal_plan_generation_page():
#     st.markdown('<div class="title">Meal Plan Generation</div>', unsafe_allow_html=True)
#     st.markdown('<div class="box">Generating a meal plan based on your preferences and ingredients...</div>', unsafe_allow_html=True)

#     if st.button("Generate Meal Plan"):
#         # Simulate meal plan generation and store it in session state
#         st.session_state.meal_plan_generated = True
#         st.session_state.page = "Recipe Details Page"

# def recipe_details_page():
#     st.markdown('<div class="title">Recipe Details</div>', unsafe_allow_html=True)
#     st.markdown('<div class="box">Here are the details for your selected meal plan.</div>', unsafe_allow_html=True)

#     # Display placeholder recipe details based on preferences
#     st.write("Recipe Name:", "Sample Recipe Based on Your Preferences")
#     st.write("Ingredients:")
#     st.write("- Ingredient 1")
#     st.write("- Ingredient 2")
#     st.write("Steps:")
#     st.write("1. Do this.")
#     st.write("2. Then do that.")

# def settings_page():
#     st.markdown('<div class="title">Settings</div>', unsafe_allow_html=True)
#     st.markdown('<div class="box">Adjust your preferences here.</div>', unsafe_allow_html=True)
#     dark_mode = st.checkbox("Enable Dark Mode")
#     if dark_mode:
#         st.write("Dark mode enabled (simulated).")

# # Navigation logic to display the appropriate page based on session state
# if st.session_state.page == "Dietary Preferences Page":
#     dietary_preferences_page()
# elif st.session_state.page == "Manual Entry Page":
#     manual_entry_page()
# elif st.session_state.page == "Meal Plan Generation Page":
#     meal_plan_generation_page()
# elif st.session_state.page == "Recipe Details Page":
#     recipe_details_page()
# elif st.session_state.page == "Settings Page":
#     settings_page()


# import os
# from google.oauth2 import service_account

# # Set up the path to your service account JSON key
# SERVICE_ACCOUNT_FILE = 'service_account_key.json'
# credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)


# import requests
# from requests.exceptions import ChunkedEncodingError
# import time

# def get_recipe_suggestions(ingredients, preferences):
#     api_url = "https://gemini.googleapis.com/v1/projects/windy-star-439722-m2/locations/global/models/gemini"
#     headers = {
#         "Authorization": f"Bearer {credentials.token}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "ingredients": ingredients,
#         "preferences": preferences
#     }

#     for attempt in range(3):  # Try up to 3 times
#         try:
#             # Add a timeout parameter (e.g., 10 seconds)
#             response = requests.post(api_url, headers=headers, json=data, timeout=10)

#             if response.status_code == 200:
#                 return response.json()
#             else:
#                 print("Error:", response.status_code, response.text)
#                 return None
#         except ChunkedEncodingError:
#             print(f"Attempt {attempt + 1}: Connection broken. Retrying...")
#             time.sleep(2)  # Wait for 2 seconds before retrying

#     print("Failed after 3 attempts.")
#     return None
#     response = requests.post(api_url, headers=headers, json=data, timeout=20)


# import streamlit as st
# from google.cloud import aiplatform
# import os

# # Set up Google Cloud credentials
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "AIzaSyCS299hjxsa7hhSu-cL0eSb8N22YCF9c-U.json"

# # Initialize Vertex AI
# aiplatform.init(project="your_project_id", location="us-central1")

# # Streamlit page configuration
# st.set_page_config(page_title="Google AI Meal Plan Generator", page_icon="🍲", layout="centered")

# # Page title
# st.title("Google AI-Powered Meal Plan Generator")

# # Instruction box
# st.text_area("Meal Plan Details",
#              value="Enter ingredients or dietary preferences below to generate a custom meal plan.",
#              height=100, disabled=True)

# # User input for ingredients or preferences
# user_input = st.text_input("Enter ingredients or dietary preferences:")

# # Button to trigger meal plan generation
# if st.button("Generate Meal Plan"):
#     if user_input:
#         with st.spinner("Generating meal plan..."):
#             try:
#                 # Use PaLM 2 or Gemini model from Vertex AI Model Garden
#                 model = aiplatform.TextGenerationModel.from_pretrained("projects/your_project_id/locations/us-central1/models/text-bison@001")

#                 # Generate the meal plan
#                 response = model.predict(f"Generate a meal plan based on these ingredients and preferences: {user_input}")

#                 meal_plan = response.text.strip()

#                 # Display the meal plan
#                 st.subheader("Your AI-Generated Meal Plan:")
#                 st.write(meal_plan)
#             except Exception as e:
#                 st.error(f"An error occurred: {e}")
#     else:
#         st.warning("Please enter ingredients or preferences to generate a meal plan.")

# # test_import.py
# from google.cloud import aiplatform
# print("Successfully imported aiplatform")

# from google.cloud import aiplatform

# # Initialize Vertex AI with your project ID and region
# aiplatform.init(
#     project="windy-star-439722-m2",       # Replace with your Google Cloud project ID
#     location="us-central1"           # Replace with your desired region, e.g., us-central1
# )
# # Load the text generation model
# model = aiplatform.TextGenerationModel.from_pretrained("projects/your_project_id/locations/us-central1/models/text-bison@001")

# # Define the ingredients or dietary preferences
# user_input = "chicken, spinach, garlic, low-carb"  # Replace with dynamic input from your application

# # Generate the meal plan
# response = model.predict(
#     f"Generate a meal plan based on these ingredients and preferences: {user_input}"
# )

# # Get the response text
# meal_plan = response.text.strip()

# # Print the generated meal plan
# print("Generated Meal Plan:")
# print(meal_plan)


# import streamlit as st
# import os
# from google.cloud import aiplatform
# from google.oauth2 import service_account
#
# # Set up Streamlit page configuration
# st.set_page_config(page_title="AI Meal Plan Generator", page_icon="🍲", layout="centered")
#
# # Define the path to the Google Cloud credentials and initialize Vertex AI
# SERVICE_ACCOUNT_FILE = r'C:\Users\engpr.ASUS2022\OneDrive\Documents\AIATL_PROJECT_PREPPER\service_account_key.json'
# PROJECT_ID = "windy-star-439722-m2"
# MODEL_NAME = "projects/windy-star-439722-m2/locations/us-central1/models/text-bison@001"
# LOCATION = "us-central1"
# ENDPOINT_ID = "your_endpoint_id"
#
# # Test loading the credentials
# try:
#     credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
#     st.write("Credentials loaded successfully!")
# except Exception as e:
#     st.error(f"Error loading credentials: {e}")
#
# # Load credentials and initialize Vertex AI
# credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
# aiplatform.init(credentials=credentials, project=PROJECT_ID, location="us-central1")
#
# # Custom CSS for background shapes and warm theme
# st.markdown("""
#     <style>
#     .stApp { background: linear-gradient(135deg, #F1D9BC, #E6C2A5); font-family: "Arial", sans-serif; }
#     .title { font-size: 28px; color: #333; font-weight: bold; margin-bottom: 15px; text-align: center; }
#     .box { background-color: #FFFFFF; padding: 25px; border-radius: 15px; box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.15); margin-bottom: 20px; }
#     .stButton button { color: white; background-color: #D2785F; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold; }
#     </style>
# """, unsafe_allow_html=True)
#
# # App title and instruction box
# st.title("Google AI-Powered Meal Plan Generator")
# st.text_area("Meal Plan Details",
#              value="Enter ingredients or dietary preferences below to generate a custom meal plan.", height=100,
#              disabled=True)
#
# # User input for ingredients or preferences
# user_input = st.text_input("Enter ingredients or dietary preferences:")
#
# # Button to trigger meal plan generation
# if st.button("Generate Meal Plan"):
#     if user_input:
#         with st.spinner("Generating meal plan..."):
#             try:
#                 # Load the text generation model from Vertex AI Model Garden
#                 model = aiplatform.TextGenerationModel.from_pretrained(MODEL_NAME)
#
#                 # Generate the meal plan
#                 response = model.predict(
#                     f"Generate a meal plan based on these ingredients and preferences: {user_input}")
#
#                 # Display the meal plan if generated successfully
#                 meal_plan = response.text.strip()
#                 st.subheader("Your AI-Generated Meal Plan:")
#                 st.write(meal_plan)
#             except Exception as e:
#                 st.error(f"An error occurred while generating the meal plan: {e}")
#     else:
#         st.warning("Please enter ingredients or preferences to generate a meal plan.")

# import streamlit as st
# import os
# from google.cloud import aiplatform
# from google.oauth2 import service_account
#
# # Set up Streamlit page configuration
# st.set_page_config(page_title="AI Meal Plan Generator", page_icon="🍲", layout="centered")
#
# # Define the path to the Google Cloud credentials and initialize Vertex AI
# SERVICE_ACCOUNT_FILE = r'C:\Users\engpr.ASUS2022\OneDrive\Documents\AIATL_PROJECT_PREPPER\service_account_key.json'
# PROJECT_ID = "windy-star-439722-m2"
# LOCATION = "us-central1"
# ENDPOINT_ID = "your_endpoint_id"  # replace with your actual endpoint ID
#
# # Load credentials and initialize Vertex AI
# credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
# aiplatform.init(credentials=credentials, project=PROJECT_ID, location=LOCATION)
#
# # Custom CSS for background shapes and warm theme
# st.markdown("""
#     <style>
#     .stApp { background: linear-gradient(135deg, #F1D9BC, #E6C2A5); font-family: "Arial", sans-serif; }
#     .title { font-size: 28px; color: #333; font-weight: bold; margin-bottom: 15px; text-align: center; }
#     .box { background-color: #FFFFFF; padding: 25px; border-radius: 15px; box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.15); margin-bottom: 20px; }
#     .stButton button { color: white; background-color: #D2785F; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold; }
#     </style>
# """, unsafe_allow_html=True)
#
# # App title and instruction box
# st.title("Google AI-Powered Meal Plan Generator")
# st.text_area("Meal Plan Details",
#              value="Enter ingredients or dietary preferences below to generate a custom meal plan.", height=100,
#              disabled=True)
#
#
# # Define the function to generate the meal plan using Vertex AI Endpoint
# def generate_meal_plan(input_text):
#     try:
#         # Initialize the endpoint
#         endpoint = aiplatform.Endpoint(endpoint_name=ENDPOINT_ID)
#         # Send the input to the model for prediction
#         response = endpoint.predict(instances=[{"content": input_text}])
#
#         # Extract and return predictions
#         predictions = response.predictions
#         return predictions[0] if predictions else "No result available."
#     except Exception as e:
#         st.error(f"An error occurred while generating the meal plan: {e}")
#         return None
#
#
# # User input for ingredients or preferences
# user_input = st.text_input("Enter ingredients or dietary preferences:")
#
# # Button to trigger meal plan generation
# if st.button("Generate Meal Plan"):
#     if user_input:
#         with st.spinner("Generating meal plan..."):
#             # Generate the meal plan using the provided ingredients/preferences
#             meal_plan = generate_meal_plan(
#                 f"Generate a meal plan based on these ingredients and preferences: {user_input}")
#             if meal_plan:
#                 st.subheader("Your AI-Generated Meal Plan:")
#                 st.write(meal_plan)
#     else:
#         st.warning("Please enter ingredients or preferences to generate a meal plan.")

import streamlit as st
import google.generativeai as genai

# Configure API key for Gemini
genai.configure(api_key="AIzaSyC2TmWiA2WQM5QGTjjyfQodc5ACR4Shb-c")

# Set model configuration
generation_config = {
    "temperature": 0.7,
    "max_output_tokens": 500,
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

# Function to generate recipes
def get_recipes(ingredients, dietary_preferences):
    input_message = f"""
    I have the following ingredients: {ingredients}.
    Based on my dietary preferences: {dietary_preferences},
    please provide recipe ideas that only use these ingredients and align with my preferences.
    """
    response = model.start_chat().send_message(input_message)
    return response.text

# Streamlit UI
st.title("AI-Powered Recipe Generator")

# User input
ingredients = st.text_input("Enter ingredients (comma-separated):")
dietary_preferences = st.text_input("Enter dietary preferences:")

# Generate recipe button
if st.button("Generate Recipe"):
    if ingredients and dietary_preferences:
        recipe = get_recipes(ingredients, dietary_preferences)
        st.subheader("Generated Recipe Suggestions:")
        st.write(recipe)
    else:
        st.warning("Please enter both ingredients and dietary preferences.")
