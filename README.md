# Problem Solver Script

This Python script utilizes the Google Gemini API to analyze an image, identify a potential problem depicted within it, propose a solution, and generate a relevant code snippet.

## Requirements

*   Python 3.x
*   Google Generative AI library: `pip install google-generativeai`
*   Pillow library: `pip install Pillow`
*   A Google Gemini API Key.

## Setup

1.  **API Key:** This script requires your Google Gemini API key to be set as an environment variable named `GEMINI_API_KEY`.
    *   **Windows (Command Prompt - current session):**
        ```bash
        set GEMINI_API_KEY=YOUR_API_KEY_HERE
        ```
    *   **Windows (PowerShell - current session):**
        ```powershell
        $env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```
    *   For persistent storage, consider adding it to your system's environment variables.

2.  **Dependencies:** Install the required Python libraries:
    ```bash
    pip install google-generativeai Pillow
    ```

## Usage

1.  **Place Image:** Put the image file you want to analyze in the same directory as the `problem_solver.py` script.
2.  **Configure Image Path:** By default, the script looks for an image named `image.png`. If your image has a different name, update the `image_path` variable within the `problem_solver.py` script:
    ```python
    # Define the path to the image containing the problem
    image_path = "your_image_filename.png" # CHANGE THIS
    ```
3.  **Run Script:** Execute the script from your terminal:
    ```bash
    python problem_solver.py
    ```

The script will load the image, send it to the Gemini API, and print the identified problem, proposed solution, and code snippet to the console.