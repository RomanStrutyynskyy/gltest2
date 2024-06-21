from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")

def index():
	# now=datetime.now()
	# ans = request.get_data(as_text=True)
	return render_template("index.html", now=datetime.now())

if __name__ == "__main__":
	app.run()