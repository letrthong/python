
from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    telua_url = os.getenv("TELUA_URL", "https://default.url")
    return render_template("index.html", telua_url=telua_url)

if __name__ == "__main__":
    app.run(debug=True)
