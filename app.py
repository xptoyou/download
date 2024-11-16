from flask import Flask, send_file, render_template

app = Flask(__name__)

# Replace 'seif.zip' with the actual path to your file
FILE_PATH = "seif.zip"

@app.route("/")
def index():
    # Render the index.html file
    return render_template("index.html")

@app.route("/download")
def download_file():
    # Send the file for download
    return send_file(FILE_PATH, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

