
import pandas as pd
from database import get_connection


# Load validated company data
company_df = pd.read_csv(
    "data/processed/validated_company_data.csv"
)

# Prepare records for each staging table

employees_df = company_df[
    [
        "employee_id",
        "employee_name",
        "email",
        "department",
        "hire_date"
    ]
].dropna(subset=["employee_id"])

salary_df = company_df[
    [
        "employee_id",
        "basic_salary",
        "bonus",
        "salary_month"
    ]
].dropna(
    subset=["employee_id", "basic_salary", "salary_month"]
)

sales_df = company_df[
    [
        "transaction_id",
        "employee_id",
        "product_name",
        "sale_amount",
        "sale_date"
    ]
].dropna(
    subset=[
        "transaction_id",
        "employee_id",
        "product_name",
        "sale_amount",
        "sale_date"
    ]
)


# Connect to PostgreSQL
connection = get_connection()

try:

    cursor = connection.cursor()

    # STEP 1: Load HR records
    for _, row in employees_df.iterrows():

        cursor.execute(
            """
            INSERT INTO stg_employees
            (employee_id, employee_name, email, department, hire_date)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (employee_id) DO NOTHING
            """,
            (
                int(row["employee_id"]),
                row["employee_name"],
                None if pd.isna(row["email"]) else row["email"],
                row["department"],
                row["hire_date"]
            )
        )

    print("HR records processed:", len(employees_df))


    # STEP 2: Load Finance records
    for _, row in salary_df.iterrows():

        cursor.execute(
            """
            INSERT INTO stg_salary_records
            (employee_id, basic_salary, bonus, salary_month)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (employee_id, salary_month) DO NOTHING
            """,
            (
                int(row["employee_id"]),
                row["basic_salary"],
                None if pd.isna(row["bonus"]) else row["bonus"],
                row["salary_month"]
            )
        )

    print("Finance records processed:", len(salary_df))


    # STEP 3: Load Sales records
    for _, row in sales_df.iterrows():

        cursor.execute(
            """
            INSERT INTO stg_sales_records
            (transaction_id, employee_id, product_name,
             sale_amount, sale_date)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (transaction_id) DO NOTHING
            """,
            (
                row["transaction_id"],
                int(row["employee_id"]),
                row["product_name"],
                row["sale_amount"],
                row["sale_date"]
            )
        )

    print("Sales records processed:", len(sales_df))


    # Commit all three loads together
    connection.commit()

    print("\nValidated data loaded successfully!")
    print("PostgreSQL transaction committed!")

except Exception as error:

    connection.rollback()

    print("\nData loading failed!")
    print("Transaction rolled back.")
    print(error)

    raise

finally:

    cursor.close()
    connection.close()
