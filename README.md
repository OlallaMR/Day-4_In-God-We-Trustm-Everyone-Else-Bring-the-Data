# Lab: Statistical Analysis of Marketing Channel Performance
## File Map

| File | Description |
|------|-------------|
| `data_exploration.ipynb` | Part 1: dataset loading, cleaning, metric calculation and visualizations |
| `statistical_analysis.ipynb` | Parts 2-3: pairwise t-tests, Fisher's exact test, multiple comparisons correction (Bonferroni + FDR) |
| `power_analysis.py` | Part 4: empirical power simulations and minimum sample size recommendations |
| `executive_memo.md` | Part 5: business recommendations, budget allocation, statistical caveats |
| `marketing_data_raw.csv` | Raw dataset from Kaggle (Marketing Campaign Performance Dataset) |
| `marketing_data.csv` | Cleaned dataset with derived metrics (CPA, ROAS, Revenue) |
| `group_metrics_overview.png` | Bar charts of key metrics by channel |
| `group_distributions.png` | Boxplots of CPA, ROAS and conversion rate distributions by channel |
| `metric_comparison_heatmap.png` | Heatmap of p-values from pairwise CPA comparisons |
| `rate_comparison.png` | Conversion rate comparison across channels |
| `correction_comparison.png` | Effect of Bonferroni and FDR corrections on significant comparisons |
| `power_analysis_cpa.png` | Power curves for different effect sizes and sample sizes |

---

## Dataset

**Name:** Marketing Campaign Performance Dataset
**Source:** Kaggle
**URL:** https://www.kaggle.com/datasets/manishabhatt22/marketing-campaign-performance-dataset
**License:** CC0-1.0
**Size:** 200,000 rows, 16 columns
**Channels:** Email, Facebook, Google Ads, Instagram, Website, YouTube

---

## Key Findings

- No statistically significant differences found between channels after multiple comparisons correction
- 90 days of data is sufficient to detect CPA differences of 10% or more (98.9% power)
- See `executive_memo.md` for full findings and recommendations
