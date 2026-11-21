
import unittest
import pandas as pd

from src.validate import validate_data


class TestDataValidation(unittest.TestCase):

    def test_valid_records(self):

        df = pd.DataFrame({
            "employee_id": [101, 102],
            "basic_salary": [50000, 60000],
            "sale_amount": [10000, 20000],
            "transaction_id": ["TXN001", "TXN002"]
        })

        valid_df, rejected_df = validate_data(df)

        self.assertEqual(len(valid_df), 2)
        self.assertEqual(len(rejected_df), 0)

    def test_missing_employee_id(self):

        df = pd.DataFrame({
            "employee_id": [101, None],
            "basic_salary": [50000, 60000],
            "sale_amount": [10000, 20000],
            "transaction_id": ["TXN001", "TXN002"]
        })

        valid_df, rejected_df = validate_data(df)

        self.assertEqual(len(valid_df), 1)
        self.assertEqual(len(rejected_df), 1)

        self.assertIn(
            "Missing employee ID",
            rejected_df.iloc[0]["rejection_reason"]
        )

    def test_duplicate_employee_id(self):

        df = pd.DataFrame({
            "employee_id": [101, 101],
            "basic_salary": [50000, 60000],
            "sale_amount": [10000, 20000],
            "transaction_id": ["TXN001", "TXN002"]
        })

        valid_df, rejected_df = validate_data(df)

        self.assertEqual(len(valid_df), 1)
        self.assertEqual(len(rejected_df), 1)

    def test_invalid_salary(self):

        df = pd.DataFrame({
            "employee_id": [101],
            "basic_salary": [-5000]
        })

        valid_df, rejected_df = validate_data(df)

        self.assertEqual(len(valid_df), 0)
        self.assertEqual(len(rejected_df), 1)

    def test_invalid_sales_amount(self):

        df = pd.DataFrame({
            "employee_id": [101],
            "sale_amount": [0]
        })

        valid_df, rejected_df = validate_data(df)

        self.assertEqual(len(valid_df), 0)
        self.assertEqual(len(rejected_df), 1)


if __name__ == "__main__":
    unittest.main()
