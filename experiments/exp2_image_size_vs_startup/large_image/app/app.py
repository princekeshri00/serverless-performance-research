from flask import Flask
import time
import os

app = Flask(__name__)

@app.route("/")
def test():
    start = time.time()
    time.sleep(0.05)
    latency = time.time() - start

    return {
        "latency": latency,
        "instance": os.environ.get("K_REVISION", "unknown")
    }