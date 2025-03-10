import streamlit as st
import requests

def get_images(prompt):
    url = "http://localhost:5000/generateimages"
    response = requests.post(url, json={"prompt": prompt})


    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        st.error("Error fetching images")
        return []

st.title("AI Image Generator")

prompt = st.text_input("Enter your prompt:")

if st.button("Generate Images"):
    if prompt:
        st.write(f"### Generated images for: {prompt}")
        image_urls = get_images(prompt)

        if image_urls:
            cols = st.columns(len(image_urls))
            for col, img_url in zip(cols, image_urls):
                col.image(img_url, use_column_width=True)
        else:
            st.error("No images generated. Try a different prompt.")
    else:
        st.warning("Please enter a prompt.")
