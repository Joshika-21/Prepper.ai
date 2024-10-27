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

