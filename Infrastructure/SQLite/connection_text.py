import sqlite3
conn = sqlite3.connect("codal.db")
cursor = conn.cursor()


query ="""
    /* select * from FinancialData*/
    SELECT *
    FROM FinancialData f
    WHERE (year, period) = (
        SELECT year, period
        FROM FinancialData
        WHERE Symbol = f.Symbol
        ORDER BY year DESC, period DESC
        LIMIT 1
);
"""
query2 = """
    select * from   FinancialAdjustments
"""
