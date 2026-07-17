import sqlite3
from pathlib import Path


class ConnectionText:
    def __init__(self):
        self.base_dir = Path(__file__).resolve().parents[2]
        self.db_path = self.base_dir / "codal.db"

    def get_connection(self):
        return sqlite3.connect(self.db_path)