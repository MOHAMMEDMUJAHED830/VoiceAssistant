# Gemini-Powered Chatbot

This repository contains a Flask-based web application that integrates with the Google Gemini AI model to provide chatbot functionality. Users can input text through a simple HTML interface, and the application sends the input to the Gemini API, returning the AI's response to the user.

## Features

* **Interactive Chatbot:** Allows users to engage in conversations with the Gemini AI.
* **Flask Backend:** Utilizes Flask to handle API requests and serve the user interface.
* **Gemini Integration:** Leverages the Google Gemini API for generating intelligent responses.
* **Simple HTML Frontend:** Provides a basic HTML page for user interaction.
* **Error Handling:** Implements error handling to gracefully manage API request failures.

## Setup Instructions

1. **Clone the Repository:** `git clone [repository URL]`
2. **Install Dependencies:** `pip install Flask Flask-CORS requests`
3. **Set Gemini API Key:** Replace `"AIzaSyBvBMlOqMvG75P7cNoSf9_GrD3_u8fw6Do"` in `app.py` with your actual Gemini API key.
4. **Run the Application:** `python app.py`
5. **Access the Chatbot:** Open your web browser and navigate to `http://127.0.0.1:5000/`

## Usage

1. Enter your message in the text input field.
2. Click the "Send" button.
3. The Gemini AI's response will be displayed below the input field.

## Contributing

Contributions are welcome! Feel free to submit pull requests to improve the functionality or add new features.
