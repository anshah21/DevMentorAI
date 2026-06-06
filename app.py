from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)
CORS(app)

# Configure Gemini API
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


# Home Route
@app.route("/")
def home():
    return "DevMentor AI Backend Running!"


# Review Route
@app.route("/review", methods=["POST"])
def review_code():

    try:

        data = request.get_json()

        code = data.get("code", "")
        language = data.get("language", "Python")

        prompt = f"""
Review the following {language} code:

{code}

Provide:

1. Bugs Found
2. Improvements
3. Corrected Code
4. Time Complexity
5. Space Complexity
6. Learning Recommendations

Format clearly.
"""

        response = model.generate_content(prompt)

        return jsonify({
            "review": response.text
        })

    except Exception as e:

        print("REVIEW ERROR:", e)

        return jsonify({
            "review": f"Error: {str(e)}"
        }), 500


# Quiz Route
@app.route("/quiz", methods=["POST"])
def generate_quiz():

    try:

        data = request.get_json()

        code = data.get("code", "")
        language = data.get("language", "Python")

        prompt = f"""
Based on this {language} code:

{code}

Generate:

1. Three Multiple Choice Questions (MCQs)
2. Two Short Answer Questions
3. One Coding Challenge

Include answers.
"""

        response = model.generate_content(prompt)

        return jsonify({
            "quiz": response.text
        })

    except Exception as e:

        print("QUIZ ERROR:", e)

        return jsonify({
            "quiz": f"Error: {str(e)}"
        }), 500


# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)