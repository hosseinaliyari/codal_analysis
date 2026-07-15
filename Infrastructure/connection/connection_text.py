from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parents[2]
db_path = BASE_DIR / "codal.db"
def get_connection():
    return sqlite3.connect(db_path)