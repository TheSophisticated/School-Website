from flask import Blueprint

@app.route('/')
def home():
    return "Hello World"
