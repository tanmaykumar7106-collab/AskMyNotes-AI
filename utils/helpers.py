import os


def ensure_directory(path):
    """
    Create directory if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)