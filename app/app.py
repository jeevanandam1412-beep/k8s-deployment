
import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

APP_NAME = "CloudOps Dashboard"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "development")


@app.route("/")
def home():
    return render_template(
        "index.html",
        app_name=APP_NAME,
        app_version=APP_VERSION,
        app_env=APP_ENV,
    )


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


@app.route("/ready")
def ready():
    return jsonify(status="ready"), 200


@app.route("/version")
def version():
    return jsonify(
        application=APP_NAME,
        version=APP_VERSION,
        environment=APP_ENV,
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
