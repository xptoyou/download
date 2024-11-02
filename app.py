from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configure the path to your file
FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = "seif.zip"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download")
def download_file():
    # Send the file as an attachment to the user
    return send_from_directory(FILE_DIRECTORY, FILE_NAME, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
