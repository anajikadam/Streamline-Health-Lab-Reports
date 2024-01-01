import streamlit as st
import os
from PIL import Image

from genai_app import get_gemini_response

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

##initialize our streamlit app
st.set_page_config(page_title="Gemini Application Demo")

st.header("Gemini Application: Health laboratory Report Data Extractor")
input = st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image invoice")

input_prompt = """
               You are an expert in understanding Health laboratory report.
               You will receive input images as laboratory report &
               you will have to answer questions based on the input image
               """


## If ask button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)



