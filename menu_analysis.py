from io import BytesIO
import os
import openai
from PIL import Image
from pdf2image import convert_from_bytes
import pytesseract
import requests

os.environ['PATH'] = r'C:\poppler-0.68.0\bin;' + os.environ['PATH']

def open_file(filepath):
    with open(filepath, 'r') as infile:
        return infile.read()

# Get the local key, and if it doesn't exist get the SM
def get_api_key():
    if os.path.isfile('openaiapikey.txt'):
        api_key = open_file('openaiapikey.txt')
    return api_key

# Uses function above to open and read this file's contents as the API Key.
openai.api_key = get_api_key()

def extract_text_from_image(img_bytes, file_ext):
    if file_ext == '.pdf':
        images = convert_from_bytes(img_bytes)
        pdf_text = []
        for img in images:
            text = pytesseract.image_to_string(img)
            pdf_text.append(text)
        return '\n'.join(pdf_text)
    else:
        img = Image.open(BytesIO(img_bytes))
        return pytesseract.image_to_string(img)
        

def call_openai_gpt(text, prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert translator and visualiser that analyses restaurant menus and images and assists users with queries about the menu or image."},
            {"role": "user", "content": f"{text}\n{prompt}"}
        ],
    )

    response_data = completion.choices[0].message['content']
    return response_data.strip()


def perform_analysis(image_bytes, file_ext, prompt):
    menu_text = extract_text_from_image(image_bytes, file_ext)
    analysis_result = call_openai_gpt(menu_text, prompt)
    return {
        prompt: analysis_result
    }