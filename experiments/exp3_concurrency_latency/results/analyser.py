import pandas as pd
import matplotlib.pyplot as plt
import os
import time

DATA_PATH = "experiments/exp3_concurrency_latency/results/results.csv"

df = pd.read_csv(DATA_PATH)
df["latency_ms"] = pd.to_numeric(df["latency_ms"], errors="coerce")
df = df.dropna()


#latency vs concurrency
avg_latency = df.groupby("concurrency")["latency_ms"].mean()

plt.figure()
avg_latency.plot(marker="o")
plt.xlabel("Concurrency")
plt.ylabel("Average Latency (ms)")
plt.title("Latency vs Concurrency")
plt.grid()

plt.savefig("experiments/exp3_concurrency_latency/results/latency_vs_concurrency.png")
plt.close()


#boxplot (distribution)
plt.figure()
df.boxplot(column="latency_ms", by="concurrency")
plt.xlabel("Concurrency")
plt.ylabel("Latency (ms)")
plt.title("Latency Distribution by Concurrency")
plt.suptitle("")

plt.savefig("experiments/exp3_concurrency_latency/results/boxplot.png")
plt.close()


#throughput calculation
throughput = {}
for c in df["concurrency"].unique():
    subset = df[df["concurrency"] == c]
    
    total_requests = len(subset)
    total_time_sec = subset["latency_ms"].sum() / 1000
    
    if total_time_sec > 0:
        throughput[c] = total_requests / total_time_sec
    else:
        throughput[c] = 0

throughput_series = pd.Series(throughput).sort_index()

plt.figure()
throughput_series.plot(marker="o")
plt.xlabel("Concurrency")
plt.ylabel("Requests per Second")
plt.title("Throughput vs Concurrency")
plt.grid()

plt.savefig("experiments/exp3_concurrency_latency/results/throughput.png")
plt.close()


print("done")