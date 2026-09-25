# disclosure: Claude generated this script, but the data was manually written in the csv to produce the graph given the data I tracked

import csv
import matplotlib.pyplot as plt

threads, single, multi, speedup = [], [], [], []

with open("view1bythread.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        threads.append(int(row["threads"]))
        single.append(float(row["single"]))
        multi.append(float(row["multi"]))
        speedup.append(float(row["speedup"]))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Mandelbrot Thread Scaling (View 1, Contiguous Blocks)", fontsize=13, fontweight="bold")

# --- Runtime plot ---
ax1.plot(threads, single, "o--", color="#888", label="Serial")
ax1.plot(threads, multi, "o-", color="#2563eb", label="Threaded", linewidth=2, markersize=6)
ax1.set_xlabel("Number of Threads")
ax1.set_ylabel("Time (ms)")
ax1.set_title("Execution Time vs Thread Count")
ax1.legend()
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.set_xticks(threads)

# --- Speedup plot ---
ax2.plot(threads, threads, "--", color="#aaa", label="Ideal Linear Speedup")
ax2.plot(threads, speedup, "o-", color="#16a34a", linewidth=2, markersize=6, label="Actual Speedup")
ax2.set_xlabel("Number of Threads")
ax2.set_ylabel("Speedup (x)")
ax2.set_title("Speedup vs Thread Count")
ax2.legend()
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.set_xticks(threads)

plt.tight_layout()
plt.savefig("view1_speedup.png", dpi=150, bbox_inches="tight")
print("Saved view1_speedup.png")
plt.show()
