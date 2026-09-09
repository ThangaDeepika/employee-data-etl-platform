from backend.database.connection import (
    get_connection
)

def insert_employee_data(records):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT IGNORE INTO employee_data
    (
        EE_ID,
        EE_name,
        Age,
        Salary,
        Location,
        source_file
    )
    VALUES
    (%s,%s,%s,%s,%s,%s)
    """

    cursor.executemany(
        query,
        records
    )

    connection.commit()

    cursor.close()
    connection.close()

def insert_audit_log(data):

    print("AUDIT DATA RECEIVED:", data)

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO audit_log
    (
        file_name,
        total_records,
        valid_records,
        duplicate_records,
        invalid_records
    )
    VALUES
    (%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        data
    )

    connection.commit()

    print("AUDIT INSERT SUCCESS")

    cursor.close()
    connection.close()

def insert_error_log(data):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO error_log
    (
        file_name,
        row_num,
        error_type,
        error_message
    )
    VALUES
    (%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        data
    )

    connection.commit()

    cursor.close()
    connection.close()

