import pandas as pd

# Load cleaned HR data
employees_df = pd.read_csv("data/processed/cleaned_employees.csv")

# Load cleaned Finance data
salary_df = pd.read_csv("data/processed/cleaned_salary.csv")

# Load cleaned Sales data
sales_df = pd.read_csv("data/processed/cleaned_sales.csv")


# Display record counts
print("HR Records:", len(employees_df))
print("Finance Records:", len(salary_df))
print("Sales Records:", len(sales_df))


# Merge HR and Finance data
hr_finance_df = pd.merge(
    employees_df,
    salary_df,
    on="employee_id",
    how="left"
)

print("\nHR + Finance Integrated Data:")
print(hr_finance_df.head())

print("\nTotal Integrated Records:")
print(len(hr_finance_df))



# Merge HR + Finance with Sales data
company_df = pd.merge(
    hr_finance_df,
    sales_df,
    on="employee_id",
    how="left"
)

print("\nComplete Company Integrated Data:")
print(company_df.head())

print("\nTotal Integrated Records:")
print(len(company_df))


# Validate integrated data

print("\nColumn Names:")
print(company_df.columns.tolist())

print("\nMissing Values:")
print(company_df.isnull().sum())

print("\nDuplicate Employee IDs:")
print(company_df["employee_id"].duplicated().sum())

print("\nTotal Rows:")
print(len(company_df))



# Save integrated company data
company_df.to_csv(
    "data/processed/integrated_company_data.csv",
    index=False
)

print("\nIntegrated company data saved successfully!")

# Employee ID validation

invalid_employee_ids = company_df[
    company_df["employee_id"].isnull() |
    (company_df["employee_id"] <= 0)
]

print("\nInvalid Employee ID Records:")
print(invalid_employee_ids)

print("\nTotal Invalid Employee IDs:")
print(len(invalid_employee_ids))

# Check duplicate employee IDs
duplicate_employees = company_df[
    company_df["employee_id"].duplicated()
]

print("\nDuplicate Employee Records:")
print(duplicate_employees)

print("\nTotal Duplicate Employees:")
print(len(duplicate_employees))


# Salary validation

invalid_salary = company_df[
    company_df["basic_salary"].notnull() &
    (company_df["basic_salary"] <= 0)
]

print("\nInvalid Salary Records:")
print(invalid_salary)

print("\nTotal Invalid Salaries:")
print(len(invalid_salary))


# Negative bonus validation

invalid_bonus = company_df[
    company_df["bonus"].notnull() &
    (company_df["bonus"] < 0)
]

print("\nInvalid Bonus Records:")
print(invalid_bonus)

print("\nTotal Invalid Bonuses:")
print(len(invalid_bonus))

# Sales amount validation

invalid_sales = company_df[
    company_df["sale_amount"].notnull() &
    (company_df["sale_amount"] <= 0)
]

print("\nInvalid Sales Records:")
print(invalid_sales)

print("\nTotal Invalid Sales:")
print(len(invalid_sales))


# Duplicate transaction validation

duplicate_transactions = company_df[
    company_df["transaction_id"].notnull() &
    company_df["transaction_id"].duplicated()
]

print("\nDuplicate Transactions:")
print(duplicate_transactions)

print("\nTotal Duplicate Transactions:")
print(len(duplicate_transactions))

# Overall Data Quality Summary

print("\n========== DATA QUALITY SUMMARY ==========")

print("Total Employees:", len(company_df))
print("Invalid Employee IDs:", len(invalid_employee_ids))
print("Duplicate Employees:", len(duplicate_employees))
print("Invalid Salaries:", len(invalid_salary))
print("Invalid Bonuses:", len(invalid_bonus))
print("Invalid Sales:", len(invalid_sales))
print("Duplicate Transactions:", len(duplicate_transactions))

print("\nData Quality Validation Completed!")