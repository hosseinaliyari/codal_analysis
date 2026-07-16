from infrastructure.connection.connection_text import get_connection
from domain.entities.EconomicData import EconomicData
from domain.repositories.IEconomicData import IEconomicData

class RepositoriesEconomicData(IEconomicData) :
  
    def add(self, economic_data):
        addquery =(""" INSERT INTO EconomicData (Year, DollarNima, InterestRate, UpdateDate)
        VALUES (?,?,?,?)""")
        conn = get_connection()
        conn.execute(addquery,(
            economic_data.year,
            economic_data.dollar_nima,
            economic_data.interest_rate,
            economic_data.update_date
        ))
        conn.commit()
        conn.close()

    def get_by_year(self, year):
        conn = get_connection()
        cursor = conn.execute("""
            SELECT
                Year,
                DollarNima,
                InterestRate,
                UpdateDate
            FROM EconomicData
            WHERE Year = ?
        """,(year,))
        row = cursor.fetchone()
        conn.close()
        if row is None:
            return None
        return EconomicData(*row)

    def get_all(self):
        conn = get_connection()
        cursor = conn.execute("""
            SELECT
                Year,
                DollarNima,
                InterestRate,
                UpdateDate
            FROM EconomicData
            ORDER BY Year
        """)
        rows = cursor.fetchall()
        conn.close()
        return [EconomicData(*row) for row in rows]

    def update(self, economic_data):
        conn = get_connection()
        conn.execute("""
            UPDATE EconomicData
            SET
                DollarNima=?,
                InterestRate=?,
                UpdateDate=?
            WHERE Year=?
        """,
        (
            economic_data.dollar_nima,
            economic_data.interest_rate,
            economic_data.update_date,
            economic_data.year
        ))
        conn.commit()
        conn.close()

    def delete(self, year):
        conn = get_connection()
        conn.execute("""
            DELETE
            FROM EconomicData
            WHERE Year=?
        """,(year,))
        conn.commit()
        conn.close()