# Company Data Integration Pipeline

A Python-based data integration pipeline that extracts, cleans, validates, integrates, and loads company data from multiple sources into PostgreSQL.

## Project Overview

Companies often store information in different formats and systems. This project demonstrates how HR, Finance, and Sales data can be integrated into a centralized PostgreSQL database for reporting and analysis.

## Technologies Used

- Python
- Pandas
- PostgreSQL
- SQL
- psycopg
- Linux (Ubuntu / WSL)
- Git and GitHub
- Python unittest

## Data Sources

| Department | Source | Format |
|---|---|---|
| HR | Employee records | CSV |
| Finance | Salary records | Excel |
| Sales | Transaction records | JSON |

## Pipeline Workflow

1. Extract HR, Finance, and Sales data.
2. Inspect and clean the source datasets.
3. Transform and integrate the datasets using Pandas.
4. Validate records and identify rejected data.
5. Load validated records into PostgreSQL staging tables.
6. Generate business reports using SQL and Pandas.
7. Record pipeline activities using logging.

## Project Structure

```text
company-data-integration-pipeline/
├── data/
│   ├── raw/
│   ├── processed/
│   └── rejected/
├── logs/
├── reports/
├── sql/
├── src/
├── tests/
├── main.py
└── requirements.txt
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/riwaqinm/company-data-integration-pipeline.git
cd company-data-integration-pipeline
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create the PostgreSQL database and configure the connection details in a `.env` file using `.env.example` as a reference.

Do not upload your actual `.env` file or database password to GitHub.

### 5. Run database scripts

Execute the required SQL scripts in the `sql/` directory to create the database tables.

### 6. Run the pipeline

```bash
python main.py
```

## Business Reports

The pipeline generates:

- Department Report
- Sales Report
- Top Employees Report
- Company Performance Summary

Reports are saved in the `reports/` directory.

## Data Validation

The pipeline checks for:

- Missing employee IDs
- Duplicate employee IDs
- Invalid salary values
- Invalid sales amounts
- Duplicate transaction IDs

Rejected records are saved separately with rejection reasons.

## Logging and Error Handling

The pipeline records execution activities, errors, completion status, and total execution time in `logs/pipeline.log`.

## Automated Testing

Run the validation unit tests:

```bash
python -m unittest tests.test_validate -v
```

The project includes five automated validation tests.

## Project Highlights

- Multiple-source data extraction
- Data cleaning and transformation
- Dataset integration using Pandas
- PostgreSQL database loading
- Data validation and rejection handling
- SQL-based business reporting
- Logging and exception handling
- Automated pipeline execution
- Unit testing

## Author

Riwaqi

University of Vavuniya

**Project:** Company Data Integration Pipeline
