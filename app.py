from flask import Flask, render_template, request, jsonify
import menu_analysis
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_menu', methods=['POST'])
def analyze_menu():
    img = request.files['menu_image']
    prompt = request.form.get('prompt', '')

    # Add this line to get the uploaded file extension
    _, file_ext = os.path.splitext(img.filename)

    analysis = menu_analysis.perform_analysis(img.read(), file_ext, prompt)
    return jsonify(analysis), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(app.run(port=5001))