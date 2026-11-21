CREATE TABLE IF NOT EXISTS stg_employees (
    employee_id INT,
    employee_name VARCHAR(100),
    email VARCHAR(150),
    department VARCHAR(50),
    hire_date DATE
);

CREATE TABLE IF NOT EXISTS stg_salary_records (
    employee_id INT,
    basic_salary NUMERIC(10,2),
    bonus NUMERIC(10,2),
    salary_month DATE
);

CREATE TABLE IF NOT EXISTS stg_sales_records (
    transaction_id VARCHAR(50),
    employee_id INT,
    product_name VARCHAR(100),
    sale_amount NUMERIC(10,2),
    sale_date DATE
);