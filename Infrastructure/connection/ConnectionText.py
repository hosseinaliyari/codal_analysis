import sqlite3
from pathlib import Path



base_dir = Path(__file__).resolve().parents[2]
db_path = base_dir / "codal.db"

def get_connection():
    return sqlite3.connect(db_path)