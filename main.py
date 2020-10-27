#import trend_app_protect.start
import os
import sys
import hashlib
import time
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def p_root():
    return """
        <h1>This is TEST Web App</h1>
        <ul>
            <li><a href="/time">Time</li>
            <li><a href="/stop">Stop</li>
        </ul>
    """
@app.route('/time')
def p_time():
    return f"<h1>Time is: {time.asctime()}</h1>"

@app.route('/stop')
def log():
    sys.exit(1)

if __name__ == '__main__':
    app.run()