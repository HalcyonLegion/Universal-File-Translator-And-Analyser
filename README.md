# PDF or Image Reader

I had to install a couple of local programs for this to work, you will also need your own openaiapikey.txt file with your openai api key inside.

Poppler bins - https://blog.alivate.com.au/poppler-windows/
Tesseract OCR - https://github.com/UB-Mannheim/tesseract/wiki

# Install the requirements
pip install -r requirements.txt

# Setup your OpenAI API Key

Rename the .example file to just .txt and simply paste your key in and save, make sure there are no spaces.

# Usage

Open app.py in the integrated terminal and run python app.py

Go to the application on the local server (flask is traditionally served on http://127.0.0.1:5000)

Paste your Document into the file selector and then tell the AI what you'd like to do with it, it can be literally anything it's quite versatile.

For example I had it translate a Menu PDF into HTML code, I also asked it to translate a PDF from Swedish to English.