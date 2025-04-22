import google.generativeai as genai
from PIL import Image # Import the Image class from Pillow
import os # Import os for path joining

# Configure the API key
# It's recommended to use environment variables for API keys
API_KEY = os.getenv('GEMINI_API_KEY') # Replace with your key or use env var

if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set.")
    exit()

try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    print(f"Error configuring Generative AI: {e}")
    exit()

# --- Image Loading ---
# Define the path to the image containing the problem
image_path = "image.png" # CHANGE THIS to your actual image file name
script_dir = os.path.dirname(__file__) # Get the directory of the script
full_image_path = os.path.join(script_dir, image_path)

try:
    img = Image.open(full_image_path)
    print(f"Successfully loaded image: {full_image_path}")
except FileNotFoundError:
    print(f"Error: Image file not found at {full_image_path}")
    exit() # Exit if the image isn't found
except Exception as e:
    print(f"Error opening image: {e}")
    exit()

# --- Model Initialization ---
try:
    # Using gemini-1.5-flash as it supports vision
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Error initializing Generative Model: {e}")
    exit()

# --- Prompt Definition ---
# Define the prompt asking the model to identify a problem and suggest a solution
prompt = """
Analyze the provided image carefully.
1. Identify the main problem or challenge depicted in the image.
2. Propose a concise and practical solution or suggestion to address that problem.
3. give the accurate code snippet to solve the problem.

Please structure your response clearly, first stating the identified problem, and then the proposed solution.
"""

# --- Generate Content ---
print("\nGenerating solution...")
try:
    # Send the image and the prompt to the model
    response = model.generate_content([img, prompt])
    response.resolve() # Ensure the response is fully generated

    # Print the generated text (problem and solution)
    print("\n--- Generated Response ---")
    print(response.text)
    print("------------------------")

except Exception as e:
    print(f"\nAn error occurred during content generation: {e}")