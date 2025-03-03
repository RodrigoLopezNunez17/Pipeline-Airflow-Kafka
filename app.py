from flask import Flask, render_template, url_for, request, redirect
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/init', methods=["POST"])
def init():
    subprocess.run("source app.sh", shell = True)
    subprocess.run("sleep 5", shell = True)
    render_template('initiation.html', methods = ['POST', 'GET'])
    return redirect('localhost:8080')

if __name__ == "__main__":
    app.run(debug = True)