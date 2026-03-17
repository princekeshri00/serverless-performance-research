import requests
import time
import concurrent.futures
import csv
import os

URL = ""
RESULTS_PATH = "experiments/exp3_concurrency_latency/results/results.csv"

def send_request():
    start = time.time()
    try:
        r = requests.get(URL)
        latency = (time.time() - start) * 1000
        return latency
    except:
        return None


def run_test(concurrency, total_requests=100):
    latencies = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(send_request) for _ in range(total_requests)]

        for f in concurrent.futures.as_completed(futures):
            result = f.result()
            if result is not None:
                latencies.append(result)

    return latencies


def save_results(concurrency, latencies):
    file_exists = os.path.isfile(RESULTS_PATH)

    with open(RESULTS_PATH, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["concurrency", "latency_ms"])

        for l in latencies:
            writer.writerow([concurrency, l])


if __name__ == "__main__":
    concurrency_levels = [1, 5, 10, 20, 40, 80]

    for c in concurrency_levels:
        print(f"\nRunning test with concurrency = {c}")

        latencies = run_test(c)

        print(f"Avg latency: {sum(latencies)/len(latencies):.2f} ms")
        print(f"Requests completed: {len(latencies)}")

        save_results(c, latencies)