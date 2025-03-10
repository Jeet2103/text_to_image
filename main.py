from flask import Flask, render_template, jsonify, request
import os
from openai import OpenAI
from flask_cors import CORS

# Set up OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generateimages', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    print(f"Received prompt: {prompt}")

    try:
        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            n=3,
            size="256x256"
        )

        # Correct way to extract image URLs
        image_urls = [img.url for img in response.data]

        return jsonify({"data": image_urls})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
