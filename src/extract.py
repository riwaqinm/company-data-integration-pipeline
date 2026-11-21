import pandas as pd

# Read employee CSV file
employees_df = pd.read_csv("data/raw/employees.csv")

# Display first 5 records
print(employees_df.head())

print("\nTotal Records:")
print(len(employees_df))

print("\nColumn Information:")
print(employees_df.info())

print("\nStatistical Summary:")
print(employees_df.describe(include="all"))


# Convert hire_date into datetime format
employees_df["hire_date"] = pd.to_datetime(
    employees_df["hire_date"]
)

print("\nUpdated Data Types:")
print(employees_df.dtypes)

print("\nMissing Values:")
print(employees_df.isnull().sum())

print("\nDuplicate Records:")
print(employees_df.duplicated().sum())

print("\nDuplicate Employee IDs:")
print(employees_df["employee_id"].duplicated().sum())

print("\nDuplicate Emails:")
print(employees_df["email"].duplicated().sum())



# Remove extra spaces from text columns
text_columns = ["employee_name", "email", "department"]

for column in text_columns:
    employees_df[column] = employees_df[column].str.strip()

print("\nData after removing extra spaces:")
print(employees_df.head())

# Standardize department names
employees_df["department"] = employees_df["department"].str.upper()

print("\nStandardized Departments:")
print(employees_df["department"].unique())



print("\nFinal Data Types:")
print(employees_df.dtypes)

print("\nFinal Missing Values:")
print(employees_df.isnull().sum())

print("\nFinal Duplicate Employee IDs:")
print(employees_df["employee_id"].duplicated().sum())


# Save cleaned employee data
employees_df.to_csv(
    "data/processed/cleaned_employees.csv",
    index=False
)

print("\nCleaned employee data saved successfully!")