import streamlit as st
import google.generativeai as genai

# Configure API key for Gemini
genai.configure(api_key="AIzaSyC2TmWiA2WQM5QGTjjyfQodc5ACR4Shb-c")  # Replace with your actual API key

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
st.title("P R E P P E R")

# User input for ingredients
ingredients = st.text_input("Enter ingredients (comma-separated):")
# User input for dietary preferences
dietary_preferences = st.text_input("Enter dietary preferences:")

# Generate recipe button
if st.button("Generate Recipe"):
    if ingredients and dietary_preferences:
        recipe = get_recipes(ingredients, dietary_preferences)
        st.subheader("Generated Recipe Suggestions:")
        st.write(recipe)
    else:
        st.warning("Please enter both ingredients and dietary preferences.")

# Custom CSS for background shapes and warm theme
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #F1D9BC, #E6C2A5); /* Lighter peach gradient background */
        font-family: "Arial", sans-serif;
    }

    .title {
        font-size: 28px;
        color: #333;
        font-weight: bold;
        margin-bottom: 15px;
        text-align: center;
    }

    .box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.15);
        margin-bottom: 20px;
    }

    .stButton button {
        color: white;
        background-color: #D2785F; /* Darker coral color */
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: bold;
    }

    .stTextInput, .stTextArea {
        background-color: #F3DEC2;
        border-radius: 8px;
        border: none;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)
