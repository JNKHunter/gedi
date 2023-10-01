#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    return render_template('results.html',input=request.form.get("user_input",""))
