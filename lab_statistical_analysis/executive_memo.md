# Executive Memo: Marketing Channel Performance Analysis

**Date:** May 28, 2026
**Analyst:** Olalla
**Dataset:** Marketing Campaign Performance Dataset (Kaggle)
**Observations:** 200,000 campaigns across 6 channels

---

## Executive Summary

This analysis evaluated the performance of six marketing channels (Email, Facebook, Google Ads, Instagram, Website, YouTube) using statistical hypothesis testing on CPA and conversion rates. No statistically significant differences were found between channels after applying multiple comparisons correction. Budget allocation recommendations are based on composite performance rankings rather than statistically confirmed differences.

---

## Key Findings

### Top Performing Channels
- All six channels show remarkably similar CPA (~$246K-$250K) and conversion rates (~0.000146)
- Facebook shows the lowest CPA ($246,429) and highest ROAS (6.03)
- Email shows the highest total conversions (2,697) and clicks (18,493,963)

### Statistical Testing Results
- 15 pairwise CPA comparisons performed (t-tests): 0 significant at p<0.05
- 15 pairwise conversion rate comparisons performed (Fisher's exact): 0 significant at p<0.05
- After Bonferroni correction: 0 significant comparisons
- After FDR (Benjamini-Hochberg) correction: 0 significant comparisons
- All Cohen's d effect sizes were negligible (<0.02)

### Data Adequacy Assessment
- At 90 days of data, power to detect a 10% CPA difference: 98.9%
- At 90 days of data, power to detect a 5% CPA difference: 63.4%
- To reliably detect 5% differences, approximately 180 days of data are needed

---

## Recommendations

### Budget Allocation
Given the absence of statistically significant differences, allocation is based on composite ranking across CPA, ROAS, and conversion rate:

| Channel    | Allocation | % of Budget |
|------------|------------|-------------|
| Facebook   | $91,000    | 18.2%       |
| Email      | $88,000    | 17.6%       |
| Google Ads | $85,000    | 17.0%       |
| YouTube    | $84,000    | 16.8%       |
| Instagram  | $83,000    | 16.6%       |
| Website    | $69,000    | 13.8%       |

### Strategic Actions
1. Do not shift budget dramatically between channels until statistically significant differences are confirmed
2. Run controlled A/B tests with at least 180 days of data to detect small (5%) CPA differences
3. Monitor Facebook and Email closely as they show marginally better composite scores
4. Collect more granular data (daily level) to enable more sensitive statistical testing

---

## Statistical Caveats

- **Dataset limitations:** The dataset is synthetic, which explains the unusually uniform performance across channels. Real-world data would likely show more variability.
- **Multiple comparisons correction applied:** Both Bonferroni and FDR corrections were used. Results are conservative.
- **Confidence intervals:** 95% bootstrap CIs for CPA are very narrow due to large sample size, but this reflects dataset uniformity rather than real precision.
- **Statistical vs practical significance:** Even if small differences were statistically significant, a $1,000 CPA difference on a $250,000 base may not justify reallocation.
- **Power analysis limitations:** Simulations assume normally distributed CPA with 15% coefficient of variation. Real distributions may differ.
- **External factors:** Seasonality, competitive activity, and campaign quality are not captured in this dataset.

---

## Next Steps

1. Validate findings with real first-party data
2. Run 180-day controlled experiment to detect 5% CPA differences
3. Incorporate customer lifetime value (LTV) into channel scoring
4. Segment analysis by campaign type, audience, and location for deeper insights