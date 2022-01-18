from flask import Flask, render_template, request
app = Flask(__name__, template_folder='./')

@app.route("/")
def hello():
    return render_template('template.html')