from infrastructure.connection.connection_text import get_connection
from infrastructure.codal.financial_statements import financialStatements

query=("""
        INSERT OR IGNORE INTO FinancialData
        (Symbol, Title, period, date, year, Profit, profit_last, Equity)
        VALUES (?,?,?,?,?,?,?,?)
        """)

def update_codal_financialStatements():
    financialStatement = financialStatements()
    rows = list(financialStatement.itertuples(index=False, name=None))
    conn = get_connection()
    conn.executemany(query, rows)
    conn.commit()
    conn.close()