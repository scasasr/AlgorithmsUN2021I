import time
from flask import Flask, render_template

import time

app = Flask(__name__)

@app.route('/')
def index():
    r = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return render_template('index.html',r=r)

if __name__ == "__main__":
    app.run()
