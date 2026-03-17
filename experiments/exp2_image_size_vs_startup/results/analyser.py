import pandas as pd
import matplotlib.pyplot as plt

small = pd.read_csv("./experiments/exp2_image_size_vs_startup/results/small_image_latency.csv")
medium = pd.read_csv("./experiments/exp2_image_size_vs_startup/results/medium_image_latency.csv")
large = pd.read_csv("./experiments/exp2_image_size_vs_startup/results/large_image_latency.csv")

# Box plot
plt.figure()
plt.boxplot(
    [small["latency"], medium["latency"], large["latency"]],
    labels=["Small", "Medium", "Large"]
)

plt.ylabel("Latency (seconds)")
plt.title("Image Size vs Cold Start Latency")

plt.savefig("./experiments/exp2_image_size_vs_startup/results/startup_comparison_box.png")
plt.close()


# Scatter points
plt.figure()
plt.scatter(["Small"] * len(small), small["latency"])
plt.scatter(["Medium"] * len(medium), medium["latency"])
plt.scatter(["Large"] * len(large), large["latency"])

plt.ylabel("Latency (seconds)")
plt.title("Image Size vs Cold Start Latency (Raw Data)")

plt.savefig("./experiments/exp2_image_size_vs_startup/results/startup_comparison_scatter.png")
plt.close()