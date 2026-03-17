from flask import Flask, jsonify
import time
import os

app = Flask(__name__)
PROCESSING_TIME = float(os.environ.get("PROCESSING_TIME", 0.2))

@app.route("/")
def home():
    start = time.time()
    time.sleep(PROCESSING_TIME)
    latency = time.time() - start

    return jsonify({
        "message": "OK",
        "processing_time": PROCESSING_TIME,
        "actual_latency": latency
    })

@app.route("/health")
def health():
    return "healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)