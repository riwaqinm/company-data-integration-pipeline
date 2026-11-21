
import pandas as pd
import os


def validate_data(df):

    os.makedirs("data/rejected", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    # Store rejection reasons for each record
    reasons = pd.Series("", index=df.index, dtype="object")

    def add_reason(condition, message):
        nonlocal reasons

        reasons.loc[condition] = reasons.loc[condition].apply(
            lambda old: old + "; " + message if old else message
        )

    # Missing employee ID
    add_reason(
        df["employee_id"].isna(),
        "Missing employee ID"
    )

    # Duplicate employee ID
    add_reason(
        df["employee_id"].duplicated(keep="first")
        & df["employee_id"].notna(),
        "Duplicate employee ID"
    )

    # Invalid salary
    if "basic_salary" in df.columns:
        add_reason(
            df["basic_salary"].notna()
            & (df["basic_salary"] <= 0),
            "Invalid salary"
        )

    # Invalid sales amount
    if "sale_amount" in df.columns:
        add_reason(
            df["sale_amount"].notna()
            & (df["sale_amount"] <= 0),
            "Invalid sales amount"
        )

    # Duplicate transaction ID
    if "transaction_id" in df.columns:
        add_reason(
            df["transaction_id"].duplicated(keep="first")
            & df["transaction_id"].notna(),
            "Duplicate transaction ID"
        )

    valid_df = df[reasons == ""].copy()

    rejected_df = df[reasons != ""].copy()
    rejected_df["rejection_reason"] = reasons[reasons != ""]

    # Save valid records
    valid_df.to_csv(
        "data/processed/validated_company_data.csv",
        index=False
    )

    # Save rejected records
    rejected_df.to_csv(
        "data/rejected/rejected_records.csv",
        index=False
    )

    print("\n========== VALIDATION RESULTS ==========")
    print("Total Records:", len(df))
    print("Valid Records:", len(valid_df))
    print("Rejected Records:", len(rejected_df))

    print("\nValidation completed!")

    return valid_df, rejected_df
