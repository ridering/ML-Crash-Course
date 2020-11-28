from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def main():
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    return render_template('index.html', posts=posts.json())


app.run(host='127.0.0.1', port=8080, debug=False)
