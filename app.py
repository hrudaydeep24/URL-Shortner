from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

url_dict = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form['url']
    short_code = generate_short_code()
    url_dict[short_code] = url
    short_url = request.host_url + short_code
    return render_template('success.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url = url_dict.get(short_code)
    if url:
        return redirect(url)
    else:
        return "Invalid URL"

def generate_short_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choices(characters, k=6))
    return code

if __name__ == '__main__':
    app.run(debug=True)
