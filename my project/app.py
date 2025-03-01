from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__, template_folder="templates")  # Ensure templates folder is correctly set
CORS(app)

# Set your Gemini API key
GEMINI_API_KEY = "AIzaSyBvBMlOqMvG75P7cNoSf9_GrD3_u8fw6Do"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"


# Function to get Gemini AI response
def get_gemini_response(prompt):
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}

    # Ensure the response is around 200 words
    modified_prompt = prompt + " for 200 words"

    data = {"contents": [{"parts": [{"text": modified_prompt}]}]}

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=data)
        response.raise_for_status()
        gemini_data = response.json()

        if "candidates" in gemini_data and gemini_data["candidates"]:
            return gemini_data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "I'm having trouble understanding or responding right now. Please try again later."

    except requests.exceptions.RequestException:
        return "An error occurred while processing your request."


# ✅ Route to serve the HTML page
@app.route('/')
def index():
    return render_template("index.html")  # Ensure index.html exists inside /templates

# ✅ API route to handle chatbot responses
@app.route('/get_response', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_input = data.get("prompt", "")

    if not user_input:
        return jsonify({"reply": "Please provide a valid input."})

    response = get_gemini_response(user_input)
    return jsonify({"reply": response})

# ✅ Prevent favicon error
@app.route('/favicon.ico')
def favicon():
    return '', 204

# ✅ Run Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)


