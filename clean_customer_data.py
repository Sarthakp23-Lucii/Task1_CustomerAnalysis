import pandas as pd

df = pd.read_csv("marketing_campaign.csv", sep="\t")

print("Missing values before cleaning:\n", df.isnull().sum())

df.fillna({'Income': df['Income'].median()}, inplace=True)

df.drop_duplicates(inplace=True)

df['Marital_Status'] = df['Marital_Status'].replace(
    ['Absurd', 'YOLO', 'Alone'], 'Other'
)

df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], dayfirst=True, errors='coerce')

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df['year_birth'] = df['year_birth'].astype(int)
df['income'] = df['income'].astype(float)

df.to_csv("customer_personality_cleaned.csv", index=False)

print("\n✅ Cleaning Completed! File saved as 'customer_personality_cleaned.csv'")

print("\nSummary of cleaning steps:")
print("- Filled missing Income with median value")
print("- Removed duplicate rows")
print("- Standardized Marital_Status (rare values → Other)")
print("- Converted Dt_Customer to datetime format")
print("- Renamed columns to lowercase with underscores")
print("- Ensured correct data types (year_birth=int, income=float, dt_customer=datetime)")
