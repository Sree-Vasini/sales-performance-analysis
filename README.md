# Sales Performance Analysis (Python)

**Tools Used:** Python, Pandas, Matplotlib  
**Dataset:** Synthetic sales dataset generated using Python  

## Project Goal
The goal of this project is to analyze sales transactions to understand:
- Total revenue and key KPIs
- Monthly sales trends
- Top performing categories and products

## What I Did
- Generated a realistic synthetic sales dataset with 5,000 records  
- Cleaned and explored the data using Python  
- Calculated key business metrics  
- Built visualizations to analyze trends  

## Key Insights
- Identified top revenue-generating categories  
- Analyzed monthly revenue patterns  
- Found best performing products  

## Project Structure

sales-performance-analysis/
  data/               -> Generated CSV dataset
  src/                -> Python scripts to generate data
  notebooks/          -> Analysis scripts
  outputs/            -> Charts and results

## How to Run the Project

1. Install dependencies:
pip install -r requirements.txt

2. Generate dataset:
python src/generate_data.py

3. Run analysis:
python notebooks/01_sales_analysis.py

## Outputs

The analysis generates:
- Monthly revenue trend chart  
- Revenue by category chart  
- Top products summary  
