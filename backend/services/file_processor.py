import os
import pandas as pd

from backend.config.settings import (
    EXPECTED_COLUMNS
)

from backend.services.validator import (
    count_null_records,
    count_duplicate_records,
    count_negative_salary,
    count_invalid_age
)

from backend.services.cleaner import (
    clean_dataframe,
    remove_duplicates,
    remove_negative_salary,
    remove_invalid_age,
    remove_null_values
)

from backend.services.memory_handler import (
    release_memory
)

from backend.database.repository import (
    insert_employee_data,
    insert_error_log,
    insert_audit_log
)


def process_file(file_path):

    try:

        df = pd.read_excel(file_path)

        file_name = os.path.basename(file_path)

        actual_columns = [
            str(col).strip()
            for col in df.columns
        ]

        print("\n" + "=" * 60)

        print(
            f"FILE : {file_name}"
        )

        print(
            f"ROWS READ : {len(df)}"
        )

        if actual_columns != EXPECTED_COLUMNS:

            print(
                "COLUMN VALIDATION : FAIL"
            )

            return None

        print(
            "COLUMN VALIDATION : PASS"
        )

        duplicate_count = int(
            count_duplicate_records(df)
        )

        null_count = int(
            count_null_records(df)
        )

        negative_count = int(
            count_negative_salary(df)
        )

        invalid_age_count = int(
            count_invalid_age(df)
        )

        print(
            f"NULL RECORDS : {null_count}"
        )

        print(
            f"DUPLICATES : {duplicate_count}"
        )

        print(
            f"NEGATIVE SALARY : {negative_count}"
        )

        print(
            f"INVALID AGE : {invalid_age_count}"
        )

        total_invalid = int(

            duplicate_count +

            null_count +

            negative_count +

            invalid_age_count

        )

        # ====================================
        # CLEAN DATA
        # ====================================

        df = clean_dataframe(df)

        df = remove_duplicates(df)

        df = remove_negative_salary(df)

        df = remove_invalid_age(df)

        df = remove_null_values(df)

        valid_record_count = int(
            len(df)
        )

        print(
            f"VALID RECORDS : {valid_record_count}"
        )

        print(
            f"INVALID RECORDS : {total_invalid}"
        )

        # ====================================
        # PREPARE VALID RECORDS
        # ====================================

        records = [

            (
                int(row["EE_ID"]),
                str(row["EE_name"]),
                int(row["Age"]),
                float(row["Salary"]),
                str(row["Location"]),
                str(file_name)
            )

            for _, row in df.iterrows()

        ]

        # ====================================
        # INSERT VALID DATA
        # ====================================

        if records:

            insert_employee_data(
                records
            )

        # ====================================
        # INSERT ERROR LOGS
        # ====================================

        if invalid_age_count:

            insert_error_log(
                (
                    str(file_name),
                    0,
                    "INVALID_AGE",
                    f"{invalid_age_count} invalid age records"
                )
            )

        if null_count:

            insert_error_log(
                (
                    str(file_name),
                    0,
                    "NULL_RECORD",
                    f"{null_count} null records"
                )
            )

        if negative_count:

            insert_error_log(
                (
                    str(file_name),
                    0,
                    "NEGATIVE_SALARY",
                    f"{negative_count} negative salary records"
                )
            )

        if duplicate_count:

            insert_error_log(
                (
                    str(file_name),
                    0,
                    "DUPLICATE_RECORD",
                    f"{duplicate_count} duplicate records"
                )
            )

        # ====================================
        # INSERT AUDIT LOG
        # ====================================

        audit_record = (

            str(file_name),

            int(valid_record_count + total_invalid),

            int(valid_record_count),

            int(duplicate_count),

            int(total_invalid)

        )

        print(
            "AUDIT RECORD : ",
            audit_record
        )

        insert_audit_log(
            audit_record
        )

        release_memory(df)

        print("=" * 60)

        return {

            "rows_read":
                int(valid_record_count + total_invalid),

            "valid":
                int(valid_record_count),

            "invalid":
                int(total_invalid),

            "duplicates":
                int(duplicate_count)

        }

    except Exception as error:

        print(
            f"\nERROR : {file_path}"
        )

        print(error)

        return None