import pandas as pd
from infrastructure.connection.ConnectionText import get_connection
from infrastructure.codal.FinancialStatements import financialStatements

class RepositoriesFinancialStatements:

    def get_codal_financialStatements():
        query=("select * from FinancialData")
        conn = get_connection()
        df = pd.read_sql_query(query,conn)
        conn.close()
        return df

    def update_codal_financialStatements():
        query=("""
            INSERT OR IGNORE INTO FinancialData
            (Symbol, Title, period, date, year, Profit, profit_last, Equity)
            VALUES (?,?,?,?,?,?,?,?)
            """)
        financialStatement = financialStatements()
        rows = list(financialStatement.itertuples(index=False, name=None))
        conn = get_connection()
        conn.executemany(query, rows)
        conn.commit()
        conn.close()