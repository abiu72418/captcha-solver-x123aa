# captcha-solver-x123aa

## Summary
captcha-solver-x123aa is a simple web application that solves CAPTCHAs by processing image URLs provided as query parameters. The application defaults to a sample CAPTCHA image if no URL is specified.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/captcha-solver-x123aa.git
   cd captcha-solver-x123aa
   ```
2. Install the required dependencies:
   ```bash
   pip install Flask pytesseract Pillow
   ```
3. Ensure Tesseract OCR is installed on your system. Follow the installation instructions for your OS from [Tesseract's GitHub](https://github.com/tesseract-ocr/tesseract).

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://127.0.0.1:5000/?url=https://.../image.png` to solve a CAPTCHA from the provided URL. If no URL is provided, it will default to the sample CAPTCHA image.

## Code Explanation
- **app.py**: The main application file that sets up a Flask web server, handles incoming requests, and processes CAPTCHA images using Tesseract OCR.
- **index.html**: The HTML template that displays the CAPTCHA image and the solved text.
- **style.css**: Basic styling for the web page.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.