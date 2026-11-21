import pandas as pd

# Read salary Excel file
salary_df = pd.read_excel("data/raw/salary.xlsx")

# Display first 5 records
print("First 5 Salary Records:")
print(salary_df.head())

# Total records
print("\nTotal Records:")
print(len(salary_df))

# Column information
print("\nColumn Information:")
salary_df.info()

# Data types
print("\nData Types:")
print(salary_df.dtypes)

# Missing values
print("\nMissing Values:")
print(salary_df.isnull().sum())

# Clean column names
salary_df.columns = salary_df.columns.str.strip()

print("\nCleaned Column Names:")
print(salary_df.columns.tolist())

print([repr(column) for column in salary_df.columns])

print("\nDuplicate Employee IDs:")
print(salary_df["employee_id"].duplicated().sum())



# Check invalid salary values
invalid_salary = salary_df[salary_df["basic_salary"] <= 0]

print("\nInvalid Salary Records:")
print(invalid_salary)

print("\nTotal Invalid Salaries:")
print(len(invalid_salary))


# Check invalid bonus values
invalid_bonus = salary_df[salary_df["bonus"] < 0]

print("\nInvalid Bonus Records:")
print(invalid_bonus)

print("\nTotal Invalid Bonuses:")
print(len(invalid_bonus))


# Check invalid salary months
invalid_dates = salary_df[salary_df["salary_month"].isnull()]

print("\nInvalid Salary Dates:")
print(len(invalid_dates))


# Read HR employee data
employees_df = pd.read_csv("data/processed/cleaned_employees.csv")

# Find unmatched employee IDs
unmatched_ids = salary_df[
    ~salary_df["employee_id"].isin(employees_df["employee_id"])
]

print("\nUnmatched Employee IDs:")
print(unmatched_ids)

print("\nTotal Unmatched Employees:")
print(len(unmatched_ids))


# Save cleaned salary data
salary_df.to_csv(
    "data/processed/cleaned_salary.csv",
    index=False
)

print("\nCleaned salary data saved successfully!")