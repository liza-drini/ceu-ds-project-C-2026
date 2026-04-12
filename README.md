# Linking Feral Cat Density to Sheep Industry Outcomes in Australia

This repository contains the code, notebooks, and processed datasets for the **Data Science Project** on the relationship between feral cats and sheep-industry outcomes in Australia.

The project combines 4 data dimensions:

- **farm data**: annual sheep-related indicators such as lambs, rams, ewes, sheep flock size, animals shorn, and sheep purchased
- **cat occurrence data**: CSIRO-based feral cat occurrence records aggregated by year and territory
- **economic data**: cat-related and mixed-species cost estimates derived from the InvaCost framework
- **news data**: yearly media indicators derived from GDELT, including article volume, tone, and media visibility

The goal of the project is to explore whether sheep-industry outcomes align with feral cat occurrence, economic costs, and public/media attention.

---

## Repository overview

The workflow is organized as a sequence of preparation, merging, and analysis steps.

### Main folders

- `src/` – notebooks and scripts for data preparation, merging, and analysis
- `datasets/` – processed intermediate and final CSV files
- `pngs/` – exported figures used in analysis and presentations
- `raw data/` – input files used in preparation steps 

---

## Recommended notebook order

To follow the project from raw inputs to final analysis, the notebooks should be viewed in the following order:

### 1. Preparation of individual datasets
1. `farm.ipynb`  
   Prepares the farm dataset from separate sheep-related Excel files and saves the result as `farm.csv`.

2. `realtime_prep.ipynb`  
   Filters and prepares the cat occurrence data from the original CSIRO invasive-species dataset.

3. 'real_time_visualization.ipynb'
    Visualizes patterns in cat occurence dataset.

4. `econ_ds_cleaning.ipynb`  
   Cleans and filters the economic dataset and saves the result as `eco_df_clean.csv`.

5. `news.py`  
   Builds the yearly aggregated news dataset from processed GDELT-based inputs and saves the result as `news.csv`.

6. `news_analysis.ipynb`  
   Performs descriptive and exploratory analysis of the news dataset before merging.

### 2. Layered merging of datasets
6. `farm_cat_merge.ipynb`  
   Merges the farm and cat datasets and saves the output as `farm_cat.csv`.

7. `farm_cat_eco_merge.ipynb`  
   Extends the merged farm-cat dataset with economic variables and saves the result as `farm_cat_eco.csv`.

8. `farm_cat_eco_news_merge.ipynb`  
   Merges the national-level farm-cat-economic dataset with the news dataset and saves the final output as `farm_cat_eco_news.csv`.

### 3. Exploratory analysis of merged datasets
9. `cat_farm_analysis.ipynb`  
   Explores relationships between sheep indicators and feral cat occurrence.

10. `econ_farm_cat_visual.ipynb`  
    Visualizes the economic dimension of the farm-cat-economic dataset.

11. `econ_farm_cat_analysis.ipynb`  
    Analyzes the relationship between sheep indicators, cat occurrence, and economic costs.

12. `farm_cat_eco_news.ipynb`  
    Explores the final merged dataset combining sheep indicators, cat occurrence, economic costs, and media attention.
