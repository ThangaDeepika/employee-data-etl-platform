import os

from backend.config.settings import (
    ALLOWED_EXTENSIONS
)


def scan_excel_files(folder_path):
    """
    Scan all folders and sub-folders
    and return Excel files.
    """

    for root, _, files in os.walk(folder_path):

        for file in files:

            if file.lower().endswith(
                tuple(ALLOWED_EXTENSIONS)
            ):

                yield os.path.join(
                    root,
                    file
                )