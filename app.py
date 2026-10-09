from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "student_app_request_total",
    "Total requests by endpoint",
    ["endpoint"]
)

@app.route("/")
def home():
    REQUEST_COUNT.labels(endpoint="/").inc()
    return "Student App - MLOps Practical"

@app.route("/login")
def login():
    REQUEST_COUNT.labels(endpoint="/login").inc()
    return "Login Page"

@app.route("/dashboard")
def dashboard():
    REQUEST_COUNT.labels(endpoint="/dashboard").inc()
    return "Dashboard Page"

@app.route("/health")
def health():
    REQUEST_COUNT.labels(endpoint="/health").inc()
    return "Application is healthy"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

