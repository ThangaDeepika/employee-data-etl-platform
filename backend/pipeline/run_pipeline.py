from backend.config.settings import (
    SOURCE_FOLDER
)

from backend.services.file_scanner import (
    scan_excel_files
)

from backend.services.file_processor import (
    process_file
)

def main():

    total_files = 0

    total_rows = 0

    total_valid = 0

    total_invalid = 0

    total_duplicates = 0

    for file in scan_excel_files(
            SOURCE_FOLDER):

        total_files += 1

        result = process_file(file)

        if result:

            total_rows += (
                result["rows_read"]
            )

            total_valid += (
                result["valid"]
            )

            total_invalid += (
                result["invalid"]
            )

            total_duplicates += (
                result["duplicates"]
            )

    print("\n")

    print("=" * 60)

    print("FINAL SUMMARY")

    print("=" * 60)

    print(
        f"FILES PROCESSED : "
        f"{total_files}"
    )

    print(
        f"ROWS READ : "
        f"{total_rows}"
    )

    print(
        f"VALID RECORDS : "
        f"{total_valid}"
    )

    print(
        f"INVALID RECORDS : "
        f"{total_invalid}"
    )

    print(
        f"DUPLICATES : "
        f"{total_duplicates}"
    )

    print("=" * 60)


if __name__ == "__main__":

    main()