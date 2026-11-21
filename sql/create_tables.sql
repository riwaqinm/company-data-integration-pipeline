CREATE TABLE IF NOT EXISTS employees  (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    department VARCHAR(50),
    hire_date DATE
);
CREATE TABLE IF NOT EXISTS salary_records  (
    salary_id SERIAL PRIMARY KEY,
    employee_id INT NOT NULL,
    basic_salary NUMERIC(10,2) NOT NULL,
    bonus NUMERIC(10,2) DEFAULT 0,
    salary_month DATE NOT NULL,

    FOREIGN KEY (employee_id)
    REFERENCES employees(employee_id)
);

CREATE TABLE IF NOT EXISTS sales_records (
    sales_id SERIAL PRIMARY KEY,
    employee_id INT NOT NULL,
    transaction_id VARCHAR(50) UNIQUE NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    sale_amount NUMERIC(10,2) NOT NULL,
    sale_date DATE NOT NULL,

    FOREIGN KEY (employee_id)
    REFERENCES employees(employee_id)
);