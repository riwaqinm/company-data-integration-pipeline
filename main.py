
import subprocess
import sys
import pandas as pd
from datetime import datetime

from src.logger_config import logger
from src.validate import validate_data


def main():

    start_time = datetime.now()

    print("Pipeline Start Time:", start_time)

    print("===================================")
    print(" COMPANY DATA INTEGRATION PIPELINE")
    print("===================================")

    print("\nPipeline started successfully!")

    logger.info("Company Data Integration Pipeline Started")

    try:

        # STEP 1: HR Extraction
        print("\nSTEP 1: Extracting HR Data...")

        subprocess.run(
            [sys.executable, "src/extract.py"],
            check=True
        )

        print("\nHR Extraction Completed!")
        logger.info("HR Extraction Completed")

        # STEP 2: Finance Extraction
        print("\nSTEP 2: Extracting Finance Data...")

        subprocess.run(
            [sys.executable, "src/extract.py"],
            check=True
        )

        print("\nFinance Extraction Completed!")
        logger.info("Finance Extraction Completed")

        # STEP 3: Sales Extraction
        print("\nSTEP 3: Extracting Sales Data...")

        subprocess.run(
            [sys.executable, "src/extract_sales.py"],
            check=True
        )

        print("\nSales Extraction Completed!")
        logger.info("Sales Extraction Completed")

        # STEP 4: Data Integration
        print("\nSTEP 4: Integrating Department Data...")

        subprocess.run(
            [sys.executable, "src/integrate.py"],
            check=True
        )

        print("\nData Integration Completed!")
        logger.info("Data Integration Completed")

        # STEP 5: Data Validation
        print("\nSTEP 5: Validating Integrated Data...")

        integrated_df = pd.read_csv(
            "data/processed/integrated_company_data.csv"
        )

        valid_df, rejected_df = validate_data(integrated_df)

        logger.info(
            "Data validation completed. Valid: %s, Rejected: %s",
            len(valid_df),
            len(rejected_df)
        )

        # STEP 6: PostgreSQL Loading
        print("\nSTEP 6: Loading Data into PostgreSQL...")

        subprocess.run(
            [sys.executable, "src/load.py"],
            check=True
        )

        print("\nPostgreSQL Loading Completed!")
        logger.info("PostgreSQL Loading Completed")

        # STEP 7: Generate Business Reports
        print("\nSTEP 7: Generating Business Reports...")

        subprocess.run(
            [sys.executable, "src/generate_reports.py"],
            check=True
        )

        print("\nBusiness Reports Generated Successfully!")
        logger.info("Business Reports Generated Successfully")

        # Final Success
        print("\n===================================")
        print(" PIPELINE COMPLETED SUCCESSFULLY")
        print("===================================")

        logger.info(
            "Company Data Integration Pipeline Completed Successfully"
        )

    except subprocess.CalledProcessError as error:

        print("\nPipeline failed! Check the error details.")

        logger.error(
            "Pipeline failed at a subprocess. Exit code: %s",
            error.returncode
        )

    except Exception:

        print("\nUnexpected error occurred!")

        logger.exception("Unexpected pipeline error")

    finally:

        end_time = datetime.now()
        execution_time = end_time - start_time

        print("\nPipeline End Time:", end_time)
        print("Total Execution Time:", execution_time)

        logger.info("Pipeline ended at: %s", end_time)
        logger.info("Total execution time: %s", execution_time)


if __name__ == "__main__":
    main()
