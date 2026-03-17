import subprocess
import re
import csv
import json
from datetime import datetime
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "../results")
os.makedirs(RESULTS_DIR, exist_ok=True)

CSV_FILE = os.path.join(RESULTS_DIR, "results.csv")
JSON_FILE = os.path.join(RESULTS_DIR, "results.json")

REGIONS = {
    "india": "",
    "taiwan": "",
    "us": ""
}

REQUESTS = 100
CONCURRENCY = 5


def run_hey(url):
    cmd = ["hey", "-n", str(REQUESTS), "-c", str(CONCURRENCY), url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def extract_metrics(output):
    metrics = {}

    avg = re.search(r"Average:\s+([\d.]+)\s+secs", output)
    if avg:
        metrics["avg_latency_ms"] = float(avg.group(1)) * 1000

    fastest = re.search(r"Fastest:\s+([\d.]+)\s+secs", output)
    if fastest:
        metrics["min_latency_ms"] = float(fastest.group(1)) * 1000

    slowest = re.search(r"Slowest:\s+([\d.]+)\s+secs", output)
    if slowest:
        metrics["max_latency_ms"] = float(slowest.group(1)) * 1000

    rps = re.search(r"Requests/sec:\s+([\d.]+)", output)
    if rps:
        metrics["requests_per_sec"] = float(rps.group(1))

    return metrics


def main():
    results = []

    print("Starting Regional Latency Test...\n")

    for region, url in REGIONS.items():
        print(f"Testing {region.upper()} → {url}")

        output = run_hey(url)
        metrics = extract_metrics(output)

        entry = {
            "region": region,
            "url": url,
            "requests": REQUESTS,
            "concurrency": CONCURRENCY,
            "timestamp": datetime.now().isoformat(),
            **metrics
        }

        results.append(entry)

        print(f"Done: {region} | Avg Latency: {metrics.get('avg_latency_ms', 'N/A')} ms\n")


    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    with open(JSON_FILE, "w") as f:
        json.dump(results, f, indent=4)

    print("success")


if __name__ == "__main__":
    main()