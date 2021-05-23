import os
from flask import Flask, render_template, flash, redirect, url_for, request, session
if os.path.exists("env.py"):
    import env



app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
