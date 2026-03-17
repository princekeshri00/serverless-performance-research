import requests
import time
import csv
import os

URL = ""
file_path = "experiments/exp1_cold_start_latency/results/warm_results.csv"
file_exists = os.path.isfile(file_path)

with open(file_path, "a", newline="") as f:

    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["request_id", "latency_ms"])

    for i in range(1, 51):

        start = time.time()
        r = requests.get(URL, headers={"Connection": "close"})
        latency = (time.time() - start) * 1000

        print(f"{i}: {latency:.2f} ms")
        writer.writerow([i, latency])

        time.sleep(1)