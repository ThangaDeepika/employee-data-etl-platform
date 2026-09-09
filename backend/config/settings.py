import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

SOURCE_FOLDER = os.getenv("SOURCE_FOLDER")
ARCHIVE_FOLDER = os.getenv("ARCHIVE_FOLDER")
REJECTED_FOLDER = os.getenv("REJECTED_FOLDER")

EXPECTED_COLUMNS = [
    "EE_ID",
    "EE_name",
    "Age",
    "Salary",
    "Location"
]

ALLOWED_EXTENSIONS = [
    ".xlsx",
    ".xls"
]