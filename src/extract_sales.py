import pandas as pd

# Read Sales JSON file
sales_df = pd.read_json("data/raw/sales.json")

# Display first 5 records
print("First 5 Sales Records:")
print(sales_df.head())

# Total records
print("\nTotal Records:")
print(len(sales_df))

# Column information
print("\nColumn Information:")
sales_df.info()

# Data types
print("\nData Types:")
print(sales_df.dtypes)

# Missing values
print("\nMissing Values:")
print(sales_df.isnull().sum())

# Convert sale_date into datetime format
sales_df["sale_date"] = pd.to_datetime(
    sales_df["sale_date"]
)

print("\nUpdated Data Types:")
print(sales_df.dtypes)

# Check duplicate transaction IDs
print("\nDuplicate Transaction IDs:")
print(sales_df["transaction_id"].duplicated().sum())


# Check invalid sale amounts
invalid_sales = sales_df[sales_df["sale_amount"] <= 0]

print("\nInvalid Sales Records:")
print(invalid_sales)

print("\nTotal Invalid Sales:")
print(len(invalid_sales))



# Read cleaned HR employee data
employees_df = pd.read_csv("data/processed/cleaned_employees.csv")

# Find unmatched employee IDs
unmatched_ids = sales_df[
    ~sales_df["employee_id"].isin(employees_df["employee_id"])
]

print("\nUnmatched Employee IDs:")
print(unmatched_ids)

print("\nTotal Unmatched Employees:")
print(len(unmatched_ids))


# Save cleaned sales data
sales_df.to_csv(
    "data/processed/cleaned_sales.csv",
    index=False
)

print("\nCleaned sales data saved successfully!")