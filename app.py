import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Replace with your actual API key
GENAI_API_KEY = "AIzaSyCwIkYsvA43zrZFDaoQByzu-MHgjRyxzQA"
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "I didn't hear anything!"}), 400
    
    try:
        # Generate response from AI
        response = model.generate_content(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
