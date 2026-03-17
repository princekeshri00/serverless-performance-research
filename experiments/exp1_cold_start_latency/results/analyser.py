import pandas as pd
import matplotlib.pyplot as plt

warm_file = "experiments/exp1_cold_start_latency/results/warm_results.csv"
cold_file = "experiments/exp1_cold_start_latency/results/cold_results.csv"

warm = pd.read_csv(warm_file)
cold = pd.read_csv(cold_file)
warm_latency = warm.iloc[:,1]
cold_latency = cold.iloc[:,1]

print(f"Warm Mean: {warm_latency.mean():.2f} ms")
print(f"Cold Mean: {cold_latency.mean():.2f} ms")
print(f"Warm Median: {warm_latency.median():.2f} ms")
print(f"Cold Median: {cold_latency.median():.2f} ms")


#cold vs warm
plt.figure()
plt.boxplot([warm_latency, cold_latency], labels=["Warm", "Cold"])

plt.ylabel("Latency (ms)")
plt.title("Cold vs Warm Request Latency")

plt.savefig("experiments/exp1_cold_start_latency/results/cold_vs_warm_latency.png")
plt.close()



#distributions

#cold distribution
plt.figure()
plt.hist(cold_latency, bins=10, alpha=0.6, label="Cold", color="blue")

plt.xlabel("Latency (ms)")
plt.ylabel("Frequency")
plt.title("Cold Latency Distribution")

plt.legend()

plt.savefig("experiments/exp1_cold_start_latency/results/cold_latency_distribution_overlay.png")
plt.close()

#warm distribution
plt.figure()
plt.hist(warm_latency, bins=10, alpha=0.6, label="Warm", color="red")

plt.xlabel("Latency (ms)")
plt.ylabel("Frequency")
plt.title("Warm Latency Distribution")

plt.legend()

plt.savefig("experiments/exp1_cold_start_latency/results/warm_latency_distribution_overlay.png")
plt.close()

print("\nSuccess")