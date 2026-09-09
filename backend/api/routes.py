from fastapi import APIRouter

from backend.database.connection import (
    get_connection
)

router = APIRouter()


@router.get("/health")
def health_check():

    return {
        "status": "UP"
    }


@router.get("/dashboard-summary")
def dashboard_summary():

    connection = get_connection()

    cursor = connection.cursor()

    try:

        cursor.execute(
            "SELECT COUNT(*) FROM employee_data"
        )

        unique_employees = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM error_log"
        )

        total_errors = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM audit_log"
        )

        files_processed = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COALESCE(
                SUM(total_records),
                0
            )
            FROM audit_log
            """
        )

        total_rows_read = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COALESCE(
                SUM(valid_records),
                0
            )
            FROM audit_log
            """
        )

        valid_records = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COALESCE(
                SUM(invalid_records),
                0
            )
            FROM audit_log
            """
        )

        invalid_records = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COALESCE(
                SUM(duplicate_records),
                0
            )
            FROM audit_log
            """
        )

        duplicate_records = cursor.fetchone()[0]

        return {

            "unique_employees":
                unique_employees,

            "files_processed":
                files_processed,

            "total_rows_read":
                total_rows_read,

            "valid_records":
                valid_records,

            "invalid_records":
                invalid_records,

            "duplicate_records":
                duplicate_records,

            "total_errors":
                total_errors

        }

    finally:

        cursor.close()
        connection.close()


@router.get("/audit")
def get_audit_log():

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    try:

        cursor.execute(
            """
            SELECT *
            FROM audit_log
            ORDER BY id DESC
            """
        )

        return cursor.fetchall()

    finally:

        cursor.close()
        connection.close()


@router.get("/errors")
def get_errors():

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    try:

        cursor.execute(
            """
            SELECT *
            FROM error_log
            ORDER BY id DESC
            """
        )

        return cursor.fetchall()

    finally:

        cursor.close()
        connection.close()


@router.get("/employees")
def get_employees():

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    try:

        cursor.execute(
            """
            SELECT *
            FROM employee_data
            ORDER BY EE_ID
            """
        )

        return cursor.fetchall()

    finally:

        cursor.close()
        connection.close()