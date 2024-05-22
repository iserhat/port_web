from flask import Flask, render_template, redirect, url_for, request
from bs4 import BeautifulSoup
from selenium import webdriver
from flask_bootstrap import Bootstrap5
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
Bootstrap5(app=app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/certificates")
def getCertificates():
    return render_template("certificates.html")

if __name__ == '__main__':
    app.run(debug=True)