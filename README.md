# Task 1: Data Cleaning & Preprocessing

Clean and prepare the Customer Personality Analysis dataset (handle missing values, duplicates, inconsistent formats, and incorrect data types).

- `marketing_campaign.csv` → Raw dataset
- `customer_personality_cleaned.csv` → Cleaned dataset
- `clean_customer_data.py` → Python code used for cleaning

# Steps Performed
1. Checked and filled missing values in `Income` with median.  
2. Removed duplicate rows.  
3. Standardized `Marital_Status` values (grouped rare categories into "Other").  
4. Converted `Dt_Customer` to `dd-mm-yyyy` format.  'ff' 
5. Renamed columns to lowercase with underscores.  
6. Corrected data types (year_birth → int, income → float, dt_customer → datetime).  
7. Sorted dataset in ascending order by Income.  

# Tools Used
- Python 3 (Pandas)
- Excel 
