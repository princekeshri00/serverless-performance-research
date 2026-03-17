import json
import matplotlib.pyplot as plt

INPUT_FILE = "experiments/exp4_autoscaling_saturation/results/results.json"
LATENCY_GRAPH = "experiments/exp4_autoscaling_saturation/results/latency_vs_concurrency.png"
ERROR_GRAPH = "experiments/exp4_autoscaling_saturation/results/error_rate.png"
THROUGHPUT_GRAPH = "experiments/exp4_autoscaling_saturation/results/throughput.png"

with open(INPUT_FILE, "r") as f:
    data = json.load(f)

concurrency = [d["concurrency"] for d in data]
avg_latency = [d["avg_latency"] for d in data]
p95_latency = [d["p95_latency"] for d in data]
error_rate = [d["error_rate"] for d in data]
throughput = [d["throughput"] for d in data]



#latency vs concurrency
plt.figure()
plt.plot(concurrency, avg_latency, marker='o', label="Avg Latency")
plt.plot(concurrency, p95_latency, marker='s', linestyle='--', label="P95 Latency")

plt.xlabel("Concurrency")
plt.ylabel("Latency (seconds)")
plt.title("Latency vs Concurrency")
plt.legend()
plt.grid()

plt.savefig(LATENCY_GRAPH)
plt.close()


#error rate vs concurrency
plt.figure()
plt.plot(concurrency, error_rate, marker='o')

plt.xlabel("Concurrency")
plt.ylabel("Error Rate")
plt.title("Error Rate vs Concurrency")
plt.grid()

plt.savefig(ERROR_GRAPH)
plt.close()


#throughput vs concurrency
plt.figure()
plt.plot(concurrency, throughput, marker='o')

plt.xlabel("Concurrency")
plt.ylabel("Requests per Second")
plt.title("Throughput vs Concurrency")
plt.grid()

plt.savefig(THROUGHPUT_GRAPH)
plt.close()


print("success")