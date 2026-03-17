import requests
import time
import csv
import os

print("Waiting to make sure Cold Start...")
time.sleep(120)
print("Starting...\n\n\n")

URLS = {
    "small": "https://exp2-small-546481439801.us-central1.run.app",
    "medium": "https://exp2-medium-546481439801.us-central1.run.app",
    "large": "https://exp2-large-546481439801.us-central1.run.app"
}

def test_service(name, url):
    results = []

    print(f"\nTesting {name}...\n")

    for i in range(25):
        time.sleep(30)

        start = time.time()
        r = requests.get(url)
        latency = time.time() - start

        print(f"{i+1}: {latency:.3f}s")
        results.append(latency)
    

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RESULTS_DIR = os.path.join(BASE_DIR, "..", "results")
    os.makedirs(RESULTS_DIR, exist_ok=True)
    
    file_path = os.path.join(RESULTS_DIR, f"{name}_image_latency.csv")
    with open(file_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["latency"])
        for r in results:
            writer.writerow([r])


for name, url in URLS.items():
    test_service(name, url)
