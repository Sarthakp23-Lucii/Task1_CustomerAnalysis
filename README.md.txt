# Task 1: Data Cleaning & Preprocessing

# Objective
Clean and prepare the Customer Personality Analysis dataset using Python IDLE (handle missing values, duplicates, inconsistent formats, and data types).

# Files Included
- marketing_campaign.csv → Raw dataset
- customer_personality_cleaned.csv → Cleaned dataset
- clean_customer_data.py → Python code run in IDLE
- screenshots/ → Optional screenshots showing results

# Steps Performed
1. Filled missing values in Income with median.  
2. Removed duplicate rows.  
3. Standardized Marital_Status (grouped rare categories into Other).  
4. Converted Dt_Customer to dd-mm-yyyy format.  
5. Renamed columns to lowercase with underscores.  
6. Corrected data types (year_birth → int, income → float, dt_customer → datetime).  
7. Sorted dataset in ascending order by Income.

# Tools Used
- Python 3 (IDLE)
- Pandas
- Excel (for verification)