from flask import Flask, request, render_template
import pytesseract
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFElEQVQYV2NkQAP/Gf4bBjCqAEMAAHQDAh0U8PYAAAAASUVORK5CYII=')
    image = None
    if url.startswith('data:image/png;base64,'):
        image_data = url.split(',')[1]
        image = Image.open(BytesIO(base64.b64decode(image_data)))
    else:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
    solved_text = pytesseract.image_to_string(image)
    return render_template('index.html', captcha_image=url, solved_text=solved_text)

if __name__ == '__main__':
    app.run(debug=True)