# app.py
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, GWC it's my new CODE it's my New code version"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
