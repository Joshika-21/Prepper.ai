

import google.generativeai as genai

# Configure API key directly in Python code
genai.configure(api_key="AIzaSyC2TmWiA2WQM5QGTjjyfQodc5ACR4Shb-c")

# Define model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(history=[])

# Function to get recipe ideas based on ingredients and dietary preferences
def get_recipes(ingredients, dietary_preferences):
    input_message = f"""
    I have the following ingredients: {ingredients}.
    Based on my dietary preferences: {dietary_preferences},
    please provide recipe ideas that only use these ingredients and align with my preferences.
    """
    response = chat_session.send_message(input_message)
    return response.text

# Example Usage
ingredients = "tomatoes, pasta, garlic, olive oil, basil"
dietary_preferences = "vegetarian, gluten-free"
recipes = get_recipes(ingredients, dietary_preferences)

print("Recipe Suggestions:\n", recipes)