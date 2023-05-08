# TODO
## Legend
- (C): will need new code
- (F): needs figures

## 4-3-23
1. Add unclassified amount to each pipeline. Not reported by Biobakery by default, but can be enabled.
    - Can be back-calculated for Woltka. (C)
2. Confusion Matrix for NIST data (C)(F)
    - Need to run NEG on pipelines (only BB4).
    - Calculate TP, FP, TN, FN for each pipeline.
3. Need to figure out how to do sensitivity filtering. If we filter out below 0.01% RA, should any observed features in the left joined data count as 0 if below?