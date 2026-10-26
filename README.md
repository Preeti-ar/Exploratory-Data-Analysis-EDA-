
# Exploratory Data Analysis (EDA) Project

## 1. Project Overview
This project explores a sales dataset to identify patterns, trends, and useful insights using Python.

## 2. Objectives
- Understand the dataset structure.
- Identify missing values and duplicate records.
- Clean the dataset.
- Calculate descriptive statistics.
- Analyze revenue by product and city.
- Visualize relationships between numerical variables.
- Present findings using graphs.

## 3. Tools and Technologies
- Python
- Pandas
- Matplotlib

## 4. Dataset Description
The dataset contains sales information with the following columns:

- order_id: Unique order identifier
- product: Name of the product
- city: City where the sale occurred
- sales_channel: Online or store
- units_sold: Number of units sold
- unit_price: Price per unit
- discount_percent: Discount rate
- customer_satisfaction: Customer satisfaction score

The dataset is synthetic and created for educational purposes.

## 5. Data Cleaning
The project performs these cleaning steps:

- Checks missing values.
- Identifies and removes duplicate rows.
- Fills missing city values with "Unknown".
- Fills missing discount values using the median.
- Calculates revenue after discounts.

Revenue = Units Sold × Unit Price × (1 − Discount)

## 6. Exploratory Data Analysis
The project includes:

- Dataset overview
- Descriptive statistics
- Revenue by product
- Revenue by city
- Correlation analysis

## 7. Visualizations
The Python script generates:

- Revenue by Product chart
- Revenue by City chart
- Correlation Matrix

## 8. Project Files
- analysis.py: Main Python analysis script
- sales_eda_dataset.csv: Sample sales dataset
- requirements.txt: Required Python libraries
- README.md: Project documentation

## 9. How to Run
Install Python 3, then install the required libraries:

pip install -r requirements.txt

Run the project:

python analysis.py

The results and charts are saved in the outputs folder.

## 10. Conclusion
This project demonstrates how Python can be used to clean data, calculate statistics, identify trends, and create visualizations.

## 11. Limitations
This project uses synthetic sample data. Its findings should not be treated as conclusions about real businesses.
