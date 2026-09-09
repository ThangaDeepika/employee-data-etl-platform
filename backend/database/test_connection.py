from backend.database.connection import (
    get_connection
)

try:

    conn = get_connection()

    print(
        "\nDatabase Connected Successfully\n"
    )

    conn.close()

except Exception as error:

    print(error)