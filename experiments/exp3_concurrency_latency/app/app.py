from flask import Flask, jsonify
import time
import os

app = Flask(__name__)

@app.route("/")
def handle_request():
    start_time = time.time()

    time.sleep(0.05)  # 50ms workload
    
    latency = (time.time() - start_time) * 1000

    return jsonify({
        "message": "ok",
        "latency_ms": latency,
        "instance": os.getenv("K_REVISION", "unknown")
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)