from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "<p>Dit is een Test pagina, please ignore!</p>"