# To Generate Data
1. First, make sure the `utils/data_paths.py` has the correct mounting point. By default, this doesn't need to be changed.  
2. Run the clean pipelines in `python_src/pipeline_clean`
3. Run `figures.ipynb`
4. Run `utils/analysis/analyze_stats.ipynb`
5. Run `utils/analysis/ad_vs_reads/read_AD.ipynb`
6. Run `utils/paper/heatmaps.ipynb`