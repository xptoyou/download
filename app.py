from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Specify the directory and file name
FILE_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')
FILE_NAME = "seif.zip"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download")
def download_file():
    try:
        # Send the file as an attachment
        return send_from_directory(FILE_DIRECTORY, FILE_NAME, as_attachment=True)
    except FileNotFoundError:
        return "File not found. Please check the file path.", 404

if __name__ == "__main__":
    app.run(debug=True)

