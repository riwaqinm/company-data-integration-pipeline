
import pandas as pd
from database import get_connection
from logger_config import logger


def generate_reports():

    connection = None

    try:
        # Database Connection
        connection = get_connection()

        print("Database connected successfully!")
        logger.info("Database connected successfully")

        # 1. Department Report
        department_query = """
            SELECT
                department,
                COUNT(*) AS total_employees
            FROM stg_employees
            GROUP BY department
            ORDER BY total_employees DESC;
        """

        department_df = pd.read_sql(department_query, connection)

        department_df.to_csv(
            "reports/department_report.csv",
            index=False
        )

        print("Department report generated successfully!")
        logger.info("Department report generated successfully")

        # 2. Sales Report
        sales_query = """
            SELECT
                e.department,
                COUNT(s.transaction_id) AS total_transactions,
                SUM(s.sale_amount) AS total_revenue,
                ROUND(AVG(s.sale_amount), 2) AS average_sale
            FROM stg_employees e
            JOIN stg_sales_records s
                ON e.employee_id = s.employee_id
            GROUP BY e.department
            ORDER BY total_revenue DESC;
        """

        sales_df = pd.read_sql(sales_query, connection)

        sales_df.to_csv(
            "reports/sales_report.csv",
            index=False
        )

        print("Sales report generated successfully!")
        logger.info("Sales report generated successfully")

        # 3. Top Employees Report
        top_employees_query = """
            SELECT
                e.employee_id,
                e.employee_name,
                e.department,
                COUNT(s.transaction_id) AS total_transactions,
                SUM(s.sale_amount) AS total_sales
            FROM stg_employees e
            JOIN stg_sales_records s
                ON e.employee_id = s.employee_id
            GROUP BY
                e.employee_id,
                e.employee_name,
                e.department
            ORDER BY total_sales DESC
            LIMIT 5;
        """

        top_employees_df = pd.read_sql(
            top_employees_query,
            connection
        )

        top_employees_df.to_csv(
            "reports/top_employees.csv",
            index=False
        )

        print("Top employees report generated successfully!")
        logger.info("Top employees report generated successfully")

        print(top_employees_df)

        # 4. Company Summary Report
        summary_query = """
            SELECT
                (SELECT COUNT(*) FROM stg_employees) AS total_employees,
                (SELECT COUNT(*) FROM stg_salary_records) AS salary_records,
                (SELECT COUNT(*) FROM stg_sales_records) AS total_transactions,
                (SELECT SUM(sale_amount) FROM stg_sales_records) AS total_revenue,
                (SELECT SUM(basic_salary + bonus)
                 FROM stg_salary_records) AS total_salary_expense;
        """

        summary_df = pd.read_sql(summary_query, connection)

        summary = summary_df.iloc[0]

        with open("reports/company_summary.txt", "w") as file:
            file.write("COMPANY PERFORMANCE SUMMARY\n")
            file.write("============================\n\n")
            file.write(
                f"Total Employees: {int(summary['total_employees'])}\n"
            )
            file.write(
                f"Salary Records: {int(summary['salary_records'])}\n"
            )
            file.write(
                f"Sales Transactions: {int(summary['total_transactions'])}\n"
            )
            file.write(
                f"Total Revenue: {summary['total_revenue']:,.2f}\n"
            )
            file.write(
                f"Total Salary Expense: {summary['total_salary_expense']:,.2f}\n"
            )

        print("Company summary report generated successfully!")
        logger.info("Company summary report generated successfully")

        print("\nAll reports generated successfully!")
        logger.info("All business reports generated successfully")

    except Exception as error:

        print("\nReport generation failed!")

        logger.exception(
            "Report generation failed: %s",
            error
        )

        raise

    finally:

        if connection is not None:
            connection.close()
            logger.info("Database connection closed")


if __name__ == "__main__":
    generate_reports()
