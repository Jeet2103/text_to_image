# AI Image Generator

This project consists of a Flask API and a Streamlit frontend to generate AI-powered images using OpenAI's DALL·E model.

## Features

- Enter a text prompt to generate images.
- Displays multiple dall-e-2 AI model generated images.
- Flask backend handles API requests to OpenAI.
- Streamlit frontend for user-friendly interaction.

## Installation

### Clone the repository:
```sh
git clone https://github.com/Jeet2103/text_to_image.git
```

### Set up a virtual environment (optional but recommended):
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies:
```sh
pip install -r requirements.txt
```

### Set OpenAI API key:
```sh
export OPENAI_API_KEY='your_api_key_here'  # On Windows: set OPENAI_API_KEY=your_api_key_here
```

## Running the Application

### 1. Start the Flask Backend
```sh
python app.py
```

### 2. Start the Streamlit Frontend
```sh
streamlit run streamlit_app.py
```

## Usage

- Open the Streamlit app in your browser.
- Enter a text prompt and generate images.
- View AI-generated images directly.

## Requirements

- Python 3.8+
- Flask
- Streamlit
- OpenAI Python SDK


