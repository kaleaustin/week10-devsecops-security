from flask import Flask
import hashlib
import secrets
import os

app = Flask(__name__)

PASSWORD = os.getenv("PASSWORD")
API_KEY = os.getenv("API_KEY")

@app.route("/")
def home():
    return "Week 10 DevSecOps - Secure Version"

@app.route("/hash")
def sha256():
    return hashlib.sha256(b"secure").hexdigest()

@app.route("/token")
def token():
    return secrets.token_hex(16)

if __name__ == "__main__":
    app.run(debug=False)
