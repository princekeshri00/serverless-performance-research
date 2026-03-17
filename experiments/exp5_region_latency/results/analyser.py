import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "../results")

os.makedirs(RESULTS_DIR, exist_ok=True)

CSV_FILE = os.path.join(RESULTS_DIR, "results.csv")

LATENCY_GRAPH = os.path.join(RESULTS_DIR, "latency_vs_region.png")
THROUGHPUT_GRAPH = os.path.join(RESULTS_DIR, "throughput_vs_region.png")

df = pd.read_csv(CSV_FILE)
df = df.sort_values(by="avg_latency_ms")


#region vs avg latency
plt.figure()
plt.bar(df["region"], df["avg_latency_ms"])
plt.xlabel("Region")
plt.ylabel("Average Latency (ms)")
plt.title("Region vs Average Latency")

plt.savefig(LATENCY_GRAPH)
plt.close()

#region vs throughput
plt.figure()
plt.bar(df["region"], df["requests_per_sec"])
plt.xlabel("Region")
plt.ylabel("Requests per Second")
plt.title("Region vs Throughput")

plt.savefig(THROUGHPUT_GRAPH)
plt.close()


print("success")