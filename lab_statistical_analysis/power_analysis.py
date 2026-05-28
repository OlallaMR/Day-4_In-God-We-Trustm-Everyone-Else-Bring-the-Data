import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

df = pd.read_csv("marketing_data.csv")
grouping_col = "Channel_Used"

def empirical_power_cpa(true_diff_pct, base_cpa, n_days, n_sim=1000, alpha=0.05):
    rejections = 0
    for _ in range(n_sim):
        std = base_cpa * 0.15
        a = np.random.normal(base_cpa, std, n_days)
        a = np.clip(a, base_cpa * 0.5, np.inf)
        b = np.random.normal(base_cpa * (1 + true_diff_pct), std, n_days)
        b = np.clip(b, base_cpa * 0.5, np.inf)
        _, p = ttest_ind(a, b)
        if p < alpha:
            rejections += 1
    return rejections / n_sim

base_cpa = df["CPA_row"].dropna().mean()
effect_sizes = [0.05, 0.10, 0.15, 0.20]
sample_sizes = [30, 60, 90, 120, 180]

print(f"Base CPA: {base_cpa:.2f}")
print("Running power simulations...")

power_results = []
for eff in effect_sizes:
    for n in sample_sizes:
        power = empirical_power_cpa(eff, base_cpa, n, n_sim=1000)
        power_results.append({
            "effect_size_pct": int(eff * 100),
            "n_days": n,
            "power": round(power, 3)
        })

power_df = pd.DataFrame(power_results)

fig, ax = plt.subplots(figsize=(10, 6))
for eff in [5, 10, 15, 20]:
    subset = power_df[power_df["effect_size_pct"] == eff]
    ax.plot(subset["n_days"], subset["power"], marker="o", label=f"{eff}% difference")

ax.axhline(0.80, color="red", linestyle="--", linewidth=1.2, label="80% power target")
ax.set_xlabel("Sample size (days)")
ax.set_ylabel("Statistical power")
ax.set_title("Power Curves by Effect Size", fontweight="bold")
ax.legend()
ax.grid(True, alpha=0.4)
plt.tight_layout()
plt.savefig("power_analysis_cpa.png", bbox_inches="tight")
plt.show()

print("\n=== MINIMUM DAYS FOR 80% POWER ===")
print(f"{'Effect Size':<15} {'Min Days':<12} {'Status (90 days)'}")
print("-" * 45)
for eff in [5, 10, 15, 20]:
    subset = power_df[power_df["effect_size_pct"] == eff].sort_values("n_days")
    sufficient = subset[subset["power"] >= 0.80]
    if len(sufficient) > 0:
        min_days = sufficient.iloc[0]["n_days"]
        status = "Sufficient" if min_days <= 90 else "Insufficient"
    else:
        min_days = ">180"
        status = "Insufficient"
    print(f"{str(eff)+'%':<15} {str(min_days):<12} {status}")

print("\n=== CURRENT DATA ADEQUACY ===")
for eff in [5, 10, 15, 20]:
    subset = power_df[power_df["effect_size_pct"] == eff]
    power_90 = subset[subset["n_days"] == 90]["power"].values
    if len(power_90) > 0:
        print(f"{eff}% difference -> Power at 90 days: {power_90[0]:.1%}")